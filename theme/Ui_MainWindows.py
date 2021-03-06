# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 607)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 330, 71, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(13, 353, 781, 201))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setStyleSheet("color:green;\n"
"background-color:black;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab.setGeometry(QtCore.QRect(10, 0, 781, 321))
        self.Tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.Tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tab.setElideMode(QtCore.Qt.ElideLeft)
        self.Tab.setMovable(False)
        self.Tab.setObjectName("Tab")
        self.do_collect = QtWidgets.QWidget()
        self.do_collect.setObjectName("do_collect")
        self.input_fofa_grammar = QtWidgets.QLineEdit(self.do_collect)
        self.input_fofa_grammar.setGeometry(QtCore.QRect(80, 110, 281, 21))
        self.input_fofa_grammar.setText("")
        self.input_fofa_grammar.setObjectName("input_fofa_grammar")
        self.label_2 = QtWidgets.QLabel(self.do_collect)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 51, 21))
        self.label_2.setObjectName("label_2")
        self.button_start_fofa = QtWidgets.QPushButton(self.do_collect)
        self.button_start_fofa.setGeometry(QtCore.QRect(330, 170, 113, 32))
        self.button_start_fofa.setObjectName("button_start_fofa")
        self.input_fofa_num = QtWidgets.QLineEdit(self.do_collect)
        self.input_fofa_num.setGeometry(QtCore.QRect(460, 110, 241, 21))
        self.input_fofa_num.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_fofa_num.setText("")
        self.input_fofa_num.setObjectName("input_fofa_num")
        self.label_26 = QtWidgets.QLabel(self.do_collect)
        self.label_26.setGeometry(QtCore.QRect(400, 110, 51, 21))
        self.label_26.setObjectName("label_26")
        self.Tab.addTab(self.do_collect, "")
        self.do_dir_brute = QtWidgets.QWidget()
        self.do_dir_brute.setObjectName("do_dir_brute")
        self.label_3 = QtWidgets.QLabel(self.do_dir_brute)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_3.setObjectName("label_3")
        self.input_target_dirBrute = QtWidgets.QLineEdit(self.do_dir_brute)
        self.input_target_dirBrute.setGeometry(QtCore.QRect(60, 20, 531, 21))
        self.input_target_dirBrute.setObjectName("input_target_dirBrute")
        self.button_start_dir_brute = QtWidgets.QPushButton(self.do_dir_brute)
        self.button_start_dir_brute.setGeometry(QtCore.QRect(600, 15, 121, 32))
        self.button_start_dir_brute.setObjectName("button_start_dir_brute")
        self.display_target_dirBrute = QtWidgets.QPlainTextEdit(self.do_dir_brute)
        self.display_target_dirBrute.setGeometry(QtCore.QRect(3, 90, 261, 201))
        self.display_target_dirBrute.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_target_dirBrute.setObjectName("display_target_dirBrute")
        self.display_result_dirBrute = QtWidgets.QTextEdit(self.do_dir_brute)
        self.display_result_dirBrute.setGeometry(QtCore.QRect(300, 90, 471, 201))
        self.display_result_dirBrute.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_result_dirBrute.setObjectName("display_result_dirBrute")
        self.label_4 = QtWidgets.QLabel(self.do_dir_brute)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.do_dir_brute)
        self.label_5.setGeometry(QtCore.QRect(710, 70, 60, 16))
        self.label_5.setObjectName("label_5")
        self.Tab.addTab(self.do_dir_brute, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.input_target_addr = QtWidgets.QLineEdit(self.tab_3)
        self.input_target_addr.setGeometry(QtCore.QRect(140, 110, 171, 21))
        self.input_target_addr.setObjectName("input_target_addr")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(80, 110, 60, 21))
        self.label_25.setObjectName("label_25")
        self.button_start_port = QtWidgets.QPushButton(self.tab_3)
        self.button_start_port.setGeometry(QtCore.QRect(310, 180, 113, 32))
        self.button_start_port.setObjectName("button_start_port")
        self.input_target_port = QtWidgets.QLineEdit(self.tab_3)
        self.input_target_port.setGeometry(QtCore.QRect(470, 110, 171, 21))
        self.input_target_port.setObjectName("input_target_port")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(410, 110, 60, 21))
        self.label_28.setObjectName("label_28")
        self.Tab.addTab(self.tab_3, "")
        self.do_domain = QtWidgets.QWidget()
        self.do_domain.setObjectName("do_domain")
        self.label_6 = QtWidgets.QLabel(self.do_domain)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 41, 21))
        self.label_6.setObjectName("label_6")
        self.input_single_subdomain = QtWidgets.QLineEdit(self.do_domain)
        self.input_single_subdomain.setGeometry(QtCore.QRect(70, 10, 541, 21))
        self.input_single_subdomain.setObjectName("input_single_subdomain")
        self.button_choice_file_subdoamin = QtWidgets.QPushButton(self.do_domain)
        self.button_choice_file_subdoamin.setGeometry(QtCore.QRect(220, 40, 113, 32))
        self.button_choice_file_subdoamin.setObjectName("button_choice_file_subdoamin")
        self.button_start_subdomain = QtWidgets.QPushButton(self.do_domain)
        self.button_start_subdomain.setGeometry(QtCore.QRect(340, 40, 113, 32))
        self.button_start_subdomain.setObjectName("button_start_subdomain")
        self.display_target_subdomain = QtWidgets.QPlainTextEdit(self.do_domain)
        self.display_target_subdomain.setGeometry(QtCore.QRect(13, 100, 321, 191))
        self.display_target_subdomain.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_target_subdomain.setObjectName("display_target_subdomain")
        self.display_result_subdomain = QtWidgets.QTextEdit(self.do_domain)
        self.display_result_subdomain.setGeometry(QtCore.QRect(410, 100, 341, 191))
        self.display_result_subdomain.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_result_subdomain.setObjectName("display_result_subdomain")
        self.label_7 = QtWidgets.QLabel(self.do_domain)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.do_domain)
        self.label_8.setGeometry(QtCore.QRect(410, 80, 71, 16))
        self.label_8.setObjectName("label_8")
        self.subdomain_check = QtWidgets.QCheckBox(self.do_domain)
        self.subdomain_check.setGeometry(QtCore.QRect(620, 0, 131, 41))
        self.subdomain_check.setObjectName("subdomain_check")
        self.Tab.addTab(self.do_domain, "")
        self.do_whois = QtWidgets.QWidget()
        self.do_whois.setObjectName("do_whois")
        self.label_9 = QtWidgets.QLabel(self.do_whois)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 41, 21))
        self.label_9.setObjectName("label_9")
        self.input_target_whois = QtWidgets.QLineEdit(self.do_whois)
        self.input_target_whois.setGeometry(QtCore.QRect(70, 20, 541, 21))
        self.input_target_whois.setObjectName("input_target_whois")
        self.whois_check = QtWidgets.QCheckBox(self.do_whois)
        self.whois_check.setGeometry(QtCore.QRect(620, 10, 131, 41))
        self.whois_check.setObjectName("whois_check")
        self.button_choice_file_whois = QtWidgets.QPushButton(self.do_whois)
        self.button_choice_file_whois.setGeometry(QtCore.QRect(210, 50, 113, 32))
        self.button_choice_file_whois.setObjectName("button_choice_file_whois")
        self.button_start_whois = QtWidgets.QPushButton(self.do_whois)
        self.button_start_whois.setGeometry(QtCore.QRect(340, 50, 113, 32))
        self.button_start_whois.setObjectName("button_start_whois")
        self.display_target_whois = QtWidgets.QPlainTextEdit(self.do_whois)
        self.display_target_whois.setGeometry(QtCore.QRect(10, 110, 321, 181))
        self.display_target_whois.setObjectName("display_target_whois")
        self.display_result_whois = QtWidgets.QTextEdit(self.do_whois)
        self.display_result_whois.setGeometry(QtCore.QRect(410, 110, 351, 181))
        self.display_result_whois.setObjectName("display_result_whois")
        self.label_10 = QtWidgets.QLabel(self.do_whois)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.do_whois)
        self.label_11.setGeometry(QtCore.QRect(410, 90, 60, 16))
        self.label_11.setObjectName("label_11")
        self.Tab.addTab(self.do_whois, "")
        self.do_whois1 = QtWidgets.QWidget()
        self.do_whois1.setObjectName("do_whois1")
        self.label_12 = QtWidgets.QLabel(self.do_whois1)
        self.label_12.setGeometry(QtCore.QRect(30, 20, 60, 21))
        self.label_12.setObjectName("label_12")
        self.input_target_whatweb = QtWidgets.QLineEdit(self.do_whois1)
        self.input_target_whatweb.setGeometry(QtCore.QRect(70, 20, 541, 21))
        self.input_target_whatweb.setObjectName("input_target_whatweb")
        self.CMS_ouput_check = QtWidgets.QCheckBox(self.do_whois1)
        self.CMS_ouput_check.setGeometry(QtCore.QRect(620, 10, 131, 41))
        self.CMS_ouput_check.setObjectName("CMS_ouput_check")
        self.display_target_whatweb = QtWidgets.QPlainTextEdit(self.do_whois1)
        self.display_target_whatweb.setGeometry(QtCore.QRect(13, 103, 251, 201))
        self.display_target_whatweb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_target_whatweb.setObjectName("display_target_whatweb")
        self.button_choice_file_whatweb = QtWidgets.QPushButton(self.do_whois1)
        self.button_choice_file_whatweb.setGeometry(QtCore.QRect(220, 50, 113, 32))
        self.button_choice_file_whatweb.setObjectName("button_choice_file_whatweb")
        self.button_start_whatweb = QtWidgets.QPushButton(self.do_whois1)
        self.button_start_whatweb.setGeometry(QtCore.QRect(360, 50, 113, 32))
        self.button_start_whatweb.setObjectName("button_start_whatweb")
        self.label_13 = QtWidgets.QLabel(self.do_whois1)
        self.label_13.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_13.setObjectName("label_13")
        self.display_target_result_whatweb = QtWidgets.QTextEdit(self.do_whois1)
        self.display_target_result_whatweb.setGeometry(QtCore.QRect(400, 100, 361, 211))
        self.display_target_result_whatweb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_target_result_whatweb.setObjectName("display_target_result_whatweb")
        self.label_14 = QtWidgets.QLabel(self.do_whois1)
        self.label_14.setGeometry(QtCore.QRect(690, 80, 71, 16))
        self.label_14.setObjectName("label_14")
        self.Tab.addTab(self.do_whois1, "")
        self.do_server_info = QtWidgets.QWidget()
        self.do_server_info.setObjectName("do_server_info")
        self.label_15 = QtWidgets.QLabel(self.do_server_info)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 60, 21))
        self.label_15.setObjectName("label_15")
        self.input_target_serverinfo = QtWidgets.QLineEdit(self.do_server_info)
        self.input_target_serverinfo.setGeometry(QtCore.QRect(60, 20, 541, 21))
        self.input_target_serverinfo.setObjectName("input_target_serverinfo")
        self.button_choice_file_server_info = QtWidgets.QPushButton(self.do_server_info)
        self.button_choice_file_server_info.setGeometry(QtCore.QRect(220, 60, 113, 32))
        self.button_choice_file_server_info.setObjectName("button_choice_file_server_info")
        self.button_start_server_info = QtWidgets.QPushButton(self.do_server_info)
        self.button_start_server_info.setGeometry(QtCore.QRect(350, 60, 113, 32))
        self.button_start_server_info.setObjectName("button_start_server_info")
        self.display_serverinfo_result = QtWidgets.QPlainTextEdit(self.do_server_info)
        self.display_serverinfo_result.setGeometry(QtCore.QRect(3, 103, 281, 191))
        self.display_serverinfo_result.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_serverinfo_result.setObjectName("display_serverinfo_result")
        self.label_16 = QtWidgets.QLabel(self.do_server_info)
        self.label_16.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_16.setObjectName("label_16")
        self.calc_ServerInfo_target = QtWidgets.QLineEdit(self.do_server_info)
        self.calc_ServerInfo_target.setGeometry(QtCore.QRect(40, 80, 61, 21))
        self.calc_ServerInfo_target.setFocusPolicy(QtCore.Qt.NoFocus)
        self.calc_ServerInfo_target.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calc_ServerInfo_target.setText("")
        self.calc_ServerInfo_target.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_ServerInfo_target.setObjectName("calc_ServerInfo_target")
        self.choice_display_result_serverinfo = QtWidgets.QTextEdit(self.do_server_info)
        self.choice_display_result_serverinfo.setGeometry(QtCore.QRect(390, 100, 371, 201))
        self.choice_display_result_serverinfo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.choice_display_result_serverinfo.setObjectName("choice_display_result_serverinfo")
        self.label_17 = QtWidgets.QLabel(self.do_server_info)
        self.label_17.setGeometry(QtCore.QRect(540, 80, 71, 16))
        self.label_17.setObjectName("label_17")
        self.ServerInfo_output_check = QtWidgets.QCheckBox(self.do_server_info)
        self.ServerInfo_output_check.setGeometry(QtCore.QRect(620, 16, 113, 32))
        self.ServerInfo_output_check.setObjectName("ServerInfo_output_check")
        self.Tab.addTab(self.do_server_info, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(50, 80, 60, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(50, 130, 60, 41))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(50, 190, 60, 21))
        self.label_20.setObjectName("label_20")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 60, 261, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.proxy_addr_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.proxy_addr_edit.setText("")
        self.proxy_addr_edit.setObjectName("proxy_addr_edit")
        self.gridLayout.addWidget(self.proxy_addr_edit, 1, 0, 1, 1)
        self.proxy_port_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.proxy_port_edit.setText("")
        self.proxy_port_edit.setObjectName("proxy_port_edit")
        self.gridLayout.addWidget(self.proxy_port_edit, 2, 0, 1, 1)
        self.proxy_argement = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.proxy_argement.setObjectName("proxy_argement")
        self.proxy_argement.addItem("")
        self.proxy_argement.addItem("")
        self.proxy_argement.addItem("")
        self.gridLayout.addWidget(self.proxy_argement, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(200, 30, 61, 21))
        self.label_21.setObjectName("label_21")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 60, 261, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fofa_email_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.fofa_email_edit.setObjectName("fofa_email_edit")
        self.verticalLayout.addWidget(self.fofa_email_edit)
        self.fofa_key_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.fofa_key_edit.setObjectName("fofa_key_edit")
        self.verticalLayout.addWidget(self.fofa_key_edit)
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(570, 30, 61, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(430, 90, 31, 41))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(430, 160, 31, 41))
        self.label_24.setObjectName("label_24")
        self.button_save_setup = QtWidgets.QPushButton(self.tab)
        self.button_save_setup.setGeometry(QtCore.QRect(550, 240, 113, 32))
        self.button_save_setup.setObjectName("button_save_setup")
        self.Tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(13, 23, 751, 271))
        self.plainTextEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.Tab.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "collect_info_tool   PowerBy shawn"))
        MainWindow.setProperty("append", _translate("MainWindow", "<font color=\"green\">???????????????????????????</font>"))
        self.label.setText(_translate("MainWindow", "???????????????"))
        self.input_fofa_grammar.setPlaceholderText(_translate("MainWindow", "??????fofa??????????????????"))
        self.label_2.setText(_translate("MainWindow", "fofa??????"))
        self.button_start_fofa.setText(_translate("MainWindow", "??????"))
        self.input_fofa_num.setPlaceholderText(_translate("MainWindow", "???????????????100???"))
        self.label_26.setText(_translate("MainWindow", "????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.do_collect), _translate("MainWindow", "????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????"))
        self.button_start_dir_brute.setText(_translate("MainWindow", "??????"))
        self.label_4.setText(_translate("MainWindow", "URL"))
        self.label_5.setText(_translate("MainWindow", "????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.do_dir_brute), _translate("MainWindow", "????????????/??????"))
        self.label_25.setText(_translate("MainWindow", "????????????"))
        self.button_start_port.setText(_translate("MainWindow", "????????????"))
        self.input_target_port.setPlaceholderText(_translate("MainWindow", "??????,???????????????????????????"))
        self.label_28.setText(_translate("MainWindow", "????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.tab_3), _translate("MainWindow", "????????????"))
        self.label_6.setText(_translate("MainWindow", "?????????"))
        self.button_choice_file_subdoamin.setText(_translate("MainWindow", "????????????"))
        self.button_start_subdomain.setText(_translate("MainWindow", "??????"))
        self.label_7.setText(_translate("MainWindow", "??????"))
        self.label_8.setText(_translate("MainWindow", "????????????"))
        self.subdomain_check.setText(_translate("MainWindow", "?????????????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.do_domain), _translate("MainWindow", "???????????????"))
        self.label_9.setText(_translate("MainWindow", "?????????"))
        self.whois_check.setText(_translate("MainWindow", "?????????????????????"))
        self.button_choice_file_whois.setText(_translate("MainWindow", "????????????"))
        self.button_start_whois.setText(_translate("MainWindow", "??????"))
        self.label_10.setText(_translate("MainWindow", "??????"))
        self.label_11.setText(_translate("MainWindow", "????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.do_whois), _translate("MainWindow", "whois??????/??????"))
        self.label_12.setText(_translate("MainWindow", "?????????"))
        self.CMS_ouput_check.setText(_translate("MainWindow", "?????????????????????"))
        self.button_choice_file_whatweb.setText(_translate("MainWindow", "????????????"))
        self.button_start_whatweb.setText(_translate("MainWindow", "??????"))
        self.label_13.setText(_translate("MainWindow", "??????"))
        self.label_14.setText(_translate("MainWindow", "????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.do_whois1), _translate("MainWindow", "????????????"))
        self.label_15.setText(_translate("MainWindow", "?????????"))
        self.input_target_serverinfo.setPlaceholderText(_translate("MainWindow", "http:// or https://"))
        self.button_choice_file_server_info.setText(_translate("MainWindow", "????????????"))
        self.button_start_server_info.setText(_translate("MainWindow", "??????"))
        self.label_16.setText(_translate("MainWindow", "??????"))
        self.label_17.setText(_translate("MainWindow", "????????????"))
        self.ServerInfo_output_check.setText(_translate("MainWindow", "????????????"))
        self.Tab.setTabText(self.Tab.indexOf(self.do_server_info), _translate("MainWindow", "???????????????"))
        self.label_18.setText(_translate("MainWindow", "????????????"))
        self.label_19.setText(_translate("MainWindow", "????????????"))
        self.label_20.setText(_translate("MainWindow", "????????????"))
        self.proxy_argement.setItemText(0, _translate("MainWindow", "HTTP"))
        self.proxy_argement.setItemText(1, _translate("MainWindow", "SOCKS"))
        self.proxy_argement.setItemText(2, _translate("MainWindow", "???????????????"))
        self.label_21.setText(_translate("MainWindow", "????????????"))
        self.label_22.setText(_translate("MainWindow", "fofa??????"))
        self.label_23.setText(_translate("MainWindow", "??????"))
        self.label_24.setText(_translate("MainWindow", "Key"))
        self.button_save_setup.setText(_translate("MainWindow", "??????"))
        self.Tab.setTabText(self.Tab.indexOf(self.tab), _translate("MainWindow", "??????"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "?????????Shawn\n"
"???????????????https://52hertzi.com\n"
"?????????????????????2022???4???4???\n"
"?????????????????????\n"
"1????????????????????????fofa?????????????????????\n"
"2???????????????/?????????????????????????????????????????????????????????????????????\n"
"3????????????????????????TCP??????????????????????????????????????????????????????21,80,443,873,2601,2604,3128,4440,6082,8888,888,8083,8080,8090,8089,9090,3306,1433,1521,5432,27017,27018,3389,445,7001,7002,22,23,161,25,110,3389,5432,6379,8089???\n"
"4???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????word??????\n"
"5???whois??????/???????????????????????????whois????????????????????????????????????????????????????????????????????????????????????????????????????????????word?????????\n"
"6??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????word?????????\n"
"7??????????????????????????????????????????Server ???Set-Cookie??? Access-Control-Allow-Methods???X-Powered-By????????????????????????????????????????????????????????????????????????word?????????\n"
"8????????????????????????????????????fofa?????????1???2???3????????????????????????????????????UA???"))
        self.Tab.setTabText(self.Tab.indexOf(self.tab_2), _translate("MainWindow", "??????"))
