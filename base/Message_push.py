#-*- coding=utf-8 -*-

'''*********************************************************************************************************************
@名称介绍:公众号推送
@功能说明:需要先关注二维码
@参数说明:网站http://sc.ftqq.com/3.version
@返回结果:
@调用示例:
*********************************************************************************************************************'''

import requests
import logging
from base.get_time_value import get_format_time

def  get_Message_push(pass_list,fail_list):
    passnum = int(len(pass_list))
    failnum = int(len(fail_list))
    countnum = passnum + failnum
    pass_result = "%.2f%%" % (passnum / countnum * 100)
    fail_result = "%.2f%%" % (failnum / countnum * 100)
    content = "此次一共运行接口个数为%s个，" \
              "\n通过个数为%s个，" \
              "\n失败个数为%s个，" \
              "\n通过率为%s，" \
              "\n失败率为%s，" \
              "\n详情请查看邮件！" \
              % (countnum, passnum, failnum, pass_result, fail_result)
    test = get_format_time("")+"测试报告"
    data = 'text=%s&desp=%s'%(test,content)
    re = requests.get('http://sc.ftqq.com/SCU17696T36793e999732a8b734d8016268bdfb4f5a2a4357f3dee.send'
                      , params=data).json()
    if re['errno']!=0:
        logging.error("发送失败，请更改发送参数")
    else:
        logging.debug("公众号推送成功")
if __name__ == '__main__':
    get_Message_push(range(1000),range(1))