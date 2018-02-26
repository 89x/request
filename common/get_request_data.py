#-*- coding=utf-8 -*-

'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
from base.open_excel import OpenExcel
from common.open_json import *
from config import data_config
import logging
class RequestData:
    def __init__(self):
        self.open_excel=OpenExcel()
        self.opera_json = OpenJson()

    # 获取用例总行数
    def get_case_lines(self):
        return self.open_excel.get_sheet_lins()

    # 获取是否执行
    def get_is_run(self,row):
        flag=None
        col= int (data_config.get_run())
        run_model = self.open_excel.get_all_value(row,col)
        if run_model.upper() == 'Y':
            flag = True
        else:
            flag = False
        return flag

    #是否携带header

    def get_is_hander(self,row):
        col= int (data_config.get_hander())
        hander= self.open_excel.get_all_value(row,col)
        if hander.upper() == 'Y':
            return data_config.get_hander_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col= int(data_config.get_request_mode())
        request_method =self.open_excel.get_all_value(row,col)
        return request_method


    #获取url

    def get_request_url(self,row):
        col = int (data_config.get_url())
        url = self.open_excel.get_all_value(row,col)
        return url

    #获取请求参数

    def get_request_value(self,row):
        col = int(data_config.get_date())
        data = self.open_excel.get_all_value(row,col)
        if data=='':
            return None
        else:
            return data

    # 通过获取关键字拿到json数据
    def get_data_json(self,row):
        try:
            request_data=self.opera_json.get_data_value(self.get_request_value(row))
            return request_data
        except KeyError as e:
            pass


    #获取预期结果
    def get_expect_data(self,row):
        col= int (data_config.get_expect())
        expect = self.open_excel.get_all_value(row,col)
        if expect == '':
             return expect
        return expect

    #获取用例编号
    def  get_number_value(self,row):
        col = int(data_config.get_number())
        number= self.open_excel.get_all_value(row,col)
        return  number

    #获取实际结果
    def write_excel(self,row,value):
        col=int (data_config.get_result())
        self.open_excel.write_value(row,col,value)

    #获取依赖数据的key
    def get_dependent_key(self,row):
        col = int(data_config.get_data_depend())
        depent_key = self.open_excel.get_all_value(row,col)
        if depent_key == '':
            return None
        else:
            return depent_key

    #判断是否有数据依赖
    def is_depend(self,row):
        col = int(data_config.get_field_depend())
        depend_case_id = self.open_excel.get_all_value(row,col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_data(self,row):
        col = int(data_config.get_field_depend())
        data= self.open_excel.get_all_value(row,col)
        if data == "":
            return None
        else:
            return data
