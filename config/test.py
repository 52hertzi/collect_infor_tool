# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/21 16:09
@Author ： Shawn
@FileName ：test.py
@IDE ：PyCharm

"""

import requests

proxy = {
        "http": "socks5h://127.0.0.1:7890",
        "https": "socks5h://127.0.0.1:7890"
        }

ip_url = "http://api.getmyip.me/json"
print(proxy)
resp = requests.get(ip_url,proxies=proxy,verify=False)
print(resp.content)
