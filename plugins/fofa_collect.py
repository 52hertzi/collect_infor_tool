# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/4 3:18 下午
@Author ： Shawn
@FileName ：fofa_collect.py
@IDE ：PyCharm

"""

import requests,base64,json,os
from _datetime import datetime
import pandas as pd
from config.config import conf


path = os.path.abspath(__file__)
os = os.path.split(path)[0]
def do_fofa_collect(grammar,size):
    host = ''
    title = ''
    ip = ''
    port = ''
    server = ''
    country = ''
    province = ''
    header = ''
    cert = ''
    rst = []
    column = ['域名', '标题', 'ip', '端口', '响应头','中间件', '证书' ,'国家','省份']
    email = conf()['fofa_email']
    key = conf()['fofa_key']
    byte_code =  grammar.encode("utf-8")
    grammars = base64.b64encode(byte_code).decode('ascii')
    try:
        url = 'https://fofa.info/api/v1/search/all?email='+ email +'&key='+ key +'&qbase64='+ str(grammars) + '&size=' + str(size) + '&fields=host,title,ip,port,server,country_name,province,header,cert'
        info = requests.get(url)
        data = json.loads(info.text)

        if data['error'] == 'true':
            return data['errmsg']
        else:
            for i in range(int(size)-1):
                for y in range(len(data['results'][i])):
                    fofa_data = data['results'][i][y]
                    if len(fofa_data) == 0:
                        fofa_data = 'None'
                    if y == 0:
                        host = fofa_data
                    elif y == 1:
                        title = fofa_data
                    elif y == 2:
                        ip = fofa_data
                    elif y == 3:
                        port = fofa_data
                    elif y == 4:
                        server = fofa_data
                    elif y == 5:
                        country = fofa_data
                    elif y == 6:
                        province = fofa_data
                    elif y == 7:
                        header = fofa_data
                    elif y == 8:
                        cert = fofa_data
                rst = [host,title,ip,port,header,server,cert,country,province]
                df = pd.DataFrame(rst).T
                if i == 0:
                    df.to_csv(os+'/../result/'+datetime.now().strftime("%Y%m%d_%H%M%S") +'.csv',index=False,header=column, encoding='utf-8', mode='a+')
                else:
                    df.to_csv(os + '/../result/' + datetime.now().strftime("%Y%m%d_%H%M%S")+ '.csv', index=False, header=False, encoding='utf-8',mode='a+')
            return os + '/../result/' + datetime.now().strftime("%Y%m%d_%H%M%S")+ '.csv'
    except Exception as e:
        print(e)
        return 0


