# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/7 11:27 上午
@Author ： Shawn
@FileName ：collect_infor_tools.py
@IDE ：PyCharm

"""


from PyQt5 import QtWidgets, QtGui
import sys, time,platform,tldextract,re
from PyQt5.QtGui import QIcon
from theme.Ui_MainWindows import Ui_MainWindow
from config.config import conf_write_proxy,conf
from config.request import get_Lan_ip,get_ip
from plugins.search_ServerInfo import check_target
from plugins.whatWeb import input_url
from plugins.output_docx import check_content
from plugins.whois import do_whois,do_beian
from plugins.subdomain import run_single
from plugins.port_scan import check_mode_scan_port
from plugins.dir_brute import check_dir_brute
from plugins.fofa_collect import do_fofa_collect

class MainWindow(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(800, 590)
        self.setupUi(self)
        self.load_event()
        self.statusBar().showMessage("当前设备:" + platform.platform() + "  局域网IP：" + get_Lan_ip() + "  出网IP：" + get_ip())
    # 当前时间
    def time(self):
        NowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return NowTime

    def load_event(self):
        def proxy_change():
            proxy_arg_num = str(self.proxy_argement.currentIndex()) #代理协议索引
            if proxy_arg_num == "0":
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 代理协议当前为： '+"HTTP"+'</span>')
            elif proxy_arg_num == "1":
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 代理协议当前为： ' + "SOCKS5" + '</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 代理协议当前为： ' + "不使用代理" + '</span>')
            return proxy_arg_num
        self.proxy_argement.currentIndexChanged.connect(proxy_change)
        def setup_input_ip():
            proxy_ip = self.proxy_addr_edit.text()
            if len(proxy_ip) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] 代理地址当前为空</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 代理地址为： ' + proxy_ip + '</span>')
            return proxy_ip
        if conf()['mode'] == 0:
            self.proxy_addr_edit.setText(conf()['http_proxy'])
        elif conf()['mode'] == 1:
            self.proxy_addr_edit.setText(conf()['socks_proxy'])
        else:
            self.proxy_addr_edit.setText(' ')
        self.proxy_addr_edit.editingFinished.connect(setup_input_ip)
        def setup_input_port():
            proxy_port = self.proxy_port_edit.text()
            if len(proxy_port) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] 代理地址当前为空</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 代理端口为： ' + proxy_port + '</span>')
            return proxy_port
        if conf()['mode'] == 0:
            self.proxy_port_edit.setText(conf()['http_port'])
        elif conf()['mode'] == 1:
            self.proxy_port_edit.setText(conf()['socks_port'])
        else:
            self.proxy_port_edit.setText(' ')
        self.proxy_port_edit.editingFinished.connect(setup_input_port)
        def setup_fofa_email():
            fofa_email = self.fofa_email_edit.text()
            if len(fofa_email) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] Fofa邮箱当前为空</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] fofa_email 为： ' + fofa_email + '</span>')
            return fofa_email
        self.fofa_email_edit.setText(conf()['fofa_email'])
        self.fofa_email_edit.editingFinished.connect(setup_fofa_email)
        def setup_fofa_key():
            fofa_key = self.fofa_key_edit.text()
            if len(fofa_key) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] Fof密钥当前为空</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] fofa_key 为： ' + fofa_key + '</span>')
            return fofa_key
        self.fofa_key_edit.setText(conf()['fofa_key'])
        self.fofa_key_edit.editingFinished.connect(setup_fofa_key)
        def setup_save():
            if proxy_change() != 2:
                if len(self.proxy_addr_edit.text()) > 1:
                    if len(self.proxy_port_edit.text()) > 1:
                        data = {'ip':setup_input_ip(),'port':setup_input_port(),'email':setup_fofa_email(),'key':setup_fofa_key(),'mode':proxy_change()}
                        self.plainTextEdit.appendHtml('<span style="color:green;">[+] 保存配置： ' + str(conf_write_proxy(data)) + '</span>')
                        self.statusBar().showMessage("当前设备:" + platform.platform() + "  局域网IP：" + get_Lan_ip() + "  出网IP：" + get_ip())
                    else:
                        self.plainTextEdit.appendHtml('<span style="color:red;">[-] 端口为空！</span>')
                elif len(self.proxy_port_edit.text()) <= 0:
                    data = {'ip': '', 'port': '', 'email': setup_fofa_email(),'key': setup_fofa_key(), 'mode': proxy_change()}
                    self.plainTextEdit.appendHtml('<span style="color:green;">[+] 保存配置： ' + conf_write_proxy(data) + '</span>')
                    self.statusBar().showMessage("当前设备:" + platform.platform() + "  局域网IP：" + get_Lan_ip() + "  出网IP：" + get_ip())


                else:
                    self.plainTextEdit.appendHtml('<span style="color:red;">[-] 代理地址为空！</span>')
            else:
                data = {'ip': '', 'port': '', 'email': setup_fofa_email(), 'key': setup_fofa_key(),'mode': proxy_change()}
                self.statusBar().showMessage( "当前设备:" + platform.platform() + "  局域网IP：" + get_Lan_ip() + "  出网IP：" + get_ip())
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 保存配置： ' + conf_write_proxy(data) + '</span>')

        self.button_save_setup.clicked.connect(setup_save)
        def display_input_target_serverInfo():
            result = {}
            res_ = ''
            target_info = self.input_target_serverinfo.text()
            self.plainTextEdit.appendHtml('<span style="color:green;">[+] 开始获取目标地址信息: ' + target_info + '</span>')
            res = check_target(target_info)
            self.choice_display_result_serverinfo.append(str(target_info))
            for reNum in range(len(res)):
                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ' + str(res[reNum]) + '</span>')
                self.choice_display_result_serverinfo.append(str(res[reNum]) + '\n')
                if len(res) >= 2:
                    if reNum == 0:
                        res_ = res[reNum]
                    else:
                        res_ = res_ + res[reNum]
                    result[target_info] = res_
                else:
                    result[target_info] = res[reNum]
            return result
        def display_input_target_serverInfo_dir():
            target_dir ,target_type= QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "./", "Text Files (*.txt)")
            if target_dir == '':
               self.plainTextEdit.appendHtml('<span style="color:red;">[+] 未选择文件 ！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 选择目标路径为：' + target_dir + '</span>')
                self.input_target_serverinfo.clear()
                self.display_serverinfo_result.clear()
                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ：点击开始进行 ！</span>')
                return input_serverinfo_result(target_dir)
        self.button_choice_file_server_info.clicked.connect(display_input_target_serverInfo_dir)
        def input_serverinfo_result(path):
            finish = 0
            sum = calc_file_quantity(path)
            re = str(str(finish)+'/'+str(sum))
            self.calc_ServerInfo_target.setText(re)
            with open(path,'r') as f:
                for f1 in f.readlines():
                    f1 = f1.strip()
                    if f1 == '无' or f1 == '':
                        pass
                    elif 'http' not in f1:
                        if 'https' not in f1:
                            f1 = 'https://' + f1
                            self.display_serverinfo_result.appendHtml(f1)
                        else:
                            self.display_serverinfo_result.appendHtml(f1)
                    else:
                        self.display_serverinfo_result.appendHtml(f1)
            return sum
        # 计算文件数量
        def calc_file_quantity(path):
            count = 0
            with open(path,'r') as f:
                for line in f.readlines():
                    if line.strip('\n') != '无' and line.strip('\n') != '':
                        count += 1
            return count
        def start_server_info():
            ## 导出为报告
            def ServerInfo_output(result):
                type = 'ServerInfo'
                self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：数据导出为报告中，请稍等  ！</span>')
                ouput_addr = check_content(result,type)
                self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：报告已导出在：'+ ouput_addr +'</span>')
            sum = 0
            result = {}
            if len(self.input_target_serverinfo.text()) == 0:
                url = self.display_serverinfo_result.toPlainText().split('\n')
                for i in range(0,len(url)):
                    self.plainTextEdit.appendHtml('<span style="color:green;">[+] 开始获取目标地址信息:'+url[i]+'</span>')
                    QtWidgets.QApplication.processEvents()
                    res = check_target(url[i])
                    for reNum in range(len(res)):
                        self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ' + str(res[reNum]) + '</span>')
                    sum += 1
                    re = str(str(sum) + '/' + str(len(url)))
                    self.calc_ServerInfo_target.setText(re)
                    # 处理最后一个url
                    if len(url) - i == 1:
                        res_1 = ''
                        self.display_serverinfo_result.clear()
                        self.choice_display_result_serverinfo.append(url[i])
                        for reNum in range(len(res)):
                            self.choice_display_result_serverinfo.append(res[reNum] + '\n')
                            if len(res) > 2:
                                if reNum == 0:
                                    res_1 = res[reNum]
                                else:
                                    res_1 = res_1 + res[reNum]
                                result[url[i]] = res_1
                            else:
                                result[url[i]] = res[reNum]
                    # 处理url
                    else:
                        res_ = ''
                        self.display_serverinfo_result.setMaximumBlockCount(len(url) - i)
                        self.choice_display_result_serverinfo.append(url[i])
                        for reNum in range(len(res)):
                            self.choice_display_result_serverinfo.append(res[reNum] + '\n')
                            if len(res) > 2:
                                if reNum == 0:
                                    res_ = res[reNum]
                                else:
                                    res_ = res_ + res[reNum]
                                result[url[i]] = res_
                            else:
                                result[url[i]] = res[reNum]
            else:
                result = display_input_target_serverInfo()
            if self.ServerInfo_output_check.isChecked():
                ServerInfo_output(result)
                result.clear()
            self.display_serverinfo_result.setMaximumBlockCount(999)
        self.button_start_server_info.clicked.connect(start_server_info)
        ## cms
        def GetWhatWeb():
            target = self.input_target_whatweb.text()
            if len(target) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] 请输入Url地址或IP地址！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] 开始识别目标:' + target + '</span>')
                QtWidgets.QApplication.processEvents()
                single_target_whatweb(target)
        def single_target_whatweb(target):
            url = self.display_target_whatweb.toPlainText().split('\n')
            msg = input_url(target)
            if msg[0] == 1:
                self.plainTextEdit.appendHtml('<span style="color:orange;">[+] '+ target +' 已识别到目标使用CMS为:'+ msg[1] +'</span>')
                self.display_target_whatweb.setMaximumBlockCount(len(url) - 1)
                self.display_target_result_whatweb.append(target+' 使用的CMS系统为：\n'+msg[1]+'\n')
                if len(url) == 1:
                    self.display_target_whatweb.clear()
                QtWidgets.QApplication.processEvents()
                return msg[1]
            elif msg[0] == 2:
                self.plainTextEdit.appendHtml('<span style="color:orange;">[+] '+ target +' 已识别到目标可能使用CMS为:'+ msg[1] +'</span>')
                self.display_target_whatweb.setMaximumBlockCount(len(url) - 1)
                self.display_target_result_whatweb.append(target+' 使用的CMS系统可能为：\n'+msg[1]+'\n')
                if len(url) == 1:
                    self.display_target_whatweb.clear()
                QtWidgets.QApplication.processEvents()
                return msg[1]
            else:
                self.plainTextEdit.appendHtml('<span style="color:red;">[-] '+ target + ' 未识别到目标目标CMS</span>')
                self.display_target_whatweb.setMaximumBlockCount(len(url) - 1)
                self.display_target_result_whatweb.append(target+' 未识别到使用使用的CMS系统\n')
                if len(url) == 1:
                    self.display_target_whatweb.clear()
                QtWidgets.QApplication.processEvents()
                return msg[1]
        def file_target_whatweb():
            target_dir, target_type = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "./", "Text Files (*.txt)")
            if target_dir == '':
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] 未选择文件 ！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 选择目标路径为：' + target_dir + '</span>')
                self.input_target_whatweb.clear()
                self.display_target_whatweb.clear()
                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ：点击开始进行 ！</span>')
            input_display_wahtweb(target_dir)
        self.button_choice_file_whatweb.clicked.connect(file_target_whatweb)
        def input_display_wahtweb(path):
            with open(path, 'r') as f:
                for f1 in f.readlines():
                    f1 = f1.strip()
                    if f1 == '无' or f1 == '':
                        pass
                    elif 'http' not in f1:
                        if 'https' not in f1:
                            f1 = 'https://' + f1
                            f2 = f1.split('/')[0] + '//' + f1.split('/')[2]
                            self.display_target_whatweb.appendHtml(f2)
                        else:
                            f2 = f1.split('/')[0] + '//' + f1.split('/')[2]
                            self.display_target_whatweb.appendHtml(f2)
                    else:
                        f2 = f1.split('/')[0] + '//' + f1.split('/')[2]
                        self.display_target_whatweb.appendHtml(f2)

        def file_target_whatweb_start():
            ## 导出报告
            def output_info(result):
                type = 'CMS_info'
                self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：数据导出为报告中，请稍等  ！</span>')
                ouput_cms = check_content(result, type)
                self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：报告已导出在：' + ouput_cms + '</span>')
            result = {}
            url = str(self.display_target_whatweb.toPlainText()).split('\n')
            if self.CMS_ouput_check.isChecked():
                for i in range(len(url)):
                    result[url[i]] = single_target_whatweb(url[i])
                output_info(result)
            else:
                for i in range(len(url)):
                    single_target_whatweb(url[i])
            result.clear()
        def start_wahtweb():
            if len(self.display_target_whatweb.toPlainText()) == 0:
                GetWhatWeb()
            elif len(self.display_target_whatweb.toPlainText()) > 0:
                file_target_whatweb_start()
        self.button_start_whatweb.clicked.connect(start_wahtweb)

        ## Whois信息收集
        def Whois_Info():
            def single_target_whois():
                t = []
                target = self.input_target_whois.text()
                t.append(target)
                if len(t[0]) == 0:
                    self.plainTextEdit.appendHtml('<span style="color:red;">[+] 请输入Url地址或选择文件！</span>')
                else:
                    self.plainTextEdit.appendHtml('<span style="color:green;">[+] 开始识别目标:' + target + '</span>')
                    do_get_info_whois(t)
            def do_get_info_whois(target):
                domain = ''
                full_whois = []
                type = 'WhoisInfo'
                count = 0
                fail_count = 0
                addr = ''
                for i in range(len(target)):
                    msg = do_whois(str(target[i]))
                    if len(self.display_target_whois.toPlainText().split('\n')) > 1:
                        self.display_target_whois.setMaximumBlockCount(len(self.display_target_whois.toPlainText().split('\n')) - 1)
                        QtWidgets.QApplication.processEvents()
                    else:
                        self.display_target_whois.clear()
                    # whois
                    try:
                        if msg != 0 and msg != None:
                            self.plainTextEdit.appendHtml('<span style="color:green;">[+] 已获取到目标：'+target[i] +'的Whois信息如下：</span>')
                            for x in range(len(msg['域名状态'])):
                                if x == 0:
                                    domain = msg['域名状态'][x]
                                else:
                                    domain = domain + ',' + msg['域名状态'][x]
                            self.plainTextEdit.appendHtml('<span style="color:orange;">[+] 联系邮箱:' + str(msg['联系邮箱']) +
                                '\n联系电话:' + str(msg['联系电话']) +
                                '\nDNS解析服务器:' + str(msg['DNS解析服务器']) +
                                '\n主域名:' + str(msg['主域名']) +
                                '\n域名状态:' + domain +
                                '\n过期时间:' + str(msg['过期时间']) +
                                '\n注册人:' + str(msg['注册人']) +
                                '\n注册主体:' + str(msg['注册主体']) +
                                '\n域名注册商:' + str(msg['域名注册商']) +
                                '\n注册时间:' + str(msg['注册时间']) +
                                '\n更新时间:' + str(msg['更新时间']) +
                                '</span>')
                            self.plainTextEdit.appendHtml('<span style="color:pink;">[+] 开始获取：' + target[i] + '的备案信息，请稍后！</span>')
                            QtWidgets.QApplication.processEvents()
                            self.display_result_whois.append(target[i] + '的whois信息如下：')
                            self.display_result_whois.append('联系邮箱:' + str(msg['联系邮箱']) +
                                                             '\n联系电话:' + str(msg['联系电话']) +
                                                             '\nDNS解析服务器:' + str(msg['DNS解析服务器']) +
                                                             '\n主域名:' + str(msg['主域名']) +
                                                             '\n域名状态:' + domain +
                                                             '\n过期时间:' + str(msg['过期时间']) +
                                                             '\n注册人:' + str(msg['注册人']) +
                                                             '\n注册主体:' + str(msg['注册主体']) +
                                                             '\n域名注册商:' + str(msg['域名注册商']) +
                                                             '\n注册时间:' + str(msg['注册时间']) +
                                                             '\n更新时间:' + str(msg['更新时间'] + '\n')
                                                             )
                            QtWidgets.QApplication.processEvents()
                        else:
                            self.plainTextEdit.appendHtml('<span style="color:red;">[-] ' + target[i] + ' 无法获取目标whois信息，请检查目标是否失活及网络</span>')
                            self.display_result_whois.append(target[i] + '\n无法获取目标whois信息，请检查目标是否失活及网络')
                            QtWidgets.QApplication.processEvents()
                        # ICP
                        icp_msg = do_beian(target[i])
                        if icp_msg != 0:
                            self.plainTextEdit.appendHtml('<span style="color:green;">[+] 已获取到目标：' + target[i] + '的备案信息如下：</span>')
                            self.plainTextEdit.appendHtml('<span style="color:orange;">[+] ' + '所有者：' + icp_msg['拥有者'] +
                                                          '\n名称:' + str(icp_msg['名称']) +
                                                          '\n类型:' + str(icp_msg['类型']) +
                                                          '\nICP号:' + str(icp_msg['ICP号']) +
                                                          '\n标题:' + str(icp_msg['标题']) +
                                                          '\n更新时间:' + str(icp_msg['更新时间']) +
                                                          '</span>')
                            QtWidgets.QApplication.processEvents()
                            self.display_result_whois.append(target[i] + '的备案信息如下：')
                            self.display_result_whois.append('所有者:' + str(icp_msg['拥有者']) +
                                                             '\n名称:' + str(icp_msg['名称']) +
                                                             '\n类型:' + str(icp_msg['类型']) +
                                                             '\nICP号:' + str(icp_msg['ICP号']) +
                                                             '\n标题:' + str(icp_msg['标题']) +
                                                             '\n更新时间:' + str(icp_msg['更新时间']) + '\n')
                            QtWidgets.QApplication.processEvents()
                        else:
                            self.plainTextEdit.appendHtml('<span style="color:red;">[-] ' + target[i] + ' 无法获取目标备案信息，请检查目标是否失活及网络</span>')
                            self.display_result_whois.append(target[i] + '\n无法获取目标备案信息，请检查目标是否失活及网络')
                            QtWidgets.QApplication.processEvents()
                        # 报告导出
                        if self.whois_check.isChecked():
                            ## whois,icp均不为空方可导出报告
                            if msg != 0 and msg != None and icp_msg != 0:
                                msg['url'] = target[i]
                                msg['end'] = count
                                # 获取返回保存路径
                                if count == 0:
                                    msg['addr'] = 'None'
                                    full_whois.append(msg)
                                    full_whois.append(icp_msg)
                                    addr = check_content(full_whois, type)
                                    full_whois.clear()
                                    count += 1
                                elif msg['end'] == len(target) - fail_count - 1:
                                    msg['end'] = 'end'
                                    msg['addr'] = addr
                                    full_whois.append(msg)
                                    full_whois.append(icp_msg)
                                    self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：数据导出为报告中，请稍等  ！</span>')
                                    whois = check_content(full_whois, type)
                                    self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：报告已导出在：' + whois + '</span>')
                                    full_whois.clear()
                                else:
                                    msg['addr'] = addr
                                    full_whois.append(msg)
                                    full_whois.append(icp_msg)
                                    check_content(full_whois, type)
                                    full_whois.clear()
                                    count += 1
                            else:
                                fail_count += 1

                    except Exception:
                        self.plainTextEdit.appendHtml('<span style="color:red;">[-] 内部程序错误！')

            def file_target_whois():
                target = self.display_target_whois.toPlainText().split('\n')
                do_get_info_whois(target)
                self.display_target_whois.setMaximumBlockCount(999)
            if len(self.input_target_whois.text()) != 0:
                single_target_whois()
            else:
                file_target_whois()
        self.button_start_whois.clicked.connect(Whois_Info)

        def choice_file_whois():
            target_dir, target_type = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "./", "Text Files (*.txt)")
            self.display_target_whois.clear()
            if target_dir == '':
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] 未选择文件 ！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 选择目标路径为：' + target_dir + '</span>')
                self.display_target_whois.setMaximumBlockCount(999)
                self.input_target_whois.clear()
                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ：点击开始进行 ！</span>')
                self.input_target_whois.clear()
                file_input_target_whois(target_dir)
        self.button_choice_file_whois.clicked.connect(choice_file_whois)
        def file_input_target_whois(path):
            with open(path, 'r') as f:
                for f1 in f.readlines():
                    f1 = f1.strip()
                    if f1 == '无' or f1 == '':
                        pass
                    elif 'http' in f1:
                        f2 = f1.split('/')[2]
                        f2.replace('http://', ' ')
                        self.display_target_whois.appendHtml(f2)
                    elif 'https' in f1:
                        f2 = f1.split('/')[2]
                        f2.replace('https://',' ')
                        self.display_target_whois.appendHtml(f2)
                    else:
                        f2 = f1.split('/')[0]
                        self.display_target_whois.appendHtml(f2)

        ## Subdomain
        def subdomain_event(target,re):
            if len(re) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] ：' + target + ' 未找到子域名信息！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] ：' + target + ' 已找到子域名信息，如下:</span>')
                for i in range(len(re)):
                    self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ：' + str(re[i]) + '</span>')
                self.display_result_subdomain.append(target + '的子域名如下：')
                for r in range(len(re)):
                    self.display_result_subdomain.append(re[r])
                QtWidgets.QApplication.processEvents()

        def single_target_subdomain():
            res = {}
            if len(self.display_target_subdomain.toPlainText()) != 0:
                target = self.display_target_subdomain.toPlainText().split('\n')
                for i in range(len(target)):
                    re = run_single(target[i])
                    self.display_target_subdomain.setMaximumBlockCount(len(self.display_target_subdomain.toPlainText().split('\n')) - 1)
                    res[target[i]] = re
                    subdomain_event(target[i], re)
                    QtWidgets.QApplication.processEvents()
                    if i == len(target) - 1:
                        self.plainTextEdit.appendHtml('<span style="color:orange;">[+] ：已完成子域名信息收集！</span>')
                        self.display_target_subdomain.clear()
                        if self.subdomain_check.isChecked():
                            obj = 'Subdomain'
                            addr = check_content(res,obj)
                            self.plainTextEdit.appendHtml('<span style="color:purple;">[+] ：报告已导出在：' + str(addr) + '！</span>')
            else:
                target = self.input_single_subdomain.text()
                re = run_single(target)
                subdomain_event(target,re)
        def file_input_deal(path):
            ## 提取主域
            with open(path,'r') as f:
                for f1 in f.readlines():
                    f1 = f1.strip()
                    if f1 == '无':
                        pass
                    else:
                        f2 = tldextract.extract(f1)
                        domain = "{}.{}".format(f2.domain, f2.suffix)
                        self.display_target_subdomain.appendPlainText(domain)
        def choice_subdomain_file():
            target_dir, target_type = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "./", "Text Files (*.txt)")
            self.display_target_subdomain.clear()
            if target_dir == '':
                self.plainTextEdit.appendHtml('<span style="color:red;">[+] 未选择文件 ！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 选择目标路径为：' + target_dir + '</span>')
                self.input_single_subdomain.clear()
                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ：点击开始进行 ！</span>')
                self.input_single_subdomain.clear()
                file_input_deal(target_dir)
        self.button_choice_file_subdoamin.clicked.connect(choice_subdomain_file)
        def subdomain_brute():
            if len(self.display_target_subdomain.toPlainText()) != 0:
                single_target_subdomain()
            elif len(self.input_single_subdomain.text()) != 0:
                single_target_subdomain()
            else:
                self.plainTextEdit.appendHtml('<span style="color:red;">[-] 请输入目标或选择文件点击开始进行 ！ ！</span>')
        self.button_start_subdomain.clicked.connect(subdomain_brute)

        # Port_scan
        def start_port_scan():
            if len(self.input_target_addr.text()) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[-] 请输入目标点击开始 ！</span>')
            else:
                target = self.input_target_addr.text()
                isIp = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",target)
                if isIp:
                    if len(self.input_target_port.text()) == 0:
                        self.plainTextEdit.appendHtml('<span style="color:green;">[+] 开始扫描'+ target +'端口 ！</span>')
                        QtWidgets.QApplication.processEvents()
                        res = check_mode_scan_port(target, 0)
                        if res != 0:
                            for i in range(len(res)):
                                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] '+ str(res[i]) +' 存活 ！</span>')
                        else:
                            self.plainTextEdit.appendHtml('<span style="color:red;">[-] 扫描错误 ！</span>')
                    else:
                        port = []
                        port.append(self.input_target_port.text().split(','))
                        res = check_mode_scan_port(target, port[0])
                        if res == 1:
                            self.plainTextEdit.appendHtml('<span style="color:pink;">[+] '+ str(port[0][0]) +' 存活 ！</span>')
                        elif res == 0:
                            self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ' + str(port[0][0]) + ' 不存活 ！</span>')
                        else:
                            for o in range(len(res)):
                                self.plainTextEdit.appendHtml('<span style="color:pink;">[+] ' + str(res[o]) + ' 存活 ！</span>')
                else:
                    self.plainTextEdit.appendHtml('<span style="color:red;">[-] IP格式错误 ！</span>')
        self.button_start_port.clicked.connect(start_port_scan)

        ## dir_brute
        def start_dirBrute():
            if len(self.input_target_dirBrute.text()) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[-] 目标Url为空，请输入目标 ！</span>')
            else:
                self.plainTextEdit.appendHtml('<span style="color:green;">[+] 开始探测目标目录 ！</span>')
                self.display_target_dirBrute.appendPlainText(self.input_target_dirBrute.text())
                QtWidgets.QApplication.processEvents()
                target = self.input_target_dirBrute.text()
                res = check_dir_brute(target)
                if len(res) != 0 and len(res) > 1:
                    for i in range(len(res)):
                        self.plainTextEdit.appendHtml('<span style="color:pink;">[+] 目标'+ target +'存在目录如下： '+ res[i] +'</span>')
                        self.display_result_dirBrute.append(res[i])
                        QtWidgets.QApplication.processEvents()
                elif res[0] == 'error':
                    self.plainTextEdit.appendHtml('<span style="color:red;">[+] 网络错误 ！</span>')
                    self.display_result_dirBrute.append(target+'\n'+'网络错误')
                else:
                    self.plainTextEdit.appendHtml('<span style="color:orange;">[+] 未找到目标敏感目录 ！</span>')
                    self.display_result_dirBrute.appendPlainText(target + '\n' + '未找到目标敏感目录 !')
        self.button_start_dir_brute.clicked.connect(start_dirBrute)

        def fofa_collect():
            fofa_num = ''
            grammar = ''
            if len(self.input_fofa_num.text()) == 0:
                fofa_num = 100
            else:
                fofa_num = self.input_fofa_num.text()
            if len(self.input_fofa_grammar.text()) == 0:
                self.plainTextEdit.appendHtml('<span style="color:red;">[-] 请输入语法进行查询 ！</span>')
            else:
                grammar = self.input_fofa_grammar.text().replace("'","'")
                res_addr = do_fofa_collect(grammar,fofa_num)
                if res_addr != 0:
                    self.plainTextEdit.appendHtml('<span style="color:pink;">[+] 查询已完成！已导出至'+ res_addr +'</span>')
                else:
                    self.plainTextEdit.appendHtml('<span style="color:red;">[-] 查询出错，请检查语法问题或网络或fofa配置或fofa额度 ！</span>')
        self.button_start_fofa.clicked.connect(fofa_collect)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # splash启动界面图
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("icon/splash.png"))
    splash.show()
    QtWidgets.qApp.processEvents()
    win = MainWindow()
    win.setWindowIcon(QIcon('icon/icon.png'))
    win.show()
    splash.finish(win)
    sys.exit(app.exec_())
