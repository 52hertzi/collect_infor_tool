# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/29 4:42 下午
@Author ： Shawn
@FileName ：subdomain.py
@IDE ：PyCharm

"""

from config.request import do_requests
from config.config import conf
import os

path = os.path.abspath(__file__)
os = os.path.split(path)[0]


def run_single(target):
    mode = conf()['mode']
    obj = 'status_code'
    re = []
    with open(os+'/subdomain_dict.txt','r') as f:
        for f1 in f.readlines():
            url = 'https://' + f1.replace('\n','') + '.' + target
            u = f1.replace('\n','') + '.' + target
            code = do_requests(url,mode,obj)
            print(url,'-----',code)
            if code == 200 or code == 403 or code == 302 or code == 301 or code == 500 or code == 503:
                re.append(u)
        return re

# run_single('baidu.com')

