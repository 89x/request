#-*- coding=utf-8 -*-


from base.open_excel import OpenExcel
from base.run_method import RunMethod
from common.get_request_data import RequestData
from jsonpath_rw import jsonpath,parse
import json
class DependtndData:
    def __init__(self,case_id):
        self.Open_excel = OpenExcel()
        self.case_id = case_id
        self.data =RequestData()

    '''通过case_number获取case_id 的数据'''
    def get_case_number_depend(self):
        rows_data = self.Open_excel.get_rows_data(self.case_id)
        return rows_data
        #执行依赖数据，获取结果
    def run_dependent(self):
        run_merhod  = RunMethod()
        row_num = self.Open_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_json(row_num)
        header = self.data.get_is_hander(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_merhod.run_main(method,url,request_data,header)
        return json.loads(res)

    # 根据以来的key获取执行依赖测试case的响应数据，然后返回
    def get_data_for_key(self,row):
        depent_data = self.data.get_dependent_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depent_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
