# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/23 3:06 下午
@Author ： Shawn
@FileName ：whois.py
@IDE ：PyCharm

"""
import json
from config.request import only_use_requests


def do_whois(url):
    re = {
        "联系邮箱":"None",
        "联系电话":"None",
        "DNS解析服务器":"None",
        "主域名":"None",
        "域名状态":"None",
        "过期时间":"None",
        "注册人":"None",
        "注册主体":"None",
        "域名注册商":"None",
        "注册时间":"None",
        "更新时间":"None"
    }
    status = {
        'clientDeleteProhibited':'客户端删除禁止',
        'clientTransferProhibited':'客户转让禁止',
        'clientUpdateProhibited':'客户端更新禁止',
        'serverDeleteProhibited':'服务器删除禁止',
        'serverTransferProhibited':'服务器传输禁止',
        'serverUpdateProhibited':'服务器更新禁止'
    }
    s = []
    t = []
    try:
        whois_url = "https://api.devopsclub.cn/api/whoisquery?domain="+ str(url) +"&type=json&standard=true"
        obj = 'text'
        result = only_use_requests(whois_url,obj)
        result_json = json.loads(result)
        if result_json['data']['status'] == 0:
            if len(result_json['data']['data']['contactEmail']) != 0:
                re['联系邮箱'] = result_json['data']['data']['contactEmail']
            if len(result_json['data']['data']['contactPhone']) != 0:
                re['联系电话'] = result_json['data']['data']['contactPhone']
            if len(result_json['data']['data']['dnsNameServer'][0]) != 0:
                re['DNS解析服务器'] = result_json['data']['data']['dnsNameServer'][0] + ',' + result_json['data']['data']['dnsNameServer'][1]
            if len(result_json['data']['data']['domainName']) != 0:
                re['主域名'] = result_json['data']['data']['domainName']
            if len(result_json['data']['data']['domainStatus']) != 0:
                for i in status:
                    for o in range(len(result_json['data']['data']['domainStatus'])):
                        if i in result_json['data']['data']['domainStatus'][o]:
                            t.append(status[i])
                    re['域名状态'] = t
            if len(result_json['data']['data']['expirationTime']) != 0:
                re['过期时间'] = result_json['data']['data']['expirationTime']
            if len(result_json['data']['data']['registrant']) != 0:
                re['注册人'] = result_json['data']['data']['registrant']
            if len(result_json['data']['data']['registrar']) != 0:
                re['注册主体'] = result_json['data']['data']['registrar']
            if len(result_json['data']['data']['registrarWHOISServer']) != 0:
                re['域名注册商'] = result_json['data']['data']['registrarWHOISServer']
            if len(result_json['data']['data']['registrationTime']) != 0:
                re['注册时间'] = result_json['data']['data']['registrationTime']
            if len(result_json['data']['data']['updatedDate']) != 0:
                re['更新时间'] = result_json['data']['data']['updatedDate']

            return re
        elif result_json['data']['status'] == 1:
            return 0
    except Exception:
        return 0

def do_beian(url):
    try:
        re = {
            '拥有者': 'None',
            '名称': 'None',
            '类型': 'None',
            'ICP号': 'None',
            '标题': 'None',
            '更新时间': 'None'
        }
        obj = 'text'
        url_chinaz = "https://apidatav2.chinaz.com/single/icp?key=a6c5ac5b134e4cdeb1914b69443861e8&domain=" + url
        result_icp = only_use_requests(url_chinaz, obj)
        result_json = json.loads(result_icp)
        if result_json['StateCode'] == 1:
            if len(result_json['Result']['Owner']) != 0:
                re['拥有者'] = result_json['Result']['Owner']
            if len(result_json['Result']['CompanyName']) != 0:
                re['名称'] = result_json['Result']['CompanyName']
            if len(result_json['Result']['CompanyName']) != 0:
                re['类型'] = result_json['Result']['CompanyType']
            if len(result_json['Result']['CompanyName']) != 0:
                re['ICP号'] = result_json['Result']['SiteLicense']
            if len(result_json['Result']['SiteName']) != 0:
                re['标题'] = result_json['Result']['SiteName']
            if len(result_json['Result']['VerifyTime']) != 0:
                re['更新时间'] = result_json['Result']['VerifyTime']
            return re
        else:
            return 0
    except Exception:
        return 0


