import os
import sys

import requests
sys.path.append(os.path.dirname(sys.path[0]))
from interfaceAutomationTest.common.request_base import BaseRequest


class Login(BaseRequest):


    def login(self, method, baseurl, data):

        resp=requests.request(method, url=baseurl,params=data)
        return resp
    def register(self, method, url, data):
        resp=requests.request(method, url=url, json=data)
        return resp

    def test_dome(self,method, url, data):
        resp = requests.request(method, url=url, params=data)
        return resp