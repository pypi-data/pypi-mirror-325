import requests;
def fetch_api_data(url, params=None, headers=None):
    """
    Fetches data from the given API URL.

    :param url: API endpoint (string)
    :param params: Optional query parameters (dictionary)
    :param headers: Optional request headers (dictionary)
    :return: JSON response or None if an error occurs
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an error for HTTP errors (4xx, 5xx)
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None