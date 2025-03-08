# Opengovernance Query Runner package

- [Opengovernance Query Runner package](#opengovernance-query-runner-package)
  - [Installation](#installation)
    - [Clone the repository](#clone-the-repository)
    - [Install the package](#install-the-package)
  - [Functions](#functions)
  - [RunQuery](#runquery)
    - [Parameters](#parameters)
    - [Returns](#returns)
    - [Example](#example)
    - [Output](#output)
  - [SaveQueryResults](#savequeryresults)
    - [Parameters](#parameters-1)
    - [Returns](#returns-1)
    - [Example](#example-1)

## Installation

### Clone the repository

```bash
git clone [git@github.com:opengovern/slay-package.git](https://github.com/opengovern/slay-package.git)
```

### Install the package

```bash
pip install .
```

## Functions

- RunQuery
- SaveQueryResults

## RunQuery

RunQuery is a function that takes a query string and a connection string as input and returns the results of the query as a json object.

### Parameters

- query: string
  - The query string to be executed
- instance_url: string
  - url of the instance
- api_key: string
  - api key for authentication
  
### Returns

- json
  - The results of the query as a json object
  
### Example

```python
from og_query_runner import RunQuery
RunQuery("SELECT * FROM table", "https://instance_url", "api_key")
```

### Output

```json
{
  "data": [
    {
      "column1": "value1",
      "column2": "value2"
    },
    {
      "column1": "value3",
      "column2": "value4"
    }
  ]
}
```

## SaveQueryResults

SaveQueryResults is a function that takes a query response and a file path as input and saves the results of the query to a file.

### Parameters

- data : json
  - The results of the query as a json object
- file_path : string
  - The path to the file where the results will be saved. File extension should be .csv

### Returns

- None

### Example

```python
from og_query_runner import SaveQueryResults
SaveQueryResults({"data": [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]}, "results.csv")
```


