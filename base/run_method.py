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
import pymysql

class RunMethod:
    def post_main(self,url,data,hander=None):
        res=None
        if hander!=None:
            res=requests.post(url=url,data=data,hesder=hander).json()
        else:
            res=requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data=None,hander=None):
        res=None
        if hander!=None:
            res=requests.get(url=url,data=data,headers=hander).json()
        else:
            res=requests.get(url=url,data=data).json()
        return res
    #缺少data为j空判断


    def run_main(self,request_mode,url,data=None,hander=None):
        flag=None
        if request_mode == 'post':
            flag= self.post_main(url,data,hander)
        else:
            flag= self.get_main(url,data,hander)
        return json.dumps(flag,ensure_ascii=False,sort_keys=True,indent=2)
