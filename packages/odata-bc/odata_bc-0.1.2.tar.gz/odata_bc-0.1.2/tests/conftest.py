import pytest
from odata import OData



@pytest.fixture
def mock_response(monkeypatch):
   """
   Mock HTTP responses to avoid real API calls during testing.
   Creates a mock response with sample sales data.
   
   Parameters
   ----------
   monkeypatch : pytest.MonkeyPatch
       Pytest fixture for patching objects
       
   Returns
   -------
   None
       The fixture patches requests.get globally
   """
   class MockResponse:
       def __init__(self, data):
           self._data = data
       
       def json(self):
           return self._data
           
       def raise_for_status(self):
           pass
   
   def mock_get(*args, **kwargs):
       return MockResponse({
           "value": [
               {"Date": "2024-01-01", "Type": "Sale", "Amount": 100},
               {"Date": "2024-01-02", "Type": "Purchase", "Amount": 200}
           ]
       })
   
   monkeypatch.setattr("requests.get", mock_get)

@pytest.fixture
def client():
   """
   Create a test OData client instance.
   
   Returns
   -------
   OData
       Configured client pointing to test URL with credentials
   """
   return OData("http://test.com", ("user", "pass"))