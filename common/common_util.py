#coding:utf-8

import json
import logging
class CommonUtil:
	def is_contain(self,str_one,str_two):
		'''
		判断一个字符串是否再另外一个字符串中
		str_one:查找的字符串
		str_two：被查找的字符串
		'''
		flag = None
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag
	def is_equal_dict(self,dict_one,dict_two):
		'''
		判断两个字典是否相等
		'''
		return dict_one ==dict_two
