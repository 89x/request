#coding:utf-8

import requests
import json
from common.open_json import OpenJson


class OpenHeader:
    def __init__(self,url,data):
        self.url =url
        self.data=data



    def get_cookie(self):
        reques = requests.post(self.url,self.data)
        cookie = reques.cookies
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OpenJson()
        op_json.write_data(cookie)


if __name__ == '__main__':
    url = "http://www.cmall.com/memberSite/sso/loginJson"
    data = {
         "loginAccount": "18697980508",
          "password": "xiehengda",
          "rememberMe": "0"

    }

    res = json.dumps(requests.post(url, data).json())
    op_header = OpenHeader(url,data)
    op_header.write_cookie()