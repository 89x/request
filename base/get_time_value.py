#-*- coding=utf-8 -*-

'''*********************************************************************************************************************
@名称介绍:格式化时间
@功能说明:应用于创建时间
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
import time
import datetime

def get_format_time(flag):
    try:
        if flag.upper() == "YYYY-MM-DD HH:MM:SS":
            times = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        elif flag.upper() == "YYYY-MM-DD":
            times = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        elif flag.upper() == "HH:MM:SS":
            times = time.strftime('%H:%M:%S',time.localtime(time.time()))
        elif flag.upper() == "YYYYMMDD":
            times = time.strftime('%Y%m%d',time.localtime(time.time()))
        elif flag.upper() == "YYYY/MM/DD":
            times = time.strftime('%Y/%m/%d',time.localtime(time.time()))
        elif flag.upper() == "YYYY/MM/DD HH:MM:SS":
            times = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
        else:
            times = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
    except:
        times = ""
    return times

'''*********************************************************************************************************************
@名称介绍:格式化时间
@功能说明:应用于测试报告
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
def get_time_diff(start_time,stop_time):
    try:
        start_time = time.strptime(start_time,"%Y-%m-%d %H:%M:%S")
        stop_time = time.strptime(stop_time,"%Y-%m-%d %H:%M:%S")
        start_time = datetime.datetime(start_time[0],
                                       start_time[1],
                                       start_time[2],
                                       start_time[3],
                                       start_time[4],
                                       start_time[5]
                                       )
        stop_time = datetime.datetime(stop_time[0],
                                      stop_time[1],
                                      stop_time[2],
                                      stop_time[3],
                                      stop_time[4],
                                      stop_time[5]
                                      )
        return stop_time-start_time
    except:
        return ""
