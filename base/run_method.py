#-*- coding=utf-8 -*-
'''*********************************************************************************************************************
@名称介绍:
@功能说明:requests封装成一个执行方法  run_main 调用get以及post
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
import requests
import logging
import json

class RunMethod:
    def post_main(self,url,data=None,hander=None):
        res=None
        if hander!=None:
            res=requests.post(url=url,data=data,headers=hander)
        else:
            res=requests.post(url=url,data=data)
        return res.json()


    def get_main(self,url,data=None,hander=None):
        res=None
        try:
            if hander!=None:
                res=requests.get(url=url,params=data,headers=hander)
            else:
                res=requests.get(url=url,params=data)
            return res.json()
        except:
            logging.error("dfghjk")
    def json_main(self,url,data=None,hander=None):
        res = None
        if hander !=None:
            res =requests.post(url=url,json=data,headers=hander)
        else:
            try:
                res=requests.post(url=url,json=data)
            except:
                logging.error("url is None")
        return res.json()





    def run_main(self,request_mode,url,data=None,hander=None):
        flag=None
        if request_mode == 'post':
            flag= self.post_main(url,data,hander)
        elif request_mode =="get":
            flag= self.get_main(url,data,hander)
        else:
            flag= self.json_main(url,data,hander)
        return json.dumps(flag, ensure_ascii=False)

        #return json.dumps(flag,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    re = RunMethod()
    #re.run_main(request_mode="get",url="http://www.cmall.com/memberSite/sso/loginJson",data="loginAccount=苏小谢&password=xiehengda")
    #sa=requests.get(url="http://www.cmall.com/memberSite/sso/loginJson",params="loginAccount=18697980508&password=xiehengda")
    #print(sa.headers)