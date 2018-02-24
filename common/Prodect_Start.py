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
import datetime
from common.logging_setting import logging_setting
import os
from common.dependent_data import DependtndData

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
       # sa = config.get_time_value.get_time_diff(start_time=start_time,stop_time=stop_time)
       # print(sa)

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
            depend_case = self.data.is_depend(i)
            if is_run == True:
                if depend_case != None:
                    self.depend_data = DependtndData()
                    #获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_data(i)
                    request_mode[depend_key]= depend_response_data
                res = self.run_method.run_main(request_mode,url,data,hander)

                if self.util.is_contain(expect,res):
                    self.data.write_excel(i,"pass")
                    logging.debug("test case (%s) True"% is_number)
                else:
                    self.data.write_excel(i,'fail')
                    logging.error("test case (%s) Flase"%is_number)