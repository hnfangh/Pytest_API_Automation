# -*- coding: utf-8 -*-


"""
定义所有测试数据

"""
import os
from Params import tools
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Basic:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Basic.yaml')
    params = get_parameter('Basic')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Collections:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Collections.yaml')
    params = get_parameter('Collections')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Personal:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Personal.yaml')
    params = get_parameter('Personal')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Login:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Login.yaml')
    params = get_parameter('Login')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
