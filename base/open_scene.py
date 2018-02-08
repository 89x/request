#coding:utf-8
import os
import xlrd

def open_excel_scene():
    data=xlrd.open_workbook(os.path.abspath('..'+'/excel/Scenario.xls'))
#print(data.sheet_names())
    table=data.sheets()[0]
    cnow = table.nrows
    for x in range(cnow):
        if x<2:
            pass
        else:
            scenen_run =table.cell_value(x,0)
            print("是否执行:",scenen_run)
            if scenen_run =="Y":
                scenen_case = table.cell_value(x,2)
                print(scenen_case)
            else:
                pass
    case_data = xlrd.open_workbook(os.path.abspath('..' + '/excel/testcase/%s'%scenen_case))
    print(case_data)
open_excel_scene()
