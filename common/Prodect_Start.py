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

class RunMain:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=RequestData()
        self.util=CommonUtil()
    #程序执行主入口
    def get_go_run(self):
        #日志打印配置
        logs_path =config.get_run_logs_path()
        if os.path.exists(r"{path}".format(path=logs_path)):
            os.remove(r"{path}".format(path=logs_path))
        logging_setting(logs_path)
        #测试启止时间
        sa = config.get_time_value

        #用例主体方法
        res = None
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            request_mode=self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            is_number=self.data.get_number_value(i)
            data = self.data.get_data_json(i)
            expect=self.data.get_expect_data(i)
            hander = self.data.get_is_hander(i)
            if is_run == True:
                res = self.run_method.run_main(request_mode,url,data,hander)
                if self.util.is_contain(expect,res):
                    self.data.write_excel(i,"pass")
                    logging.debug("test case (%s) True"%is_number)
                else:
                    self.data.write_excel(i,'fail')
                    logging.error("test case (%s) Flase"%is_number)