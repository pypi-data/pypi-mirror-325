import requests
from .BaseApi import BaseAPI
from .. import TaloGameServicesApi as TGS


class PlayerAuthAPI(BaseAPI):
    def __init__(
        self,
        api_key: str,
        api: TGS,
        api_url: str = "https://api.trytalo.com",
        dev: bool = False,
    ):
        self.api_key = api_key
        self.base_url = api_url + "/v1/players/auth"
        self.headers = {"Authorization": f"Bearer {self.api_key}", "X-Talo-Dev-Build": dev}

    def login(self, username, password):
        url = self.base_url + "/login"
        data = {"username": username, "password": password}
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def register(self, username, password):
        url = self.base_url + "/register"
        data = {"username": username, "password": password}
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def logout(self, token):
        url = self.base_url + "/logout"
        response = requests.post(url, headers=self.headers)
        return response
