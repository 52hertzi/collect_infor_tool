# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/9 10:27 上午
@Author ： Shawn
@FileName ：config.py
@IDE ：PyCharm

"""

import configparser
import os
import re

path = os.path.abspath(__file__)
os = os.path.split(path)[0]
def conf():
    conf = configparser.ConfigParser()
    conf.read(os+"/conf.ini")
    Fofa_email = conf.get("FOFA","email")  # 获取fofa email
    Fofa_key = conf.get("FOFA","key")  # 获取fofa key值
    try:
        conf.get("Proxy","http_proxy")
        http_proxy = conf.get("Proxy","http_proxy") #获取http代理地址
        http_port = conf.get("Proxy","http_port")
        return {'mode':0,'fofa_email':Fofa_email,'fofa_key':Fofa_key,'http_proxy':http_proxy,'http_port':http_port}
    except:
        try:
            conf.get("Proxy","socks_proxy")
            socks_proxy = conf.get("Proxy","socks_proxy")   #获取socks代理地址
            socks_port = conf.get("Proxy","socks_port")
            return {'mode':1,'fofa_email':Fofa_email,'fofa_key':Fofa_key,'socks_proxy':socks_proxy,'socks_port':socks_port}
        except:
            return {'mode':2,'fofa_email':Fofa_email,'fofa_key':Fofa_key}

def conf_write_proxy(data):
    conf = configparser.ConfigParser()
    conf.read(os+"/conf.ini",encoding="utf-8")
    if data['mode'] == '0':
        if len(data['ip']) != 0:
            if len(data['port']) != 0:
                if int(data['port']) in range(1, 65002):
                    conf.remove_option("Proxy", "socks_proxy")
                    conf.remove_option("Proxy", "socks_port")
                    conf.set("Proxy", "http_proxy", data['ip'])
                    conf.set("Proxy", "http_port", data['port'])
                    with open(os+"/conf.ini", "w", encoding="utf-8") as f:
                        conf.write(f)
                else:
                    return "端口不合法 ！"
            else:
                return "端口为空 ！"
        else:
            return "代理地址为空 ！"

    elif data['mode'] == '1':
        if len(data['ip']) != 0:
            if len(data['port']) != 0:
                if int(data['port']) in range(1,65002):
                    regx = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
                    rst = regx.match(data['ip'])
                    if rst is None:
                        return "ip地址格式不正确 ！"
                    else:
                        conf.remove_option("Proxy", "http_proxy")
                        conf.remove_option("Proxy", "http_port")
                        conf.set("Proxy", "socks_proxy", data['ip'])
                        conf.set("Proxy", "socks_port", data['port'])
                    with open(os+"/conf.ini", "w", encoding="utf-8") as f:
                        conf.write(f)
                else:
                    return "端口不合法 ！"
            else:
                return "端口为空 ！"
        else:
            return "代理地址为空 ！"
    else:
        try:
            conf.remove_option("Proxy", "http_proxy")
            conf.remove_option("Proxy", "http_port")
            conf.remove_option("Proxy", "socks_proxy")
            conf.remove_option("Proxy", "socks_port")
            with open(os + "/conf.ini", "w", encoding="utf-8") as f:
                conf.write(f)
            return "已删除代理 ！"
        except Exception:
            conf.remove_option("Proxy", "socks_proxy")
            conf.remove_option("Proxy", "socks_port")
            conf.remove_option("Proxy", "http_proxy")
            conf.remove_option("Proxy", "http_port")
            with open(os + "/conf.ini", "w", encoding="utf-8") as f:
                conf.write(f)
            return "已删除代理 ！"

    if len(data['email']) != 0:
        if len(data['key']) != 0:
            conf.remove_option("FOFA", "key")
            conf.remove_option("FOFA", "email")
            conf.set("FOFA", "key", data['key'])
            conf.set("FOFA", "email", data['email'])
            with open(os + "/conf.ini", "w", encoding="utf-8") as f:
                conf.write(f)
        else:
            return "Fofa密钥为空 ！"
    else:
        return "Email密钥为空 ！"

    if len(data['email']) == 0:
        if len(data['key']) == 0:
            conf.remove_option("FOFA", "key")
            conf.remove_option("FOFA", "email")
            conf.set("FOFA", "key", data['key'])
            conf.set("FOFA", "email", data['email'])
            with open(os + "/conf.ini", "w", encoding="utf-8") as f:
                conf.write(f)
        else:
            conf.remove_option("FOFA", "key")
            conf.remove_option("FOFA", "email")
            conf.set("FOFA", "key", data['key'])
            conf.set("FOFA", "email", data['email'])
            with open(os + "/conf.ini", "w", encoding="utf-8") as f:
                conf.write(f)
    elif len(data['key']) == 0:
        if len(data['email']) != 0:
            conf.remove_option("FOFA", "key")
            conf.remove_option("FOFA", "email")
            conf.set("FOFA", "key", data['key'])
            conf.set("FOFA", "email", data['email'])
            with open(os + "/conf.ini", "w", encoding="utf-8") as f:
                conf.write(f)
        return "Fofa配置写入完成"




