import copy
from datetime import date
from typing import Tuple, Union, Iterator, Dict, Any, List
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

        Returns
        -------
        ODataQuery
            Self for method chaining
        """
        self._top = n
        logger.debug(f"Set top: {n}")
        return self
    
    def skip(self, n: int) -> 'ODataQuery':
        """
        Skip first n records.

        Parameters
        ----------
        n : int
            Number of records to skip.

        Returns
        -------
        ODataQuery
            Self for method chaining
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

        Returns
        -------
        ODataQuery
            Self for method chaining
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

        Returns
        -------
        ODataQuery
            Self for method chaining
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
            Field names for ASC or tuples of (field, 'desc') for DESC.

        Returns
        -------
        ODataQuery
            Self for method chaining
        """
        for field in fields:
            if isinstance(field, tuple):
                self._orderby.append(f"{field[0]} {field[1]}")
            else:
                self._orderby.append(field)
        logger.debug(f"Added orderby fields: {fields}")
        return self

    def clone(self) -> 'ODataQuery':
        """
        Create a deep copy of the query.

        Returns
        -------
        ODataQuery
            Cloned query object
        """
        logger.debug("Cloning query")
        return copy.deepcopy(self)
    
    def _build_url(self) -> str:
        """Build OData URL with query parameters."""
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

    def _fetch_page(self, url: str, timeout: int) -> Dict[str, Any]:
        """
        Fetch a single page of results.

        Parameters
        ----------
        url : str
            URL to fetch
        timeout : int
            Request timeout in seconds

        Returns
        -------
        Dict[str, Any]
            JSON response
        """
        logger.info(f"Fetching URL: {url}")
        response = requests.get(url, auth=self.credentials, timeout=timeout)
        response.raise_for_status()
        return response.json()
    
    def __iter__(self) -> Iterator[Dict[str, Any]]:
        """
        Iterator over query results.

        Yields
        ------
        Dict[str, Any]
            Individual records
        """
        url = self._build_url()
        total_retrieved = 0
        
        while True:
            data = self._fetch_page(url, timeout=30)
            
            for record in data['value']:
                if self._top and total_retrieved >= self._top:
                    return
                yield record
                total_retrieved += 1
            
            next_link = data.get('@odata.nextLink')
            if not next_link:
                break
                
            url = next_link
    
    def fetch(self, as_dataframe=True, timeout=30) -> Union[pd.DataFrame, dict]:
        """
        Execute query and fetch results.

        Parameters
        ----------
        as_dataframe : bool, default True
            Return results as pandas DataFrame if True, else as dict
        timeout : int, default 30
            Request timeout in seconds

        Returns
        -------
        Union[pd.DataFrame, dict]
            Query results
        """
        all_records = list(self)
        
        if not as_dataframe:
            return {'value': all_records}
            
        df = pd.DataFrame(all_records)
        
        if self._select and not df.empty:
            df = df[self._select]
            df = df.rename(columns=self._column_map)
            
        return df

    def batch_fetch(self, field: str, values: list, 
                   batch_size: int = 25,
                   as_dataframe=True) -> Union[pd.DataFrame, list[dict]]:
        """
        Fetch records in batches based on field values.

        Parameters
        ----------
        field : str
            Field name to filter on
        values : list
            List of values to filter for
        batch_size : int, default 25
            Number of values per batch
        as_dataframe : bool, default True
            Return results as pandas DataFrame if True, else as dict

        Returns
        -------
        Union[pd.DataFrame, dict]
            Combined results from all batches

        Examples
        --------
        >>> query.select('OrderNo', 'Amount')\\
        ...      .filter(Q('Status') == 'Open')\\
        ...      .batch_fetch('OrderNo', order_numbers)
        """
        batches = [values[i:i + batch_size] for i in range(0, len(values), batch_size)]
        all_records = []
        base_query = self.clone()
        
        for batch in batches:
            # Build OR conditions for current batch
            batch_filter = ' or '.join(
                f"({field} eq {Q('')._make_value_str(value)})" 
                for value in batch
            )
            
            # Create new query with batch filter + existing filters
            query = base_query.clone()
            query._filters.append(batch_filter)
            
            # Get results using existing fetch logic
            batch_records = list(query)
            all_records.extend(batch_records)
            
        if not as_dataframe:
            return all_records
            
        df = pd.DataFrame(all_records)
        if self._select and not df.empty:
            df = df[self._select]
            df = df.rename(columns=self._column_map)
        return df


class OData:
    """
    OData client factory.

    Parameters
    ----------
    base_url : str
        Base URL for the OData service
    credentials : tuple, optional
        (username, password) for basic auth

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