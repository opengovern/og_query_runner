# Opengovernance Query Runner Package

- [Opengovernance Query Runner Package](#opengovernance-query-runner-package)
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
  - [RunAndSaveQuery](#runandsavequery)
    - [Parameters](#parameters-2)
    - [Returns](#returns-2)
    - [Example](#example-2)
  - [ReadQueryFromFile](#readqueryfromfile)
    - [Parameters](#parameters-3)
    - [Returns](#returns-3)
    - [Example](#example-3)
  - [Example File](#example-file)

## Installation

### Clone the repository

```bash
git clone [https://github.com/opengovern/og_query_runner.git](https://github.com/opengovern/og_query_runner.git)
```

### Install the package

```bash
pip install .
```

## Functions

- RunQuery
- SaveQueryResults
- RunAndSaveQuery
- ReadQueryFromFile

## RunQuery

Executes a query on a given instance URL using an API key.

### Parameters

- `instance_url`: string
  - The base URL of the instance where the query will be executed.
- `query`: string
  - The query string to be executed.
- `api_key`: string
  - The API key for authentication.

### Returns

- `dict`
  - The results of the query as a JSON object.

### Example

```python
from og_query_runner import RunQuery

response = RunQuery("https://instance_url", "SELECT * FROM table", "api_key")
print(response)
```

### Output

```json
{
    "headers": ["column1", "column2"],
    "result": [["x", "y"], ["a", "b"]]
}
```

## SaveQueryResults

Saves query results to a CSV file and optionally saves the query itself.

### Parameters

- `data`: dict
  - The results of the query, including headers and result rows.
- `file_path`: string
  - The filename (without `.csv`) where the results will be saved.
- `query`: string (optional)
  - The query string to be saved.

### Returns

- None

### Example

```python
from og_query_runner import SaveQueryResults

SaveQueryResults({
    "headers": ["column1", "column2"],
    "result": [["x", "y"], ["a", "b"]]
}, "results")
```

## RunAndSaveQuery

Executes a query and saves the results to a CSV file.

### Parameters

- `instance_url`: string
  - The base URL of the instance where the query will be executed.
- `query`: string
  - The query string to be executed.
- `api_key`: string
  - The API key for authentication.
- `file_path`: string
  - The filename (without `.csv`) where the results will be saved.

### Returns

- None

### Example

```python
from og_query_runner import RunAndSaveQuery

RunAndSaveQuery("https://instance_url", "SELECT * FROM table", "api_key", "results")
```

## ReadQueryFromFile

Reads a query result from a CSV file and reconstructs it in the same format as `RunQuery`.

### Parameters

- `file_path`: string
  - The path to the CSV file (without `.csv`) containing the query result.

### Returns

- `dict`
  - A dictionary with 'headers' (list of column names) and 'result' (list of row values).

### Example

```python
from og_query_runner import ReadQueryFromFile

result = ReadQueryFromFile("results")
print(result)
```

## Example File

you can find an example file in the repository named [example.py](example.py) that demonstrates how to use the package.


