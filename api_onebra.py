import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

URL_BASE = "https://www.onebra.com"
URL_API = "https://api.onebra.com"
VERSION_API = "0.0.1-professional"

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504, 104],
    allowed_methods=frozenset(["HEAD", "POST", "PUT", "GET", "OPTIONS"])
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Browser(object):

    def __init__(self):
        self.response = None
        self.headers = None
        self.session = requests.Session()

    def set_headers(self, headers=None):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) "
                          "Chrome/87.0.4280.88 Safari/537.36"
        }
        if headers:
            for key, value in headers.items():
                self.headers[key] = value

    def get_headers(self):
        return self.headers

    def send_request(self, method, url, **kwargs):
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        return self.session.request(method, url, **kwargs)


class OnebraAPI(Browser):

    def __init__(self, username=None, password=None, token=None):
        super().__init__()
        self.proxies = None
        self.token = token if token else "None"
        self.uid = None
        self.username = username
        self.password = password
        self.set_headers()
        self.headers = self.get_headers()

    def auth(self):
        if self.token != "None":
            return {"msg": "Token já fornecido manualmente."}
        
        data = {
            "account": self.username,
            "password": self.password,
            "area": 55,
            "login_type": 2,
            "mainVer": 1,
            "subVer": 1,
            "pkgName": "h5_client",
            "deviceid": "PC_473dc4eb-ba36-4924-a8c3-ccdae1e67227",
            "Type": 101,
            "os": "Linux",
            "ioswebclip": 0,
            "isShell": 0,
            "language": "pt-pt"
        }
        self.headers["referer"] = f"{URL_BASE}/"
        self.response = self.send_request("PUT",
                                          f"{URL_API}/login/login",
                                          json=data,
                                          headers=self.headers)

        if not self.response.json().get("error"):
            self.token = self.response.json()["data"]["token"]
            self.uid = self.response.json()["data"]["uid"]

        return self.response.json()

    async def reconnect(self):
        return await self.auth()

    def get_last_doubles(self):
        data = {
            "limit": 12,
            "token": self.token,
            "type": 3,
            "language": "pt-pt",
        }
        self.response = self.send_request("POST",
                                          f"{URL_API}/goldGame/double_history",
                                          proxies=self.proxies,
                                          json=data,
                                          headers=self.headers)
        if self.response:
            try:
                response_data = self.response.json()
                if response_data["code"] == 0 and "data" in response_data:
                    result = {
                        "items": [
                            {"color": "⚪️" if int(i) == 15 else "🔴" if int(i) < 8 else "⚫️",
                             "value": i} for i in response_data["data"]]
                    }
                    return result
            except Exception as e:
                print(f"Erro ao processar a resposta: {e}")
                return False

        return False

    def get_last_crashs(self):
        data = {
            "type": 2,
            "uid": self.uid,
            "language": "pt-pt",
        }
        self.response = self.send_request("POST",
                                          f"{URL_API}/Goldgame/bd_history",
                                          proxies=self.proxies,
                                          json=data,
                                          headers=self.headers)
        if self.response:
            result = {
                "items": [{"color": "⬛️" if float(i["sys_odds"]) < 2 else "🟩", "value": i["sys_odds"]
                           } for i in self.response.json()["data"]]}
            return result

        return False

if __name__ == "__main__":
    token = "SEU_TOKEN_ONEBRA_AQUI"
    email = "SEU_EMAIL_ONEBRA_AQUI"
    password = "SUA_SENHA_ONEBRA_AQUI"
    api = OnebraAPI(email, password, token)
    authentication = api.auth()
    last_doubles = api.get_last_doubles()
    print("Últimos doubles:", last_doubles)
    last_crashs = api.get_last_crashs()
    print("Últimos crashes:", last_crashs) 