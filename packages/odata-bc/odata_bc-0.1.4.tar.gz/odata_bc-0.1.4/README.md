# Python OData Client

A powerful, intuitive, and production-ready OData client for Python with pandas integration.

## Features

- Fluent query building interface
- Comprehensive OData query support ($filter, $select, $expand, $orderby, $top, $skip)
- Batch fetching for large datasets
- Automatic pagination handling with @odata.nextLink
- Pandas DataFrame integration
- Type hints for better IDE support
- Extensible filter expression builder
- Request authentication support
- Logging integration with loguru
- Query cloning for reuse
- Timeout configuration

## Installation

```bash
pip install python-odata-client
```

## Quick Start

```python
from odata import OData, Q
from datetime import date

# Initialize client
client = OData("https://api.example.com", credentials=("user", "pass"))

# Create a query
sales = client("sales")
    .filter((Q("Amount") > 1000) & (Q("Date") >= date(2024, 1, 1)))
    .select("Id", "Amount", ("CustomerName", "client"))
    .orderby(("Amount", "desc"))
    .top(10)

# Execute query and get results as DataFrame
df = sales.fetch()
```

## Detailed Usage

### Client Initialization

Initialize the OData client with your service base URL and optional credentials:

```python
from odata import OData

# Basic initialization
client = OData("https://api.example.com")

# With authentication
client = OData("https://api.example.com", credentials=("username", "password"))
```

### Building Queries

The library provides a fluent interface for building OData queries:

```python
query = client("sales")  # Initialize query for 'sales' endpoint
```

#### Filtering

Use the `Q` class to build filter expressions:

```python
from odata import Q
from datetime import date

# Simple comparisons
query.filter(Q("Amount") > 1000)
query.filter(Q("Status") == "Active")
query.filter(Q("Date") >= date(2024, 1, 1))

# Combining conditions with & (and) and | (or)
query.filter(
    (Q("Type") == "Sale") & 
    (Q("Amount") > 1000) | 
    (Q("Status") == "Priority")
)
```

Supported operators:
- `==` (eq)
- `!=` (ne)
- `>` (gt)
- `>=` (ge)
- `<` (lt)
- `<=` (le)
- `&` (and)
- `|` (or)

#### Batch Fetching

For scenarios where you need to fetch data for a large number of specific values:

```python
# Fetch data for multiple order numbers efficiently
order_numbers = ['SO001', 'SO002', ..., 'SO10000']

results = query.select("OrderNo", "Amount", "Status") \
              .filter(Q("Type") == "Sale") \
              .batch_fetch("OrderNo", order_numbers, batch_size=25)
```

The batch_fetch method:
- Automatically splits values into batches (default 25 per batch)
- Combines with existing filters and query parameters
- Handles pagination within each batch
- Returns combined results as DataFrame or list

#### Select Fields

Select specific fields to return:

```python
# Simple select
query.select("Id", "Name", "Amount")

# With field aliasing
query.select(
    ("Id", "identifier"),
    ("CustomerName", "client"),
    "Amount"
)
```

#### Ordering Results

Order results by one or more fields:

```python
# Ascending order (default)
query.orderby("Date", "Amount")

# Descending order
query.orderby(("Date", "desc"), ("Amount", "desc"))
```

#### Pagination

The client handles pagination automatically using OData's @odata.nextLink. You can still control initial result set size:

```python
# Limit total results
query.top(10)

# Skip initial records
query.skip(20)

# Iterate through all records with automatic pagination
for record in query:
    process_record(record)
```

#### Expanding Related Entities

Include related entities in the results:

```python
query.expand("Customer", "Products")
```

### Executing Queries

#### Fetch as DataFrame

By default, `fetch()` returns results as a pandas DataFrame:

```python
# Default behavior
df = query.fetch()

# With custom timeout (in seconds)
df = query.fetch(timeout=60)
```

#### Fetch as List

Get results as a list of dictionaries:

```python
records = query.fetch(as_dataframe=False)
```

#### Iterating Results

Iterate through individual records with automatic pagination:

```python
# Iterate through all records
for record in query:
    process_record(record)

# With result limit
query.top(50)
for record in query:
    process_record(record)
```

### Query Reuse

Clone queries to reuse and modify them:

```python
base_query = client("sales").filter(Q("Status") == "Active")

# Clone and modify for different uses
high_value = base_query.clone().filter(Q("Amount") > 1000)
low_value = base_query.clone().filter(Q("Amount") < 1000)
```

### Logging

The library uses `loguru` for logging:

```python
from loguru import logger

# Configure logging
logger.add("odata.log", level="DEBUG", rotation="1 day")
```

## Error Handling

The library raises standard HTTP exceptions from the `requests` library:

```python
from requests.exceptions import RequestException

try:
    results = query.fetch()
except RequestException as e:
    print(f"Query failed: {e}")
```

## Type Support

The library includes comprehensive type hints for better IDE support and static type checking:

```python
from typing import Tuple, Union
from datetime import date

def get_sales(client: OData, start_date: date) -> pd.DataFrame:
    return client("sales").filter(Q("Date") >= start_date).fetch()
```

## Performance Considerations

- Use `select()` to limit returned fields when possible
- Use `batch_fetch()` for querying large sets of specific values
- Consider timeouts for slow connections or large queries
- Use `expand()` judiciously as it can increase response size
- Pagination is handled automatically for large result sets

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.