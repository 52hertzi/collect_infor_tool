# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/10 3:38 下午
@Author ： Shawn
@FileName ：search_ServerInfo.py
@IDE ：PyCharm

"""
import re
from config.request import do_requests
from config.config import conf

# 创建索引字典
data = ['Server', 'Set-Cookie', 'Access-Control-Allow-Methods','X-Powered-By']
dic_data = {'status': '0', 'Server': 'None', 'Set-Cookie': 'None', 'Access-Control-Allow-Methods': 'None','X-Powered-By':'None'}
dic_rep = {'Server':'服务器使用的中间件为','Set-Cookie':'服务器设置的Cookie值为','Access-Control-Allow-Methods':'可使用的服务器方法为','X-Powered-By':'后端语言'}
def check_target(url):
    regex_arg = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    if regex_arg.match(url) != None:
        dic_data['status'] = 1
        return processing_target(url)
    else:
        return analysis(url)

def processing_target(url):
    obj = 'headers'
    mode = conf()['mode']
    r = do_requests(url, mode, obj)
    for i in range(0,len(data)):
        if data[i] in r :
            dic_data[data[i]] = r[data[i]]
    return analysis(url)

#分析结果返回主程序
def analysis(url):
    NoNum = 0
    res = []
    if dic_data['status'] == '0':
        res.append(url + '-'*10 + '> 请输入正确的域名或ip!')
        return res
    else:
        for i in range(0,len(data)):
            if dic_data[data[i]] != 'None':
                res.append(dic_rep[data[i]] + ': ' + dic_data[data[i]])
                dic_data['status'] = '0'
            else:
                NoNum += 1
                if NoNum == len(data):
                    res.append('None')
        clear()
        return res

def clear():
    for i in range(0,len(data)):
        if dic_data[data[i]] != 'None':
            dic_data[data[i]] = 'None'
