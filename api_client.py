import requests


class APIClient:
    """Reusable REST API client."""

    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, endpoint, params=None):
        """Send a GET request and return JSON data."""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print("Error: API request timed out.")

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the API.")

        except requests.exceptions.HTTPError as error:
            print(f"HTTP error: {error}")

        except requests.exceptions.JSONDecodeError:
            print("Error: API returned invalid JSON.")

        return None