import os
from typing import Optional
from og_query_runner import ReadQueryFromFile,RunAndSaveQuery,RunQuery,SaveQueryResults

def example_run_query():
    instance_url = "https://your-instance-url.com"
    query = "SELECT * FROM your_table"
    api_key = "your_api_key"

    try:
        # Run the query
        response = RunQuery(instance_url, query, api_key)
        print("Query executed successfully.")
        print(f"Response: {response}")

    except ValueError as e:
        print(f"ValueError: {e}")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def example_save_query_results():
    data = {
        "query": "SELECT * FROM your_table",
        "headers": ["column1", "column2"],
        "result": [["x", "y"], ["a", "b"]]
    }
    file_path = "query_results"

    try:
        # Save the query results to a CSV file
        SaveQueryResults(data, file_path)
        print(f"Query results successfully saved to {file_path}.csv")

    except ValueError as e:
        print(f"ValueError: {e}")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



# Example function to run a query, save the result, and handle errors.
def example_run_and_save_query():
    instance_url = "https://your-instance-url.com"
    query = "SELECT * FROM your_table"
    api_key = "your_api_key"
    file_path = "query_results"

    try:
        # Run the query and save the results to a CSV file
        RunAndSaveQuery(instance_url, query, api_key, file_path)
        print(f"Query results successfully saved to {file_path}.csv")

    except ValueError as e:
        print(f"ValueError: {e}")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example function to read and print query results from a file
def example_read_query_from_file(file_path: str):
    try:
        # Read query result from CSV file
        result = ReadQueryFromFile(file_path)
        print("Query Result:")
        print(f"Headers: {result['headers']}")
        print(f"Result: {result['result']}")
        if 'query' in result:
            print(f"Original Query: {result['query']}")

    except ValueError as e:
        print(f"ValueError: {e}")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



# main function to run the example functions
if __name__ == "__main__":
    example_run_query()
    example_save_query_results()
    example_run_and_save_query()
    example_read_query_from_file("query_results")
    os.remove("query_results.csv")
    os.remove("query_results.query")
    print("Files removed successfully.")