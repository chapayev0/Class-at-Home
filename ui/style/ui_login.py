# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginTiDEFY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(647, 518)
        self.horizontalLayout = QHBoxLayout(login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(login)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.verticalLayout = QVBoxLayout(self.welcome_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.welcome_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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

        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.frame_9)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(224, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.key_generate_btn = QPushButton(self.frame_3)
        self.key_generate_btn.setObjectName(u"key_generate_btn")
        self.key_generate_btn.setMinimumSize(QSize(120, 50))
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.key_generate_btn.setFont(font1)
        self.key_generate_btn.setStyleSheet(u"QPushButton{\n"
"border:2px solid;\n"
"border-radius:25px;\n"
"	border-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(255, 61, 176, 255));\n"
"color:#5f6368;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0.000318182, y1:0.545, x2:0.966227, y2:0.489, stop:0 rgba(229, 47, 80, 255), stop:1 rgba(163, 39, 142, 255));\n"
"	color: rgb(243, 243, 243);\n"
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
        self.stackedWidget.addWidget(self.generate_cd_key_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.home_btn_2.setToolTip(QCoreApplication.translate("login", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn_2.setText("")
        self.label.setText(QCoreApplication.translate("login", u"Class@home", None))
        self.key_generate_btn.setText(QCoreApplication.translate("login", u"Generate CD Key", None))
    # retranslateUi

