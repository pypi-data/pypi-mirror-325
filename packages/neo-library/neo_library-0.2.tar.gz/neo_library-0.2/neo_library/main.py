
import requests

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

# Example usage
if __name__ == "__main__":
    url = "https://api.neo.saint-gobain.com/neo-api/api/v2/outsource/getrealtime"  # Sample API
    data = fetch_api_data(url,'',{"secure-api-key":'tropR$!l6R@5r*vOsWl*+I$U-UPLFre$r!HOBLpHuF34t*Aqu9imaSeWRa@LDoDE//f9de6b31-5969-4ca3-ac36-9e3284a73a45'})
    print(data)