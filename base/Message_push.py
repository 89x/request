#-*- coding=utf-8 -*-

'''*********************************************************************************************************************
@名称介绍:公众号推送
@功能说明:需要先关注二维码
@参数说明:网站http://sc.ftqq.com/3.version
@返回结果:
@调用示例:
*********************************************************************************************************************'''

import requests
import json


def  get_Message_push():

    data = 'sendkey=1685-a00c59de37a5523e47dd04c047cbcdb0&text=测试&desp=测试'

    re = requests.get('http://pushbear.ftqq.com/sub', params=data).json()
    print (re)
    if  re['code'] =='0':
        print ("消息推送成功")
    else:
        print ("消息推送失败")
