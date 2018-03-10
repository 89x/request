#coding:utf-8


'''*********************************************************************************************************************
@名称介绍:获取场景文件
@功能说明:根据场景文件取case文件
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


import os
import xlrd
import logging

def open_excel_scene():
    data=xlrd.open_workbook(os.path.abspath('..'+'/excel/scene/Scenario.xls'))
    table=data.sheets()[0]
    cnow = table.nrows
    for x in range(2,cnow):
        scenen_run =table.cell_value(x,0)
        if scenen_run == "N":
            continue
        else:
            scenen_case = table.cell_value(x, 2)
        return scenen_case