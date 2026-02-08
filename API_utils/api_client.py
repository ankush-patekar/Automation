import requests
from API_utils import config


class APIClient:

    def __init__(self):
        self.base_url = config.BASE_URL
        self.token = None

    def get_token(self):
        payload = {
            "username": config.USERNAME,
            "password": config.PASSWORD
        }

        response = requests.post(self.base_url + config.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 200, "Login Failed"

        self.token = response.json().get("token")
        return self.token

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint, headers=self.get_headers())

    def post(self, endpoint, payload):
        return requests.post(self.base_url + endpoint, json=payload, headers=self.get_headers())
