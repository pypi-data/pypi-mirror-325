from requests import Response

class BaseAPI:
    def handle_response(self, response:Response):
        if response.status_code == 200:
            return response.json()
        else:
            return {"Error": {"status_code": response.status_code, "text": response.text}}
