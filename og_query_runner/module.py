import requests
import pandas as pd
from typing import Dict, Any, List, Union

def RunQuery(instance_url: str, query: str, api_key: str) -> Dict[str, Any]:
    """
    Executes a query on a given instance URL using an API key.

    Args:
        instance_url (str): The base URL of the instance where the query will be executed.
        query (str): The query string to be executed.
        api_key (str): The API key for authentication.

    Returns:
        Dict[str, Any]: The JSON response from the API or raises an exception if an error occurs.
    """
    if not isinstance(instance_url, str) or not instance_url:
        raise ValueError("Invalid instance_url. It must be a non-empty string.")
    if not isinstance(query, str) or not query:
        raise ValueError("Invalid query. It must be a non-empty string.")
    if not isinstance(api_key, str) or not api_key:
        raise ValueError("Invalid API key. It must be a non-empty string.")
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "query": query,
        "engine": "cloudql",
        "page": {
            "no": 1,
            "size": 10000
        }
    }
    url = f'{instance_url}/main/core/api/v1/query/run'
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        final_response = response.json()
        if "title" in final_response:
            del final_response["title"]
        return final_response
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error while executing query: {e}")

def SaveQueryResults(data: Dict[str, Union[List[str], List[List[Any]]]], file_path: str) -> None:
    """
    Saves query results to a CSV file.

    Args:
        data (dict): The query result data, expected to contain headers and results.
        Example:
        {
            "query": "SELECT * FROM table",
            "headers": ["column1", "column2"],
            "result": [["x", "y"], ["a", "b"]]
        }
        file_path (str): The filename where the results will be saved.

    Returns:
        None
    """
    if not isinstance(data, dict) or "headers" not in data or "result" not in data:
        raise ValueError("Invalid data format. Expected a dictionary with 'headers' and 'result' keys.")
    if not isinstance(file_path, str) or not file_path:
        raise ValueError("Invalid file_path. It must be a non-empty string.")
    
    try:
        df = pd.DataFrame(data["result"], columns=data["headers"])
        df.to_csv(file_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Error while saving data to CSV: {e}")