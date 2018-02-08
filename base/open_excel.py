#-*- coding=utf-8 -*-
'''*********************************************************************************************************************
@名称介绍:
@功能说明:获取地址获取excel，定义获取sheet，行，内容
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
import xlrd
import os
from xlutils.copy import copy
from base.open_scene import open_excel_scene


class OpenExcel():
    def __init__(self,file_name=None,sheet_id=None,open_scene=open_excel_scene()):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id
        else:
            self.open_scene = open_scene
            print(open_scene)
            self.file_name=os.path.abspath('..' + '/excel/testcase/%s' %self.open_scene)
            self.sheet_id=0
        self.data = self.get_data()
        #获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table
        #获取单元格行数
    def get_sheet_lins(self):
        table = self.data
        return table.nrows
        #获取某一个单元格的内容
    def get_all_value(self,row,col):
        return self.data.cell_value(row,col)
        #写入excel数据
    def write_value(self,row,col,value):
        read_excel = xlrd.open_workbook(self.file_name)
        write_excel=copy(read_excel)
        sheet_excel=write_excel.get_sheet(0)
        sheet_excel.write(row,col,value)
        write_excel.save(self.file_name)

        #根据对应的numberID找到行的内容
    def get_rows_data(self,case_id):
        pass
        #根据对应的numberid找到对应的行号
    def get_row_num(self,case_id):
        pass
        #根据行号，找到该行的内容
    def get_row_value(self,row):
        pass