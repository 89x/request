# -*- coding=utf-8 -*-

'''
Created on 2016年6月1日
@author: Administrator
'''
import os
import logging
import logging.config
import configparser
from base import get_time_value
'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def read_config(file_path, field, key):
    if os.path.exists(r"{path}".format(path=file_path)):
        conf = configparser.ConfigParser()
        conf.read(file_path)
        get_key_value = conf.get(field, key)
    else:
        get_key_value = ""
        logging.error('{path}配置文件不存在!'.format(path=file_path))
    return get_key_value


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def write_config(file_path, field, key, value=""):
    if os.path.exists(r"{path}".format(path=file_path)):
        conf = configparser.ConfigParser()
        conf.read(file_path)
        conf.set(field, key, value)
        conf.write(open(file_path, 'w'))
    else:
        logging.error('{path}配置文件不存在!'.format(path=file_path))


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_data_folder_path():
    data_path = os.path.abspath("..") + "/DataFile"
    if not os.path.exists(data_path):
        try:
            os.makedirs(data_path)
        except Exception as e:
            data_path = ""
            logging.info("创建{path}文件夹失败!".format(path=data_path) + str(e))
    return data_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_report_folder_path():
    report_path = os.path.abspath("..") + "/Report"
    if not os.path.exists(report_path):
        try:
            os.makedirs(report_path)
        except Exception as e:
            report_path = ""
            logging.info("创建{path}文件夹失败!".format(path=report_path) + str(e))
    return report_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_logs_folder_path():
    logs_path = os.path.abspath("..") + "/Logs"
    if not os.path.exists(logs_path):
        try:
            os.makedirs(logs_path)
        except Exception as e:
            logs_path = ""
            logging.info("创建{path}文件夹失败!".format(path=logs_path) + str(e))
    return logs_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_temp_folder_path():
    temp_path = os.path.abspath("..") + "/Temp"
    if not os.path.exists(temp_path):
        try:
            os.makedirs(temp_path)
        except Exception as e:
            temp_path = ""
            logging.info("创建{path}文件夹失败!".format(path=temp_path) + str(e))
    return temp_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_scenario_folder_path():
    scenario_path = os.path.abspath("..") + "/Scenario"
    if not os.path.exists(scenario_path):
        try:
            os.makedirs(scenario_path)
        except Exception as e:
            scenario_path = ""
            logging.info("创建{path}文件夹失败!".format(path=scenario_path) + str(e))
    return scenario_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_csv_folder_path():
    csv_data_path = os.path.abspath("..") + "/File/CSV"
    if not os.path.exists(csv_data_path):
        try:
            os.makedirs(csv_data_path)
        except Exception as e:
            csv_data_path = ""
            logging.info("创建{path}文件夹失败!".format(path=csv_data_path) + str(e))
    return csv_data_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_txt_folder_path():
    txt_data_path = os.path.abspath("..") + "/File/TXT"
    if not os.path.exists(txt_data_path):
        try:
            os.makedirs(txt_data_path)
        except Exception as e:
            txt_data_path = ""
            logging.info("创建{path}文件夹失败!".format(path=txt_data_path) + str(e))
    return txt_data_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_excel_folder_path():
    excel_data_path = os.path.abspath("..") + "/File/EXCEL"
    if not os.path.exists(excel_data_path):
        try:
            os.makedirs(excel_data_path)
        except Exception as e:
            excel_data_path = ""
            logging.info("创建{path}文件夹失败!".format(path=excel_data_path) + str(e))
    return excel_data_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_other_file_path():
    other_path = os.path.abspath("..") + "/Others"
    if not os.path.exists(other_path):
        try:
            os.makedirs(other_path)
        except Exception as e:
            other_path = ""
            logging.info("创建{path}文件夹失败!".format(path=other_path) + str(e))
    return other_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_other_temp_path():
    other_temp_path = get_temp_folder_path() + "/Others"
    if not os.path.exists(other_temp_path):
        try:
            os.makedirs(other_temp_path)
        except Exception as e:
            other_temp_path = ""
            logging.info("创建{path}文件夹失败!".format(path=other_temp_path) + str(e))
    return other_temp_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_report_zip_path():
    report_format = get_time_value.get_format_time("")
    report_zip_path = get_report_folder_path() + "/Reports({value}).zip".format(value=report_format)
    return report_zip_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_html_report_path():
    report_format = get_time_value.get_format_time("")
    report_path = get_temp_folder_path() + "/Reports({value}).html".format(value=report_format)
    return report_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_log_report_path():
    log_format = get_time_value.get_format_time("")
    log_report_path = get_temp_folder_path() + "/RunLog({value}).html".format(value=log_format)
    return log_report_path


'''*********************************************************************************************************************
@名称介绍:
@功能说明:
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''


def get_run_logs_path():
    logs_format = get_time_value.get_format_time("yyyy-mm-dd")
    run_logs_path = get_logs_folder_path() + "/Logs.{value}.log".format(value=logs_format)
    return run_logs_path