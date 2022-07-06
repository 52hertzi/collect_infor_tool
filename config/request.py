# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/9 10:42 上午
@Author ： Shawn
@FileName ：requests.py
@IDE ：PyCharm

"""

import requests
import socket
import json
from fake_useragent import UserAgent
from .config import conf
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.adapters import HTTPAdapter
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def header():
    headers = {
        'User-Agent': UserAgent().random
    }
    return headers
# 0：http 1:socks 2:None
def exist():
    config = conf()
    if config['mode'] == 0:
        conf_proxy = config['http_proxy']  ## 获取代理
        conf_port = config['http_port']
        return 0,conf_proxy,conf_port
    elif config['mode'] == 1:
        conf_socks = config['socks_proxy']
        conf_socks_port = config['socks_port']
        return 1,conf_socks,conf_socks_port
    elif config['mode'] == 2:
        return 2,0,0
## 获取外部json数据不使用代理，设计缺陷。。。。
def only_use_requests(url,obj):
    headers = header()
    r = requests.Session()
    r.mount('http://', HTTPAdapter(max_retries=1))
    r.mount('https://', HTTPAdapter(max_retries=1))
    dic_method = ['headers', 'text', 'status_code', 'content']
    res = r.get(url,headers=headers,verify=False,timeout=10)
    for i in range(0, len(list(dic_method))):
        if dic_method[0] == obj:
            return res.headers
        elif dic_method[1] == obj:
            return res.text
        elif dic_method[2] == obj:
            return res.status_code
        elif dic_method[3] == obj:
            return res.content

# 0':'http_proxy','1':'socks_proxy','2':'http_proxy'
def do_requests(url,mode,obj):
    dic_method = ['headers','text','status_code','content']
    if mode == 0 or mode == 2:
        res = request_proxy(url)
    else:
        res = request_socks(url)
    if res != 0:
        for i in range(0, len(list(dic_method))):
            if dic_method[0] == obj:
                return res.headers
            elif dic_method[1] == obj:
                return res.text
            elif dic_method[2] == obj:
                return res.status_code
            elif dic_method[3] == obj:
                return res.content
    else:
        return 'Url Wrong'


def request_proxy(url):
    headers = header()
    try:
        if exist()[0] == 0:
            proxies = {
                "http": "http://"+exist()[1] + ":" + exist()[2],
                "https": "http://"+exist()[1] + ":" + exist()[2]
            }

            r = requests.get(url, proxies=proxies, headers=headers, verify=False,timeout=5)
            return r
        else:
            r = requests.get(url, headers=headers, verify=False,timeout=5)
            return r
    except Exception:
        return 0


def request_socks(url):
    headers = header()
    try:
        if exist()[0] == 1:
            proxies = {
                'http': 'socks5h://' + exist()[1] + ":" + exist()[2],
                'https': 'socks5h://' + exist()[1] + ":" + exist()[2]
            }
            r = requests.get(url, proxies=proxies, headers=headers, verify=False, timeout=5)
            return r
        else:
            r = requests.get(url, headers=headers, verify=False, timeout=5)
            return r
    except Exception:
        return 0



def gip(url):
    headers = header()
    try:
        if exist()[0] == 2:
            r = requests.get(url, headers=headers, verify=False,timeout=5)
        elif exist()[0] == 0:
            proxies = {
                'http': "http://"+exist()[1] + ":" + exist()[2],
                'https': "http://"+exist()[1] + ":" + exist()[2]
            }

            r = requests.get(url, proxies=proxies, headers=headers, verify=False,timeout=5)
        else:
            proxies = {
                'http': 'socks5h://' + exist()[1] + ":" + exist()[2],
                'https': 'socks5h://' + exist()[1] + ":" + exist()[2]
            }
            r = requests.get(url, proxies=proxies, headers=headers, verify=False)
        return r.text
    except Exception:
        return 0

## 获取局域网iP
def get_Lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        Lan_ip = s.getsockname()[0]
        s.close()
    except Exception:
        Lan_ip = '当前无网络'
    return Lan_ip

## 获取公网出口iP
def get_ip():
    _ip = ''
    addr = ''
    url = 'https://api.ip138.com/ip/?ip=&datatype=jsonp&token=728325dd48f6db488090f7d3d52295fa'
    try:
        res = json.loads(gip(url))
        if res['ret'] == 'ok':
            _ip = res['ip']
            if len(res['data'][0]) != 0:
                addr_country = res['data'][0]
                addr = addr + addr_country
            if len(res['data'][1]) != 0:
                addr_province = res['data'][1]
                addr = addr + ',' + addr_province
            if len(res['data'][2]) != 0:
                addr_city = res['data'][2]
                addr = addr + ',' + addr_city
            if len(res['data'][3]) != 0:
                addr_town = res['data'][3]
                addr = addr + ',' + addr_town
            if len(res['data'][4]) != 0:
                msg_com = res['data'][4]
                addr = addr + ',' + msg_com
            return _ip + ' ' + addr
        else:
            _ip = '接口发生错误！'
            return _ip
    except Exception:
        _ip = '请检查网络！'
        return _ip


