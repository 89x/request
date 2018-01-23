#coding:utf-8

'''*********************************************************************************************************************
@名称介绍:取json文件数据
@功能说明:根据excel关键字取json文件数据
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
import json
import os
import logging

class OpenJson:
    def __init__(self):
        self.data = self.read_data()
    #获取json数据
    def read_data(self):
        with  open(os.path.abspath('..'+'/json/json')) as sa :
            data = json.load(sa)
            return data


    #根据字典key获取value
    def get_data_value(self,id):
        return self.data[id]



