import requests
from .BaseApi import BaseAPI



class PlayerAuthAPI(BaseAPI):
    def __init__(
        self,
        api_key: str,
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
        self.handle_response(response)

    def register(self, username, password, email: str = ""):
        url = self.base_url + "/register"
        data = {"username": username, "password": password}
        response = requests.post(url, json=data, headers=self.headers)
        self.handle_response(response)

    def logout(self, aliasId: int, playerId: int, token: str):
        url = self.base_url + "/logout"
        headers = self.headers.copy()
        headers.update({"x-talo-alias": aliasId, "x-talo-player": playerId, "x-talo-session": token})
        response = requests.post(url, headers=headers)
        self.handle_response(response)

    def verify(self, aliasId: int, token: str):
        url = self.base_url + "/verify"
        body = {"aliasId": aliasId, "token": token}
        response = requests.post(url, headers=self.headers, json=body)
        self.handle_response(response)

    def changepassword(self, aliasId: int, playerId: int, token: str, currentPassword: str, newPassword: str):
        url = self.base_url + "/change_password"
        body = {"aliasId": aliasId, "token": token, "currentPassword": currentPassword, "newPassword": newPassword}
        headers = self.headers.copy()
        headers.update({"x-talo-alias": aliasId, "x-talo-player": playerId, "x-talo-session": token})
        response = requests.post(url, headers=headers, json=body)
        self.handle_response(response)

    def changeemail(self, aliasId: int, playerId: int, token: str, currentPassword: str, newEmail: str):
        url = self.base_url + "/change_email"
        body = {"aliasId": aliasId, "token": token, "currentPassword": currentPassword, "newEmail": newEmail}
        headers = self.headers.copy()
        headers.update({"x-talo-alias": aliasId, "x-talo-player": playerId, "x-talo-session": token})
        response = requests.post(url, headers=headers, json=body)
        self.handle_response(response)

    def resetpasswordrequest(self, email: str):
        url = self.base_url + "/forgot_password"
        body = {"email": email}
        response = requests.post(url, headers=self.headers, json=body)
        self.handle_response(response)

    def resetpassword(self, code: str, newPassword: str):
        url = self.base_url + "/reset_password"
        body = {"code": code, "password": newPassword}
        response = requests.post(url, headers=self.headers, json=body)
        self.handle_response(response)

    def toggle2fa(self, aliasId: int, playerId: int, session: str, password: str, email: str, enable: bool):
        url = self.base_url + "/toggle_verification"
        body = {"currentPassword": password, "email": email, "verificationEnabled": enable}
        headers = self.headers.copy()
        headers.update({"x-talo-alias": aliasId, "x-talo-player": playerId, "x-talo-session": session})
        response = requests.patch(url, headers=headers, json=body)
        self.handle_response(response)

    def delete(self, aliasId: int, playerId: int, session: str, password: str):
        url = self.base_url + "/delete"
        body = {"currentPassword": password}
        headers = self.headers.copy()
        headers.update({"x-talo-alias": aliasId, "x-talo-player": playerId, "x-talo-session": session})
        response = requests.delete(url, headers=headers, json=body)
        return self.handle_response(response)
