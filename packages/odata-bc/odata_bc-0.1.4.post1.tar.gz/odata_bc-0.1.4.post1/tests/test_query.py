# tests/test_query.py
from urllib.parse import parse_qs, urlparse

from odata import Q


def test_filter_builds_correct_url(client):
   """
   Test filter() method generates correct $filter parameter in URL.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   """
   query = client("sales").filter(Q("Type") == "Sale")
   url = query._build_url()
   params = parse_qs(urlparse(url).query)
   assert params["$filter"][0] == "((Type eq 'Sale'))"

def test_select_renames_columns(client, mock_response):
   """
   Test select() with column aliasing.
   Verifies DataFrame columns are properly renamed.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   mock_response : None
       Fixture that patches HTTP responses
   """
   df = client("sales").select(
       "Date", 
       ("Type", "TransactionType")
   ).fetch()
   assert "TransactionType" in df.columns
   assert "Type" not in df.columns

def test_orderby_single_field(client):
   """
   Test orderby() with single field ascending sort.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   """
   query = client("sales").orderby("Date")
   url = query._build_url()
   params = parse_qs(urlparse(url).query)
   assert params["$orderby"][0] == "Date"

def test_orderby_multiple_fields(client):
   """
   Test orderby() with multiple fields and mixed sort directions.
   Verifies correct formatting of $orderby parameter.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   """
   query = client("sales").orderby("Date", ("Amount", "desc"))
   url = query._build_url()
   params = parse_qs(urlparse(url).query)
   assert params["$orderby"][0] == "Date,Amount desc"

def test_top_adds_parameter(client):
   """
   Test top() adds correct $top parameter to URL.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   """
   query = client("sales").top(10)
   url = query._build_url()
   params = parse_qs(urlparse(url).query)
   assert params["$top"][0] == "10"

def test_expand_adds_parameter(client):
   """
   Test expand() generates correct $expand parameter.
   Verifies multiple expand fields are comma-separated.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   """
   query = client("sales").expand("Details", "Customer")
   url = query._build_url()
   params = parse_qs(urlparse(url).query)
   assert params["$expand"][0] == "Details,Customer"

def test_clone_creates_independent_copy(client):
   """
   Test clone() creates deep copy with independent state.
   Verifies modifications to clone don't affect original.
   
   Parameters
   ----------
   client : OData
       Fixture providing configured test client
   """
   query1 = client("sales").filter(Q("Type") == "Sale")
   query2 = query1.clone()
   query2.top(10)
   
   url1 = query1._build_url()
   url2 = query2._build_url()
   
   params1 = parse_qs(urlparse(url1).query)
   params2 = parse_qs(urlparse(url2).query)
   
   assert "$top" not in params1
   assert params2["$top"][0] == "10"