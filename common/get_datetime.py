#coding:utf-8

import requests
import math


class GetDatetime:
    def __init__(self,url,data):
        self.url =url
        self.data=data



    def get_time(self):
        time = requests.post(self.url,self.data)
        times = time.elapsed.microseconds/1000
        return (str(math.floor(times)))+'ms'



if __name__ == '__main__':
    url = "http://www.cmall.com/memberSite/sso/loginJson"

    data = {"loginAccount": "15921859601", "password": "111111", "rememberMe": "0"}

    res = GetDatetime(url,data)
    print(res.get_time())

