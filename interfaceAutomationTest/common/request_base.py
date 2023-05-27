import requests


class BaseRequest:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }

    # def request(self, method, url, params=None, json=None):
    #     if method.lower() == "get":
    #         resp=requests.request(method, url, params=params, header=self.header)
    #     elif method.lower == "post":
    #         requests.request(method, url, json=json, header=self.header)
