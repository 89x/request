# -*- coding=utf-8 -*-
'''*********************************************************************************************************************
@名称介绍:配置日志打印级别
@功能说明:目前调用文件名称filename，后期改成方法名称funcName
@参数说明:
@返回结果:
@调用示例:
*********************************************************************************************************************'''
from config.config import *

def logging_setting(file_path, file_mode="w"):
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] - [%(levelname)s] - [%(funcName)s] - [%(lineno)d]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=file_path,
        filemode=file_mode
    );

    console = logging.StreamHandler();
    console.setLevel(logging.DEBUG);
    formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - [%(funcName)s] - [%(lineno)d]: %(message)s');
    console.setFormatter(formatter);
    logging.getLogger('').addHandler(console);