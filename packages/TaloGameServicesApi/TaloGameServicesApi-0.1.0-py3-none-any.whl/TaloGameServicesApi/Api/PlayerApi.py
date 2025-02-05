import requests
from requests.models import Response
from .BaseApi import BaseAPI
from ..Types.Prop import Prop
from .. import TaloGameServicesApi as TGS


class Player(BaseAPI):
    def __init__(
        self,
        api_key: str,
        api: TGS,
        api_url: str = "https://api.trytalo.com",
        dev: bool = False,
    ):
        self.api_key = api_key
        self.base_url = api_url + "/v1/players"
        self.headers = {"Authorization": f"Bearer {self.api_key}","X-Talo-Dev-Build": dev}

    def Identify(self, player_id: str, player_service: str = "username"):
        url = f"{self.base_url}/identify"
        data = {"identifier": player_id, "service": player_service}
        response: Response = requests.get(url, headers=self.headers, params=data)
        return self.handle_response(response)

    def Merge(self, player1_id: str, player2_id: str):
        url = f"{self.base_url}/merge"
        data = {"playerId1": player1_id, "playerId2": player2_id}
        response: Response = requests.post(url, headers=self.headers, json=data)
        return self.handle_response(response)

    def UpdateProps(self, player_id: str, props: tuple[Prop]):
        url = f"{self.base_url}/{player_id}"
        response: Response = requests.put(url, headers=self.headers, json=props)
        return self.handle_response(response)

    def getPlayer(self, player_id: str):
        url = f"{self.base_url}/{player_id}"
        response: Response = requests.get(url, headers=self.headers)
        return self.handle_response(response)
