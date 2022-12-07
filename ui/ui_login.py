# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginsbgiJo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(644, 524)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_12)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 25))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 6, 7, 0)
        self.horizontalSpacer_5 = QSpacerItem(549, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.close_btn = QPushButton(self.frame_10)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(15, 15))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border:1px solid;\n"
"	border-radius:7px;\n"
"\n"
"	border-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(255, 61, 176, 255));\n"
"color:#5f6368;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0.000318182, y1:0.545, x2:0.966227, y2:0.489, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(255, 65, 145, 255));\n"
"	color: rgb(243, 243, 243);\n"
";\n"
"	\n"
"}")

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.frame_10)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.stackedWidget = QStackedWidget(self.frame_11)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.verticalLayout = QVBoxLayout(self.welcome_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(self.welcome_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(193, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.home_btn_2 = QPushButton(self.frame_6)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setMinimumSize(QSize(58, 0))
        self.home_btn_2.setMaximumSize(QSize(49, 50))
        self.home_btn_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-image: url(:/image/style/btn.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.home_btn_2)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Poppins SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(193, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 100))
        self.label_3.setMaximumSize(QSize(100, 100))
        self.label_3.setStyleSheet(u"background-image: url(:/image/style/icons8-key-100.png);\n"
"")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.frame_9)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 220))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 15)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(75, 75, 75);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.textBrowser = QTextBrowser(self.frame_5)
        self.textBrowser.setObjectName(u"textBrowser")
        font2 = QFont()
        font2.setFamily(u"Poppins Light")
        font2.setBold(False)
        font2.setWeight(50)
        self.textBrowser.setFont(font2)
        self.textBrowser.setStyleSheet(u"color:#5f6368;")

        self.verticalLayout_7.addWidget(self.textBrowser)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(224, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.key_generate_btn = QPushButton(self.frame_3)
        self.key_generate_btn.setObjectName(u"key_generate_btn")
        self.key_generate_btn.setMinimumSize(QSize(120, 50))
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.key_generate_btn.setFont(font3)
        self.key_generate_btn.setStyleSheet(u"QPushButton{\n"
"border:2px solid;\n"
"border-radius:25px;\n"
"	border-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(255, 61, 176, 255));\n"
"color:#5f6368;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0.000318182, y1:0.545, x2:0.966227, y2:0.489, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(163, 39, 142, 255));\n"
"	color: rgb(243, 243, 243);\n"
";\n"
"	\n"
"	border-color: rgb(200, 200, 200);\n"
"}")

        self.horizontalLayout_2.addWidget(self.key_generate_btn)

        self.horizontalSpacer_2 = QSpacerItem(224, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.welcome_page)
        self.generate_cd_key_page = QWidget()
        self.generate_cd_key_page.setObjectName(u"generate_cd_key_page")
        self.verticalLayout_16 = QVBoxLayout(self.generate_cd_key_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.generate_cd_key_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 230))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 60))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(193, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.home_btn_3 = QPushButton(self.frame_16)
        self.home_btn_3.setObjectName(u"home_btn_3")
        self.home_btn_3.setMinimumSize(QSize(58, 0))
        self.home_btn_3.setMaximumSize(QSize(49, 50))
        self.home_btn_3.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-image: url(:/image/style/btn.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.home_btn_3)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_7 = QSpacerItem(193, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 180))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.frame_24 = QFrame(self.frame_17)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(20, 0))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_24)

        self.qr_lbl = QLabel(self.frame_17)
        self.qr_lbl.setObjectName(u"qr_lbl")
        self.qr_lbl.setMinimumSize(QSize(150, 150))
        self.qr_lbl.setMaximumSize(QSize(150, 150))
        self.qr_lbl.setStyleSheet(u"background-image: url(:/image/style/icons8-key-100.png);\n"
"")

        self.horizontalLayout_7.addWidget(self.qr_lbl)

        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(40, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.qr_save_btn = QPushButton(self.frame_23)
        self.qr_save_btn.setObjectName(u"qr_save_btn")
        self.qr_save_btn.setMaximumSize(QSize(30, 30))
        self.qr_save_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	background-image: url(:/image/style/download24.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(225, 225, 225);\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.qr_save_btn)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_25)


        self.horizontalLayout_7.addWidget(self.frame_23)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.verticalLayout_12.addWidget(self.frame_17)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 220))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 150))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 0, -1, 0)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 40))
        self.frame_22.setMaximumSize(QSize(16777215, 30))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.label_6 = QLabel(self.frame_22)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamily(u"Poppins SemiBold")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(75, 75, 75);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.cd_key_copy_btn = QPushButton(self.frame_22)
        self.cd_key_copy_btn.setObjectName(u"cd_key_copy_btn")
        self.cd_key_copy_btn.setMinimumSize(QSize(30, 25))
        self.cd_key_copy_btn.setMaximumSize(QSize(30, 16777215))
        self.cd_key_copy_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/copy24.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(225, 225, 225);\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.cd_key_copy_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addWidget(self.frame_22)

        self.textBrowser_2 = QTextBrowser(self.frame_19)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(7)
        self.textBrowser_2.setFont(font5)

        self.verticalLayout_14.addWidget(self.textBrowser_2)

        self.cd_key_edit = QLineEdit(self.frame_19)
        self.cd_key_edit.setObjectName(u"cd_key_edit")
        self.cd_key_edit.setMinimumSize(QSize(0, 45))
        self.cd_key_edit.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"	background-color: rgb(240, 240, 240);\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_14.addWidget(self.cd_key_edit)


        self.verticalLayout_13.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 100))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 15)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 60))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(224, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.log_next_btn = QPushButton(self.frame_21)
        self.log_next_btn.setObjectName(u"log_next_btn")
        self.log_next_btn.setMinimumSize(QSize(120, 50))
        self.log_next_btn.setFont(font3)
        self.log_next_btn.setStyleSheet(u"QPushButton{\n"
"border:2px solid;\n"
"border-radius:25px;\n"
"	border-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(255, 61, 176, 255));\n"
"color:#5f6368;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0.000318182, y1:0.545, x2:0.966227, y2:0.489, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(163, 39, 142, 255));\n"
"	color: rgb(243, 243, 243);\n"
";\n"
"	\n"
"	border-color: rgb(200, 200, 200);\n"
"}")

        self.horizontalLayout_8.addWidget(self.log_next_btn)

        self.horizontalSpacer_9 = QSpacerItem(224, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_15.addWidget(self.frame_21)


        self.verticalLayout_13.addWidget(self.frame_20)


        self.verticalLayout_11.addWidget(self.frame_18)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.generate_cd_key_page)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_8.addWidget(self.frame_11)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("login", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn_2.setToolTip(QCoreApplication.translate("login", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn_2.setText("")
        self.label.setText(QCoreApplication.translate("login", u"Class@home", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("login", u"Activation", None))
        self.textBrowser.setHtml(QCoreApplication.translate("login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Poppins Light'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Security code must be entered to use this software. To get it, the CD number should be sent to the software company. Get the cd number by pressing the &quot;Generate CD Key&quot; button.</p></body></html>", None))
        self.key_generate_btn.setText(QCoreApplication.translate("login", u"Generate CD Key", None))
#if QT_CONFIG(tooltip)
        self.home_btn_3.setToolTip(QCoreApplication.translate("login", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn_3.setText("")
        self.label_4.setText(QCoreApplication.translate("login", u"Class@home", None))
        self.qr_lbl.setText("")
        self.qr_save_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("login", u"CD KEY", None))
        self.cd_key_copy_btn.setText(QCoreApplication.translate("login", u".", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Poppins Light'; font-size:7.25pt;\">The CD number should be sent to the software company. to get  the Activation Key. </span><span style=\" font-family:'Poppins Light'; font-size:8.25pt; color:#bf0000;\">Do Not Edit CD Key!</span></p></body></html>", None))
        self.log_next_btn.setText(QCoreApplication.translate("login", u"Next", None))
    # retranslateUi

