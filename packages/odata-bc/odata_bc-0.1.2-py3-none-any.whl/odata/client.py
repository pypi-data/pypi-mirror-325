import copy
from datetime import date
from typing import Tuple, Union
from urllib.parse import urlencode

import pandas as pd
import requests
from loguru import logger


class Q:
    """
    Query expression builder for OData filters.

    Parameters
    ----------
    field : str
        Name of the field to filter on.

    Examples
    --------
    >>> Q("Date") >= date(2024,1,1)
    >>> (Q("Type") == "Sale") | (Q("Type") == "Purchase")
    """
    def __init__(self, field: str):
        self.field = field
        self.value = None
        self.op = None
        self.left = None
        self.right = None
        
    def _make_value_str(self, value: Union[str, int, float, date]) -> str:
        if isinstance(value, str):
            return f"'{value}'"
        if isinstance(value, date):
            return value.strftime('%Y-%m-%d')
        return str(value)
    
    def __eq__(self, other): 
        self.op = 'eq'
        self.value = other
        return self
        
    def __ge__(self, other):
        self.op = 'ge'
        self.value = other
        return self
        
    def __le__(self, other):
        self.op = 'le'
        self.value = other
        return self
        
    def __gt__(self, other):
        self.op = 'gt'
        self.value = other
        return self
        
    def __lt__(self, other):
        self.op = 'lt'
        self.value = other
        return self
        
    def __ne__(self, other):
        self.op = 'ne'
        self.value = other
        return self
    
    def __and__(self, other):
        result = Q('')
        result.left = self
        result.right = other
        result.op = 'and'
        return result
    
    def __or__(self, other):
        result = Q('')
        result.left = self
        result.right = other
        result.op = 'or'
        return result
        
    def __str__(self):
        if self.value is not None:
            return f"({self.field} {self.op} {self._make_value_str(self.value)})"
        return f"({str(self.left)} {self.op} {str(self.right)})"

class ODataQuery:
    """
    OData query builder using method chaining.

    Parameters
    ----------
    service : str
        Service endpoint name.
    base_url : str
        Base URL for the OData service.
    credentials : tuple, optional
        (username, password) for basic auth.

    Examples
    --------
    >>> query = ODataQuery("sales", "http://api.example.com")
    >>> query.filter(Q("Amount") > 1000).top(10).fetch()
    """
    def __init__(self, service: str, base_url: str, credentials: tuple = None):
        self.service = service
        self.base_url = base_url.rstrip('/')
        self.credentials = credentials
        self._filters = []
        self._top = None
        self._select = []
        self._column_map = {}
        self._orderby = []
        self._skip = None
        self._expand = []
        logger.debug(f"Initialized ODataQuery for service: {service}")
    
    def filter(self, expr: Q) -> 'ODataQuery':
        """
        Add filter expression to query.

        Parameters
        ----------
        expr : Q
            Filter expression built using Q class.

        Returns
        -------
        ODataQuery
            Self for method chaining.
        """
        self._filters.append(str(expr))
        logger.debug(f"Added filter: {expr}")
        return self
    
    def top(self, n: int) -> 'ODataQuery':
        """
        Limit number of returned records.

        Parameters
        ----------
        n : int
            Maximum number of records to return.
        """
        self._top = n
        logger.debug(f"Set top: {n}")
        return self
    
    def skip(self, n: int) -> 'ODataQuery':
        """
        Skip first n records (for pagination).

        Parameters
        ----------
        n : int
            Number of records to skip.
        """
        self._skip = n
        logger.debug(f"Set skip: {n}")
        return self

    def expand(self, *fields: str) -> 'ODataQuery':
        """
        Add fields to $expand parameter.

        Parameters
        ----------
        *fields : str
            Field names to expand.
        """
        self._expand.extend(fields)
        logger.debug(f"Added expand fields: {fields}")
        return self
    
    def select(self, *fields: Union[str, Tuple[str, str]]) -> 'ODataQuery':
        """
        Select fields to return.

        Parameters
        ----------
        *fields : Union[str, Tuple[str, str]]
            Field names as strings or tuples of (field, alias).
        """
        for field in fields:
            if isinstance(field, tuple):
                self._select.append(field[0])
                self._column_map[field[0]] = field[1]
            else:
                self._select.append(field)
        logger.debug(f"Added select fields: {fields}")
        return self

    def orderby(self, *fields: Union[str, Tuple[str, str]]) -> 'ODataQuery':
        """
        Set ordering of results.

        Parameters
        ----------
        *fields : Union[str, Tuple[str, str]]
            Field names as strings for ASC or tuples of (field, 'desc') for DESC.
        """
        for field in fields:
            if isinstance(field, tuple):
                self._orderby.append(f"{field[0]} {field[1]}")
            else:
                self._orderby.append(field)
        logger.debug(f"Added orderby fields: {fields}")
        return self

    def clone(self) -> 'ODataQuery':
        """Create a deep copy of the query for reuse."""
        logger.debug("Cloning query")
        return copy.deepcopy(self)
    
    def _build_url(self) -> str:
        """Build OData URL with all query parameters."""
        params = {}
        
        if self._filters:
            params['$filter'] = ' and '.join(f'({f})' for f in self._filters)
        
        if self._top:
            params['$top'] = self._top
            
        if self._skip:
            params['$skip'] = self._skip

        if self._select:
            params['$select'] = ','.join(self._select)

        if self._expand:
            params['$expand'] = ','.join(self._expand)

        if self._orderby:
            params['$orderby'] = ','.join(self._orderby)
            
        query = urlencode(params)
        return f"{self.base_url}/{self.service}?{query}"
    
    def __iter__(self):
        """
        Provide an iterator over the query results. Yields individual record at a time. 
        Automatically handles pagination and respects any filters, selects, and ordering applied to the query.
        """
        page = 0
        total_retrieved = 0
        batch_size = 100  # Internal pagination size
        
        while True:
            query = self.clone()
            remaining = None if not self._top else self._top - total_retrieved
            
            if remaining is not None and remaining <= 0:
                break
                
            query.skip(page * batch_size)
            query.top(batch_size if remaining is None else min(batch_size, remaining))
            data = query.fetch(as_dataframe=False)
            
            if not data['value']:
                break
                
            for record in data['value']:
                yield record
                total_retrieved += 1
                
            page += 1
    
    def fetch(self, as_dataframe=True, timeout=30) -> Union[pd.DataFrame, dict]:
        """
        Execute query and fetch results.

        Parameters
        ----------
        as_dataframe : bool, default True
            Return results as pandas DataFrame if True, else as dict.
        timeout : int, default 30
            Request timeout in seconds.

        Returns
        -------
        Union[pd.DataFrame, dict]
            Query results.
        """
        url = self._build_url()
        logger.info(f"Fetching URL: {url}")
        
        response = requests.get(url, auth=self.credentials, timeout=timeout)
        response.raise_for_status()
        
        data = response.json()
        logger.debug(f"Received {len(data.get('value', []))} records")
        
        if not as_dataframe:
            return data
            
        df = pd.DataFrame(data['value'])
        
        if self._select:
            df = df[self._select]
            df = df.rename(columns=self._column_map)
            
        return df

class OData:
    """
    OData client factory.

    Parameters
    ----------
    base_url : str
        Base URL for the OData service.
    credentials : tuple, optional
        (username, password) for basic auth.

    Examples
    --------
    >>> client = OData("http://api.example.com", ("user", "pass"))
    >>> sales = client("sales")
    """
    def __init__(self, base_url: str, credentials: tuple = None):
        self.base_url = base_url
        self.credentials = credentials
        logger.info(f"Initialized OData client for {base_url}")
    
    def __call__(self, service: str) -> ODataQuery:
        return ODataQuery(service, self.base_url, self.credentials)