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

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = os.path.abspath('..'+'/json/json')
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #获取json数据
    def read_data(self):
        with  open(self.file_path) as sa :
            data = json.load(sa)
            return data

        file = open('test.json', 'r')
        for line in file.readlines():
            dic = json.loads(line)


    #根据字典key获取value
    def get_data_value(self,id):
        return self.data[id]


    # 写json
    def write_data(self, data):
        with open(os.path.abspath('..'+'/json/cookies.json'), 'w') as fp:
            fp.write(json.dumps(data))


    #获取cookies
    def get_cookie(self):
        return self.data

