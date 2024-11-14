import requests
from requests.exceptions import HTTPError, RequestException


class HTTPClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {"Content-Type": "application/json"}

    def get(self, endpoint, params=None):
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}", headers=self.headers, params=params
            )
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None

    def post(self, endpoint, data=None):
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}", headers=self.headers, json=data
            )
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None
