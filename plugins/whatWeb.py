# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/21 2:05 下午
@Author ： Shawn
@FileName ：whatWeb.py
@IDE ：PyCharm

"""

from config.request import do_requests
from config.config import conf
import json
import hashlib
import os


path = os.path.abspath(__file__)
os = os.path.split(path)[0]
def input_url(url):
    fp = open(os+"/whatWeb_data.json")
    whatweb = json.load(fp)
    status = check_status(url,whatweb)
    if status[0] == 200:
        if len(whatweb[status[1]]['md5']) != 0:
            check = check_md5(url,whatweb[status[1]]['md5'])
            if check == 1:
                return 1,whatweb[status[1]]['name']
        else:
            return 2,whatweb[status[1]]['name']
    else:
        return 0,'None'
def check_status(url,data):
    mode = conf()['mode']
    obj = 'status_code'
    for i in range(len(data)):
        url_ = url + data[i]['url']
        status_code = do_requests(url_,mode,obj)
        if status_code == 200:
            return status_code,i
        elif i == len(data) and status_code != 200:
            return 0,0


def check_md5(url,data):
    mode = conf()['mode']
    obj = 'content'
    content = do_requests(url,mode,obj)
    m2 = hashlib.md5()
    md5 = m2.update(content.encode("utf8"))
    # 1 确认   0不确认
    if data == md5:
        return 1
    else:
        return 0

