# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/1 2:39 下午
@Author ： Shawn
@FileName ：dir_brute.py
@IDE ：PyCharm

"""
from config.config import conf
from config.request import do_requests
import os

path = os.path.abspath(__file__)
os = os.path.split(path)[0]

def check_dir_brute(target):
    mode = conf()['mode']
    obj = 'status_code'
    res = []
    with open(os+'/dir_brute_dict.txt','r') as f:
        for f1 in f.readlines():
            url = target + f1.replace('\n','')
            status = do_requests(url,mode,obj)
            if status != 'Url Wrong':
                if status == 200 or status == 302 or status == 403:
                    res.append(url)
            else:
                res.append('error')
                break
    return res
