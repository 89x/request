#-*- coding=utf-8 -*-

'''*********************************************************************************************************************
@名称介绍:
@功能说明:主方法，调用即可运行程序
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
from base.run_method import RunMethod
from common.get_request_data import RequestData
from common.common_util import CommonUtil
from config import config
import logging
from common.logging_setting import logging_setting
import os
from common.dependent_data import DependtndData
from common.send_email import SendMail
from base.Message_push import get_Message_push
from base.open_header import OpenHeader
from common.open_json import OpenJson
class RunMain:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=RequestData()
        self.util=CommonUtil()
        self.send_email=SendMail()
    #程序执行主入口
    def get_go_run(self):
        #日志打印配置
        logs_path =config.get_run_logs_path()
        if os.path.exists(r"{path}".format(path=logs_path)):
            os.remove(r"{path}".format(path=logs_path))
        logging_setting(logs_path)
        #用例主体方法
        res = None
        pass_count= []
        fail_count= []
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            request_mode=self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            is_number=self.data.get_number_value(i)
            data = self.data.get_data_json(i)
            expect=self.data.get_expect_data(i)
            hander = self.data.get_is_hander(i)
            depend_case = self.data.is_depend(i)
            if is_run ==True:
                if depend_case != None:
                    self.depend_data = DependtndData()
                    #获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_data(i)
                    request_mode[depend_key]= depend_response_data
                if hander =="W":
                    res=self.run_method.run_main(request_mode,url,data)
                    op_hander=OpenHeader(url,data)
                    op_hander.write_cookie()
                elif  hander == "Y":
                    op_json = OpenJson(os.path.abspath('..'+'/json/cookies.json'))
                    cookie = op_json.get_cookie()
                    res = self.run_method.run_main(request_mode,url,data,cookie)
                else:
                    res = self.run_method.run_main(request_mode, url, data)
                if  self.util.is_contain(expect,res):
                    self.data.write_excel(i,"pass")
                    pass_count.append(i)
                    logging.debug("test case (%s) True"% is_number)
                    logging.debug("pass_count:%s True"% len(pass_count))
                else:
                    self.data.write_excel(i,res)
                    fail_count.append(i)
                    logging.error("test case (%s) Flase"%is_number)
                    logging.debug("fail_count:%s True"% len(fail_count))
        logging.debug("发送邮件中")
        self.send_email.send_main(pass_count,fail_count)
        get_Message_push(pass_count,fail_count)
        logging.debug("发送邮件成功")
