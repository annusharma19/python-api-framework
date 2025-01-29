import requests
from configs.config import BASE_URL, HEADERS
from utils.logger import logger


class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        logger.info(f"GET {url} - Status: {response.status_code}")
        return response

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload, headers=self.headers)
        logger.info(f"POST {url} - Status: {response.status_code} - Response: {response.json()}")
        return response

    def put(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=payload, headers=self.headers)
        logger.info(f"PUT {url} - Status: {response.status_code}")
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers)
        logger.info(f"DELETE {url} - Status: {response.status_code}")
        return response
