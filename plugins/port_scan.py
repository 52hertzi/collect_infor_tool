# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/30 4:28 下午
@Author ： Shawn
@FileName ：port_scan.py
@IDE ：PyCharm

"""

from socket import socket, AF_INET, SOCK_STREAM


default_port = [21,80,443,873,2601,2604,3128,4440,6082,8888,888,8083,8080,8090,8089,9090,3306,1433,1521,5432,27017,27018,3389,445,7001,7002,22,23,161,25,110,3389,5432,6379,8089]

def portScanner(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        s.close()
        return 1
    except:
        return 0

def check_mode_scan_port(target,obj):
    if obj == 0:
        alive = []
        for i in range(len(default_port)):
            port = default_port[i]
            try:
                s = socket(AF_INET,SOCK_STREAM)
                s.connect((target,port))
                s.close()
                alive.append(port)
            except Exception:
                pass
        return alive
    else:
       if len(obj) > 1:
           alives = []
           for i in range(len(obj)):
               port = int(obj[i])
               try:
                   s = socket(AF_INET, SOCK_STREAM)
                   s.connect((target, port))
                   s.close()
                   alives.append(port)
               except Exception:
                   pass
           return alives
       else:
           return portScanner(target,int(obj[0]))