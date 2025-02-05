from .version import VERSION, VERSION_SHORT
from .Api.PlayerApi import Player


class TaloGameServicesApi:
    def __init__(self, api_key: str, api_url: str = "https://api.trytalo.com", dev: bool = False):
        self.api_key = api_key
        self.base_url = api_url
        self.dev = dev
        self.headers = {"Authorization": f"Bearer {self.api_key}", "X-Talo-Dev-Build": dev}
        self.players = Player(self.api_key, self, self.base_url, dev=self.dev)
        



