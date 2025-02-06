import httpx
import requests

BASE_URL = "https://zeus.ionis-it.com/api"
DEFAULT_HEADERS = {"accept": "text/plain", "Content-Type": "application/json"}


class ZeusCore:
    def __init__(self):
        self.appId = None
        self.apiKey = None
        self.__version__ = "1.1.1"

    def handle_errors(self, status_code: int, protect: bool = False):
        if status_code == 400:
            raise Exception("Error 400 : Bad request")
        elif status_code == 403:
            raise Exception("Error 403 : Access to API is forbidden")
        elif status_code == 500:
            raise Exception("Error 500 : Internal server error")
        elif status_code != 200:
            raise Exception(f"Unknown error: {status_code}")

    def __login__(self, appId: str) -> None:
        url = f"{BASE_URL}/Application/Login"
        data = {"appId": appId}
        response = requests.post(url, headers=DEFAULT_HEADERS, json=data)
        if response.status_code == 200:
            self.apiKey = response.text
            self.appId = appId
        else:
            self.handle_errors(response.status_code)

    def version(self) -> str:
        return self.__version__

    def login(self, appId: str) -> None:
        self.__login__(appId)

    async def fetch_data(self, url: str, protect: bool = False) -> dict:
        headers = {**DEFAULT_HEADERS, "Authorization": f"Bearer {self.apiKey}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            if response.status_code == 403 and not protect:
                self.login(self.appId)
                return await self.fetch_data(url, True)
            self.handle_errors(response.status_code, protect)
            return response.json()
