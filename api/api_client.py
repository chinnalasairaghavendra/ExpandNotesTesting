import requests
from utils.logger import get_logger

class APIClient:

    def __init__(self, base_url):

        self.base_url = base_url
        self.token = None
        self.logger = get_logger(self.__class__.__name__)

    def get_headers(self):

        headers = {
            "Content-Type": "application/json"
        }

        if self.token:
            headers["x-auth-token"] = self.token

        return headers

    def get(self, endpoint):

        self.logger.info(f"GET Request -> {self.base_url}{endpoint}")
        response=requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.get_headers()
        )
        self.logger.info(
            f"Response Status -> {response.status_code}"
        )
        return response

    def post(self, endpoint, payload=None):
        self.logger.info(
            f"POST Request -> {self.base_url}{endpoint}"
        )

        self.logger.info(
            f"Payload -> {payload}"
        )
        response=requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.get_headers()
        )
        self.logger.info(
            f"Response Status -> {response.status_code}"
        )
        return response

    def delete(self, endpoint):
        self.logger.info(
            f"DELETE Request -> {self.base_url}{endpoint}"
        )
        response=requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.get_headers()
        )
        self.logger.info(
            f"Response Status -> {response.status_code}"
        )
        return response