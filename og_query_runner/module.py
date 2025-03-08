import requests
import pandas as pd
from typing import Dict, Any

def RunQuery(instance_url: str, query: str, api_key: str) -> Dict[str, Any]:
    """
    Executes a query on a given instance URL using an API key.

    Args:
        instance_url (str): The base URL of the instance where the query will be executed.
        query (str): The query string to be executed.
        api_key (str): The API key for authentication.

    Returns:
        Dict[str, Any]: The JSON response from the API or an error message if the request fails.
    """
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
        if ("title" in final_response):
            del final_response["title"]
        return final_response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def SaveQueryResults(data: list, file_path: str) -> None:
    """
    Saves query results to a CSV file.

    Args:
        data (list): The query result data, expected to be a list of dictionaries.
        file_path (str): The filename where the results will be saved.

    Returns:
        None
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
