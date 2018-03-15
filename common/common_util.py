#coding:utf-8

import json
import logging
class CommonUtil:
	def is_contain(self,str_one,str_two):
		flag = None
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag
	def is_equal_dict(self,dict_one,dict_two):
		return dict_one == dict_two
