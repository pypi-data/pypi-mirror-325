import requests

class PolarisXRestClient:
    def __init__(self, api_endpoint: str):
        """
        REST client to interact with Polaris (extended) APIs.
        """
        self.api_endpoint = api_endpoint

    def post(self, endpoint: str, json_payload: dict):
        """
        Sends a POST request to a Polaris API endpoint.
        """
        url = f"{self.api_endpoint}{endpoint}"
        response = requests.post(url, json=json_payload)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()

    def get(self, endpoint: str):
        """
        Sends a GET request to a Polaris API endpoint.
        """
        url = f"{self.api_endpoint}{endpoint}"
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
