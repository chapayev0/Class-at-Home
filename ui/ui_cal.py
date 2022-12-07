# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calOuWKEY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtWebEngineWidgets import QWebEngineView
import os
import sys
THIS_DIR = os.path.dirname(__file__)
CODE_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'ui'))
sys.path.append(CODE_DIR)
import resource_rc

class Ui_main_ui(object):
    def setupUi(self, main_ui):
        if not main_ui.objectName():
            main_ui.setObjectName(u"main_ui")
        main_ui.resize(950, 550)
        main_ui.setMinimumSize(QSize(950, 550))
        self.horizontalLayout_3 = QHBoxLayout(main_ui)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.root_frm = QFrame(main_ui)
        self.root_frm.setObjectName(u"root_frm")
        self.root_frm.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.root_frm.setFrameShape(QFrame.StyledPanel)
        self.root_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.root_frm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_title_bar = QFrame(self.root_frm)
        self.top_title_bar.setObjectName(u"top_title_bar")
        self.top_title_bar.setMinimumSize(QSize(0, 50))
        self.top_title_bar.setMaximumSize(QSize(16777215, 50))
        self.top_title_bar.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border	:none;\n"
"\n"
"\n"
"}")
        self.top_title_bar.setFrameShape(QFrame.NoFrame)
        self.top_title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.top_title_bar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_left_spacer_2 = QFrame(self.frame_4)
        self.title_bar_left_spacer_2.setObjectName(u"title_bar_left_spacer_2")
        self.title_bar_left_spacer_2.setMaximumSize(QSize(65, 16777215))
        self.title_bar_left_spacer_2.setStyleSheet(u"border:none;")
        self.title_bar_left_spacer_2.setFrameShape(QFrame.StyledPanel)
        self.title_bar_left_spacer_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.title_bar_left_spacer_2)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.title_bar_left_spacer_2)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(58, 0))
        self.home_btn.setMaximumSize(QSize(49, 50))
        self.home_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-image: url(:/image/style/btn.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}")

        self.horizontalLayout_23.addWidget(self.home_btn)

        self.line_3 = QFrame(self.title_bar_left_spacer_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setWindowModality(Qt.ApplicationModal)
        self.line_3.setMinimumSize(QSize(1, 2))
        self.line_3.setMaximumSize(QSize(1, 40))
        self.line_3.setStyleSheet(u"border:none;\n"
"\n"
"background-color: rgb(116, 125, 140);\n"
"")
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.VLine)

        self.horizontalLayout_23.addWidget(self.line_3)


        self.horizontalLayout_2.addWidget(self.title_bar_left_spacer_2)


        self.horizontalLayout.addWidget(self.frame_4)

        self.horizontalSpacer = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_23 = QFrame(self.top_title_bar)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.title_lbl = QLabel(self.frame_23)
        self.title_lbl.setObjectName(u"title_lbl")
        font = QFont()
        font.setFamily(u"Poppins SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_lbl.setFont(font)

        self.horizontalLayout_26.addWidget(self.title_lbl)


        self.horizontalLayout.addWidget(self.frame_23)

        self.horizontalSpacer_2 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_22 = QFrame(self.top_title_bar)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.title_btn_container_2 = QFrame(self.frame_22)
        self.title_btn_container_2.setObjectName(u"title_btn_container_2")
        self.title_btn_container_2.setMinimumSize(QSize(0, 0))
        self.title_btn_container_2.setStyleSheet(u"border:none;")
        self.title_btn_container_2.setFrameShape(QFrame.StyledPanel)
        self.title_btn_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.title_btn_container_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.ful_scrn_btn = QPushButton(self.title_btn_container_2)
        self.ful_scrn_btn.setObjectName(u"ful_scrn_btn")
        self.ful_scrn_btn.setMaximumSize(QSize(20, 20))
        self.ful_scrn_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-image:url(\"C:/Users/Dilhara/Desktop/New UI/new ui/ful.png\");\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	border:1px solid;\n"
"	border-radius:7px;\n"
"	border-color: rgb(69, 170, 242);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.ful_scrn_btn)

        self.minimize_btn = QPushButton(self.title_btn_container_2)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMaximumSize(QSize(15, 15))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	\n"
"	background-color: rgb(38, 222, 129);\n"
"	border-color: rgb(38, 222, 129);\n"
"	border-radius:7px;\n"
"\n"
"}")

        self.horizontalLayout_24.addWidget(self.minimize_btn)

        self.maxmize_btn = QPushButton(self.title_btn_container_2)
        self.maxmize_btn.setObjectName(u"maxmize_btn")
        self.maxmize_btn.setMaximumSize(QSize(15, 15))
        self.maxmize_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	background-color: rgb(69, 170, 242);\n"
"	border-color: rgb(69, 170, 242);\n"
"	border-radius:7px;\n"
"\n"
"}")

        self.horizontalLayout_24.addWidget(self.maxmize_btn)

        self.close_btn = QPushButton(self.title_btn_container_2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(15, 15))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border:1px solid;\n"
"	background-color: rgb(235, 59, 90);\n"
"	border-color: rgb(235, 59, 90);\n"
"	border-radius:7px;\n"
"\n"
"}")

        self.horizontalLayout_24.addWidget(self.close_btn)


        self.horizontalLayout_25.addWidget(self.title_btn_container_2)


        self.horizontalLayout.addWidget(self.frame_22)


        self.verticalLayout.addWidget(self.top_title_bar)

        self.middle_frm = QFrame(self.root_frm)
        self.middle_frm.setObjectName(u"middle_frm")
        self.middle_frm.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"background-color:none;\n"
"\n"
"\n"
"}")
        self.middle_frm.setFrameShape(QFrame.StyledPanel)
        self.middle_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.middle_frm)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_container = QFrame(self.middle_frm)
        self.btn_container.setObjectName(u"btn_container")
        self.btn_container.setMinimumSize(QSize(0, 60))
        self.btn_container.setMaximumSize(QSize(60, 16777215))
        self.btn_container.setStyleSheet(u"QFrame{\n"
"\n"
"border:none;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.btn_container.setFrameShape(QFrame.NoFrame)
        self.btn_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.btn_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.top_btn_container = QFrame(self.btn_container)
        self.top_btn_container.setObjectName(u"top_btn_container")
        self.top_btn_container.setStyleSheet(u"border:none;")
        self.top_btn_container.setFrameShape(QFrame.NoFrame)
        self.top_btn_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.top_btn_container)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.chap_btn = QPushButton(self.top_btn_container)
        self.chap_btn.setObjectName(u"chap_btn")
        self.chap_btn.setMinimumSize(QSize(60, 50))
        self.chap_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/image/style/cat.png);\n"
"\n"
"	\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid;\n"
"	\n"
"	\n"
"	border-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(50, 117, 235, 255), stop:1 rgba(0, 142, 190, 255));\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")

        self.verticalLayout_5.addWidget(self.chap_btn)

        self.assest_btn = QPushButton(self.top_btn_container)
        self.assest_btn.setObjectName(u"assest_btn")
        self.assest_btn.setMinimumSize(QSize(60, 50))
        self.assest_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/bag.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid;\n"
"	\n"
"	\n"
"	border-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(50, 117, 235, 255), stop:1 rgba(0, 142, 190, 255));\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")

        self.verticalLayout_5.addWidget(self.assest_btn)

        self.about_btn = QPushButton(self.top_btn_container)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(60, 50))
        self.about_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/card.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid;\n"
"	\n"
"	\n"
"	border-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(50, 117, 235, 255), stop:1 rgba(0, 142, 190, 255));\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")

        self.verticalLayout_5.addWidget(self.about_btn)

        self.tool_btn = QPushButton(self.top_btn_container)
        self.tool_btn.setObjectName(u"tool_btn")
        self.tool_btn.setMinimumSize(QSize(60, 50))
        self.tool_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/set.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid;\n"
"	\n"
"	\n"
"	border-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(50, 117, 235, 255), stop:1 rgba(0, 142, 190, 255));\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")

        self.verticalLayout_5.addWidget(self.tool_btn)


        self.verticalLayout_4.addWidget(self.top_btn_container, 0, Qt.AlignTop)

        self.frame_21 = QFrame(self.btn_container)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_21)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.play_lst_btn = QPushButton(self.frame_21)
        self.play_lst_btn.setObjectName(u"play_lst_btn")
        self.play_lst_btn.setMinimumSize(QSize(60, 50))
        self.play_lst_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/play_lst.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid;\n"
"	\n"
"	\n"
"	border-color: rgb(0, 255, 225);\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")

        self.verticalLayout_22.addWidget(self.play_lst_btn)


        self.verticalLayout_4.addWidget(self.frame_21)

        self.bottom_btn_container = QFrame(self.btn_container)
        self.bottom_btn_container.setObjectName(u"bottom_btn_container")
        self.bottom_btn_container.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(5)
        self.bottom_btn_container.setFont(font1)
        self.bottom_btn_container.setStyleSheet(u"border:none;")
        self.bottom_btn_container.setFrameShape(QFrame.NoFrame)
        self.bottom_btn_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bottom_btn_container)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.bottom_btn_container)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(60, 0))
        self.line_2.setMaximumSize(QSize(0, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(130, 130, 130);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.ext_btn = QPushButton(self.bottom_btn_container)
        self.ext_btn.setObjectName(u"ext_btn")
        self.ext_btn.setMinimumSize(QSize(60, 50))
        self.ext_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/ext.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid;\n"
"	\n"
"	\n"
"	border-color: rgb(255, 0, 102);\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")

        self.verticalLayout_6.addWidget(self.ext_btn)


        self.verticalLayout_4.addWidget(self.bottom_btn_container, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.btn_container)

        self.frame_7 = QFrame(self.middle_frm)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_8)
        self.pages.setObjectName(u"pages")
        self.pages.setEnabled(True)
        self.player = QWidget()
        self.player.setObjectName(u"player")
        self.verticalLayout_3 = QVBoxLayout(self.player)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.player_window = QFrame(self.player)
        self.player_window.setObjectName(u"player_window")
        self.player_window.setFrameShape(QFrame.StyledPanel)
        self.player_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.player_window)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.play_list = QFrame(self.player_window)
        self.play_list.setObjectName(u"play_list")
        self.play_list.setMaximumSize(QSize(150, 16777215))
        self.play_list.setFrameShape(QFrame.StyledPanel)
        self.play_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.play_list)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.play_list_wid = QListWidget(self.play_list)
        self.play_list_wid.setObjectName(u"play_list_wid")

        self.verticalLayout_23.addWidget(self.play_list_wid)


        self.horizontalLayout_11.addWidget(self.play_list)

        self.player_frm = QFrame(self.player_window)
        self.player_frm.setObjectName(u"player_frm")
        self.player_frm.setMinimumSize(QSize(101, 101))
        self.player_frm.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.player_frm)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget = QVideoWidget(self.player_frm)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(18, 18, 26);")

        self.horizontalLayout_8.addWidget(self.widget)


        self.horizontalLayout_11.addWidget(self.player_frm)


        self.verticalLayout_3.addWidget(self.player_window)

        self.frame_3 = QFrame(self.player)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_3)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.player_btn_container_2 = QFrame(self.frame_3)
        self.player_btn_container_2.setObjectName(u"player_btn_container_2")
        self.player_btn_container_2.setMaximumSize(QSize(16777215, 20))
        self.player_btn_container_2.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:14px;\n"
"\n"
"}")
        self.player_btn_container_2.setFrameShape(QFrame.StyledPanel)
        self.player_btn_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.player_btn_container_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.changed_lenth_lbl = QLabel(self.player_btn_container_2)
        self.changed_lenth_lbl.setObjectName(u"changed_lenth_lbl")

        self.horizontalLayout_14.addWidget(self.changed_lenth_lbl)

        self.player_slider = QSlider(self.player_btn_container_2)
        self.player_slider.setObjectName(u"player_slider")
        self.player_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bdbdbd;\n"
"	background-color: rgb(189, 189, 189);\n"
"background: white;\n"
"height: 5px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background-color: qlineargradient(spread:pad, x1:0.6645, y1:0.693, x2:0, y2:0, stop:0 rgba(118, 75, 162, 255), stop:0.704545 rgba(102, 126, 234, 255), stop:1 rgba(102, 126, 234, 255));\n"
"\n"
"border: 1px solid #bdbdbd;\n"
"height: 10px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 8px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
""
                        "background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.player_slider.setValue(50)
        self.player_slider.setTracking(False)
        self.player_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.player_slider)

        self.p_right_btn_container_2 = QFrame(self.player_btn_container_2)
        self.p_right_btn_container_2.setObjectName(u"p_right_btn_container_2")
        self.p_right_btn_container_2.setFrameShape(QFrame.StyledPanel)
        self.p_right_btn_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.p_right_btn_container_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.total_lenth_lbl = QLabel(self.p_right_btn_container_2)
        self.total_lenth_lbl.setObjectName(u"total_lenth_lbl")

        self.horizontalLayout_17.addWidget(self.total_lenth_lbl)


        self.horizontalLayout_14.addWidget(self.p_right_btn_container_2)


        self.verticalLayout_25.addWidget(self.player_btn_container_2)

        self.player_btn_container = QFrame(self.frame_3)
        self.player_btn_container.setObjectName(u"player_btn_container")
        self.player_btn_container.setMinimumSize(QSize(0, 0))
        self.player_btn_container.setMaximumSize(QSize(16777215, 50))
        self.player_btn_container.setFrameShape(QFrame.StyledPanel)
        self.player_btn_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.player_btn_container)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.player_btn_container)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.player_ful_scrn_btn = QPushButton(self.frame_9)
        self.player_ful_scrn_btn.setObjectName(u"player_ful_scrn_btn")
        self.player_ful_scrn_btn.setMinimumSize(QSize(40, 40))
        self.player_ful_scrn_btn.setMaximumSize(QSize(40, 40))
        self.player_ful_scrn_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-image: url(:/image/style/fulscr.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(46, 204, 113);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_12.addWidget(self.player_ful_scrn_btn)

        self.player_status_lbl = QLabel(self.frame_9)
        self.player_status_lbl.setObjectName(u"player_status_lbl")
        self.player_status_lbl.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_12.addWidget(self.player_status_lbl)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.player_btn_container)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.p_left_btn_container_2 = QFrame(self.frame_5)
        self.p_left_btn_container_2.setObjectName(u"p_left_btn_container_2")
        self.p_left_btn_container_2.setMaximumSize(QSize(16777215, 50))
        self.p_left_btn_container_2.setFrameShape(QFrame.StyledPanel)
        self.p_left_btn_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.p_left_btn_container_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)

        self.prev_btn = QPushButton(self.p_left_btn_container_2)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setMinimumSize(QSize(40, 40))
        self.prev_btn.setMaximumSize(QSize(40, 40))
        self.prev_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/image/style/prev.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(46, 204, 113);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_18.addWidget(self.prev_btn)

        self.play_btn = QPushButton(self.p_left_btn_container_2)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMinimumSize(QSize(40, 40))
        self.play_btn.setMaximumSize(QSize(50, 40))
        self.play_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/play.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(46, 204, 113);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_18.addWidget(self.play_btn)

        self.next_btn = QPushButton(self.p_left_btn_container_2)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(40, 40))
        self.next_btn.setMaximumSize(QSize(40, 40))
        self.next_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-image: url(:/image/style/nex.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(46, 204, 113);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_18.addWidget(self.next_btn)

        self.stop_btn = QPushButton(self.p_left_btn_container_2)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(30, 30))
        self.stop_btn.setMaximumSize(QSize(30, 40))
        self.stop_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/image/style/stop.png);\n"
"\n"
"	background-image:url(\"C:/Users/Dilhara/Desktop/New UI/new ui/stop.png\");\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(46, 204, 113);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_18.addWidget(self.stop_btn)


        self.horizontalLayout_10.addWidget(self.p_left_btn_container_2)


        self.horizontalLayout_9.addWidget(self.frame_5)

        self.frame_30 = QFrame(self.player_btn_container)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.pushButton = QPushButton(self.frame_30)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(40, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton)

        self.vol_btn = QPushButton(self.frame_30)
        self.vol_btn.setObjectName(u"vol_btn")
        self.vol_btn.setMinimumSize(QSize(40, 40))
        self.vol_btn.setMaximumSize(QSize(40, 40))
        self.vol_btn.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/image/style/spkr.png);\n"
"\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(46, 204, 113);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.vol_btn)

        self.vol_slider = QSlider(self.frame_30)
        self.vol_slider.setObjectName(u"vol_slider")
        self.vol_slider.setMinimumSize(QSize(50, 0))
        self.vol_slider.setMaximumSize(QSize(100, 16777215))
        self.vol_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 3px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.6645, y1:0.693, x2:0, y2:0, stop:0 rgba(118, 75, 162, 255), stop:0.704545 rgba(102, 126, 234, 255), stop:1 rgba(102, 126, 234, 255));\n"
"height: 10px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 8px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add"
                        "-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.vol_slider.setMaximum(100)
        self.vol_slider.setSingleStep(1)
        self.vol_slider.setValue(0)
        self.vol_slider.setTracking(False)
        self.vol_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.vol_slider)


        self.horizontalLayout_9.addWidget(self.frame_30)


        self.verticalLayout_25.addWidget(self.player_btn_container)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.pages.addWidget(self.player)
        self.chaptor_complete_page = QWidget()
        self.chaptor_complete_page.setObjectName(u"chaptor_complete_page")
        self.pages.addWidget(self.chaptor_complete_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.horizontalLayout_27 = QHBoxLayout(self.home_page)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.home_frm = QFrame(self.home_page)
        self.home_frm.setObjectName(u"home_frm")
        self.home_frm.setFrameShape(QFrame.StyledPanel)
        self.home_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.home_frm)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.home_conten_lbl = QLabel(self.home_frm)
        self.home_conten_lbl.setObjectName(u"home_conten_lbl")
        self.home_conten_lbl.setStyleSheet(u"QLabel{\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"}")

        self.horizontalLayout_28.addWidget(self.home_conten_lbl)


        self.horizontalLayout_27.addWidget(self.home_frm)

        self.pages.addWidget(self.home_page)
        self.product_page = QWidget()
        self.product_page.setObjectName(u"product_page")
        self.horizontalLayout_5 = QHBoxLayout(self.product_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_24 = QFrame(self.product_page)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_2 = QWebEngineView(self.frame_24)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_6.addWidget(self.widget_2)


        self.horizontalLayout_5.addWidget(self.frame_24)

        self.pages.addWidget(self.product_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.horizontalLayout_15 = QHBoxLayout(self.about_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.chapter_root_2 = QFrame(self.about_page)
        self.chapter_root_2.setObjectName(u"chapter_root_2")
        self.chapter_root_2.setStyleSheet(u"QFrame{\n"
"border-radius:0;\n"
"}")
        self.chapter_root_2.setFrameShape(QFrame.StyledPanel)
        self.chapter_root_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.chapter_root_2)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.chapter_root_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(400, 0))
        self.frame_34.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(241, 243, 245);\n"
"border-radius:0px;\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(500, 230))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_35)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_36)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 230))
        self.frame_33.setStyleSheet(u"background-color: rgb(241, 243, 245);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_33)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.about_top_frm = QFrame(self.frame_33)
        self.about_top_frm.setObjectName(u"about_top_frm")
        self.about_top_frm.setMinimumSize(QSize(0, 200))
        self.about_top_frm.setFrameShape(QFrame.StyledPanel)
        self.about_top_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.about_top_frm)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.about_top_frm)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 50))
        self.frame_37.setMaximumSize(QSize(16777215, 50))
        self.frame_37.setStyleSheet(u"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius:5px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-top:none;\n"
"border-left:none;\n"
"border-right:none;\n"
"border-bottom-color: rgb(240, 240, 240);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(5, 0, 5, 0)
        self.home_btn_2 = QPushButton(self.frame_37)
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

        self.horizontalLayout_38.addWidget(self.home_btn_2)

        self.label_2 = QLabel(self.frame_37)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border:none;")

        self.horizontalLayout_38.addWidget(self.label_2)


        self.verticalLayout_30.addWidget(self.frame_37)

        self.frame_32 = QFrame(self.about_top_frm)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"border-radius:6px;\n"
"border-top-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(30, 20, -1, 20)
        self.plainTextEdit = QPlainTextEdit(self.frame_32)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font3 = QFont()
        font3.setFamily(u"Poppins Light")
        font3.setPointSize(8)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"color:#5f6368;")

        self.horizontalLayout_39.addWidget(self.plainTextEdit)


        self.verticalLayout_30.addWidget(self.frame_32)


        self.verticalLayout_27.addWidget(self.about_top_frm)


        self.verticalLayout_26.addWidget(self.frame_33)

        self.frame_40 = QFrame(self.frame_36)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgb(241, 243, 245);")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_40)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.about_bottom_frm = QFrame(self.frame_40)
        self.about_bottom_frm.setObjectName(u"about_bottom_frm")
        self.about_bottom_frm.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(255, 255, 255);")
        self.about_bottom_frm.setFrameShape(QFrame.StyledPanel)
        self.about_bottom_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.about_bottom_frm)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.about_bottom_frm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 726, 184))
        self.horizontalLayout_41 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(15, 0, 0, 0)
        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        font4 = QFont()
        font4.setFamily(u"Poppins Light")
        self.plainTextEdit_2.setFont(font4)
        self.plainTextEdit_2.setStyleSheet(u"color:#5f6368;")

        self.horizontalLayout_41.addWidget(self.plainTextEdit_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_40.addWidget(self.scrollArea)


        self.verticalLayout_31.addWidget(self.about_bottom_frm)


        self.verticalLayout_26.addWidget(self.frame_40)


        self.verticalLayout_29.addWidget(self.frame_36)


        self.horizontalLayout_37.addWidget(self.frame_35)

        self.about_social_frm = QFrame(self.frame_34)
        self.about_social_frm.setObjectName(u"about_social_frm")
        self.about_social_frm.setMaximumSize(QSize(60, 16777215))
        self.about_social_frm.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.about_social_frm.setFrameShape(QFrame.StyledPanel)
        self.about_social_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.about_social_frm)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.about_fb_btn = QPushButton(self.about_social_frm)
        self.about_fb_btn.setObjectName(u"about_fb_btn")
        self.about_fb_btn.setMinimumSize(QSize(50, 50))
        self.about_fb_btn.setMaximumSize(QSize(50, 50))
        self.about_fb_btn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-image: url(:/image/style/fb.png);\n"
"}\n"
"QPushButton:hover{\n"
"	background-image: url(:/image/style/fb-hover.png);\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.about_fb_btn)

        self.about_wp_btn = QPushButton(self.about_social_frm)
        self.about_wp_btn.setObjectName(u"about_wp_btn")
        self.about_wp_btn.setMinimumSize(QSize(50, 50))
        self.about_wp_btn.setMaximumSize(QSize(50, 50))
        self.about_wp_btn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"	background-image: url(:/image/style/whatsapp.png);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/image/style/whatsapp-hover.png);\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.about_wp_btn)

        self.about_call_btn = QPushButton(self.about_social_frm)
        self.about_call_btn.setObjectName(u"about_call_btn")
        self.about_call_btn.setMinimumSize(QSize(50, 50))
        self.about_call_btn.setMaximumSize(QSize(50, 50))
        self.about_call_btn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"	background-image: url(:/image/style/call.png);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/image/style/call-hover.png);\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.about_call_btn)

        self.about_mail_btn = QPushButton(self.about_social_frm)
        self.about_mail_btn.setObjectName(u"about_mail_btn")
        self.about_mail_btn.setMinimumSize(QSize(50, 50))
        self.about_mail_btn.setMaximumSize(QSize(50, 50))
        self.about_mail_btn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"	background-image: url(:/image/style/mail.png);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-image: url(:/image/style/mail-hover.png);\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.about_mail_btn)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_6)


        self.horizontalLayout_37.addWidget(self.about_social_frm)


        self.horizontalLayout_35.addWidget(self.frame_34)


        self.horizontalLayout_15.addWidget(self.chapter_root_2)

        self.pages.addWidget(self.about_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.pages.addWidget(self.settings_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.horizontalLayout_16 = QHBoxLayout(self.user_page)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_38 = QFrame(self.user_page)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"QFrame{\n"
"\n"
"	background-image:url(\":/home_content/style/login.jpg\");\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"border-style:none;\n"
"\n"
"\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(200, 200))
        self.frame_39.setMaximumSize(QSize(200, 200))
        self.frame_39.setStyleSheet(u"background-color: rgb(152, 152, 152);")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_39)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 47, 13))

        self.horizontalLayout_36.addWidget(self.frame_39)


        self.horizontalLayout_16.addWidget(self.frame_38)

        self.pages.addWidget(self.user_page)
        self.category_page = QWidget()
        self.category_page.setObjectName(u"category_page")
        self.category_page.setMaximumSize(QSize(16777215, 16777215))
        self.category_page.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.category_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.frame = QFrame(self.category_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 220))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.cf1 = QFrame(self.frame)
        self.cf1.setObjectName(u"cf1")
        self.cf1.setMaximumSize(QSize(350, 225))
        self.cf1.setStyleSheet(u"QFrame{\n"
"border:1px solid;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(68, 129, 235, 255), stop:1 rgba(4, 190, 254, 255));\n"
"border-color:none;}\n"
"\n"
"QFrame:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(50, 117, 235, 255), stop:1 rgba(0, 142, 190, 255));\n"
"}")
        self.cf1.setFrameShape(QFrame.StyledPanel)
        self.cf1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.cf1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.c_btn1 = QPushButton(self.cf1)
        self.c_btn1.setObjectName(u"c_btn1")
        self.c_btn1.setMinimumSize(QSize(0, 150))
        font5 = QFont()
        font5.setFamily(u"0KDBOLIDDA")
        font5.setPointSize(21)
        self.c_btn1.setFont(font5)
        self.c_btn1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_13.addWidget(self.c_btn1)


        self.horizontalLayout_7.addWidget(self.cf1)

        self.cf2 = QFrame(self.frame)
        self.cf2.setObjectName(u"cf2")
        self.cf2.setMaximumSize(QSize(350, 225))
        self.cf2.setStyleSheet(u"QFrame{\n"
"border:1px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(0, 201, 255, 255), stop:1 rgba(146, 254, 157, 255));\n"
"border-radius:15px;\n"
"border-color:none;\n"
"\n"
"\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(0, 178, 226, 255), stop:1 rgba(76, 235, 92, 255));\n"
"}")
        self.cf2.setFrameShape(QFrame.StyledPanel)
        self.cf2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.cf2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.c_btn2 = QPushButton(self.cf2)
        self.c_btn2.setObjectName(u"c_btn2")
        self.c_btn2.setMinimumSize(QSize(0, 150))
        self.c_btn2.setFont(font5)
        self.c_btn2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_14.addWidget(self.c_btn2)


        self.horizontalLayout_7.addWidget(self.cf2)

        self.cf3 = QFrame(self.frame)
        self.cf3.setObjectName(u"cf3")
        self.cf3.setMaximumSize(QSize(350, 225))
        self.cf3.setStyleSheet(u"QFrame{\n"
"border:1px solid;\n"
"border-radius:15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.477682, y1:0.028, x2:0.534318, y2:1, stop:0 rgba(111, 134, 214, 255), stop:1 rgba(72, 198, 239, 255));\n"
"border-color:none;\n"
"\n"
"\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(18, 96, 232, 255), stop:1 rgba(3, 163, 217, 255));\n"
"}")
        self.cf3.setFrameShape(QFrame.StyledPanel)
        self.cf3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.cf3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.c_btn3 = QPushButton(self.cf3)
        self.c_btn3.setObjectName(u"c_btn3")
        self.c_btn3.setMinimumSize(QSize(0, 150))
        self.c_btn3.setFont(font5)
        self.c_btn3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_15.addWidget(self.c_btn3)


        self.horizontalLayout_7.addWidget(self.cf3)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.category_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 220))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setSpacing(15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(15, 15, 15, 15)
        self.cf4 = QFrame(self.frame_2)
        self.cf4.setObjectName(u"cf4")
        self.cf4.setMaximumSize(QSize(350, 225))
        self.cf4.setStyleSheet(u"QFrame{\n"
"border:1px solid;\n"
"border-radius:15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.471136, y1:0.028, x2:0.494, y2:1, stop:0 rgba(79, 172, 254, 255), stop:1 rgba(0, 242, 254, 255));\n"
"border-color:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(68, 129, 235, 255), stop:1 rgba(4, 190, 254, 255));\n"
"}")
        self.cf4.setFrameShape(QFrame.StyledPanel)
        self.cf4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.cf4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.c_btn4 = QPushButton(self.cf4)
        self.c_btn4.setObjectName(u"c_btn4")
        self.c_btn4.setMinimumSize(QSize(0, 100))
        self.c_btn4.setFont(font5)
        self.c_btn4.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.c_btn4)


        self.horizontalLayout_19.addWidget(self.cf4)

        self.cf5 = QFrame(self.frame_2)
        self.cf5.setObjectName(u"cf5")
        self.cf5.setMaximumSize(QSize(350, 225))
        self.cf5.setStyleSheet(u"QFrame{\n"
"border:1px solid;\n"
"border-radius:15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:0.0220455, x2:0.528, y2:1, stop:0 rgba(118, 75, 162, 255), stop:0.704545 rgba(102, 126, 234, 255), stop:1 rgba(102, 126, 234, 255));\n"
"border-color:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:0.0220455, x2:0.528, y2:1, stop:0 rgba(80, 0, 162, 255), stop:0.704545 rgba(71, 96, 210, 255), stop:1 rgba(92, 114, 212, 255));\n"
"}")
        self.cf5.setFrameShape(QFrame.StyledPanel)
        self.cf5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.cf5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.c_btn5 = QPushButton(self.cf5)
        self.c_btn5.setObjectName(u"c_btn5")
        self.c_btn5.setMinimumSize(QSize(0, 100))
        self.c_btn5.setFont(font5)
        self.c_btn5.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_18.addWidget(self.c_btn5)


        self.horizontalLayout_19.addWidget(self.cf5)

        self.cf6 = QFrame(self.frame_2)
        self.cf6.setObjectName(u"cf6")
        self.cf6.setMaximumSize(QSize(350, 225))
        self.cf6.setStyleSheet(u"QFrame{\n"
"border:1px solid;\n"
"border-radius:15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(155, 225, 93, 255), stop:1 rgba(0, 227, 174, 255));\n"
"border-color:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.506, y2:1, stop:0 rgba(117, 212, 33, 255), stop:1 rgba(0, 199, 153, 255));\n"
"}")
        self.cf6.setFrameShape(QFrame.StyledPanel)
        self.cf6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.cf6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.c_btn6 = QPushButton(self.cf6)
        self.c_btn6.setObjectName(u"c_btn6")
        self.c_btn6.setMinimumSize(QSize(0, 100))
        self.c_btn6.setFont(font5)
        self.c_btn6.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.c_btn6)


        self.horizontalLayout_19.addWidget(self.cf6)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.pages.addWidget(self.category_page)
        self.chapto_owerview = QWidget()
        self.chapto_owerview.setObjectName(u"chapto_owerview")
        self.horizontalLayout_20 = QHBoxLayout(self.chapto_owerview)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.chapter_root = QFrame(self.chapto_owerview)
        self.chapter_root.setObjectName(u"chapter_root")
        self.chapter_root.setStyleSheet(u"QFrame{\n"
"\n"
"border-radius:15px;\n"
"}")
        self.chapter_root.setFrameShape(QFrame.StyledPanel)
        self.chapter_root.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.chapter_root)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.chapter_root)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(175, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(233, 233, 233);\n"
"border-radius:15px;\n"
" border-top-right-radius: 0px;\n"
" border-bottom-right-radius: 0px;\n"
"border-left:none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamily(u"apex-a.pura-036")
        self.frame_10.setFont(font6)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setFamily(u"apex-a.pura-040")
        font7.setPointSize(18)
        self.label_5.setFont(font7)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_5)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.chapter_content_lst = QListWidget(self.frame_11)
        self.chapter_content_lst.setObjectName(u"chapter_content_lst")

        self.verticalLayout_9.addWidget(self.chapter_content_lst)


        self.verticalLayout_8.addWidget(self.frame_11)


        self.horizontalLayout_21.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.chapter_root)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(400, 0))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(247, 247, 247);\n"
"border-radius:0px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 230))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.chap_img = QFrame(self.frame_13)
        self.chap_img.setObjectName(u"chap_img")
        self.chap_img.setStyleSheet(u"QFrame{\n"
"\n"
"background-image: url(:/thumbnals/style/chp1.jpg);\n"
" background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.chap_img.setFrameShape(QFrame.StyledPanel)
        self.chap_img.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.chap_img)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 250))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 100))
        self.frame_15.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"	background-color: rgb(233, 233, 233);\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.chap_discription_lbl = QPlainTextEdit(self.frame_15)
        self.chap_discription_lbl.setObjectName(u"chap_discription_lbl")
        self.chap_discription_lbl.setReadOnly(True)

        self.verticalLayout_21.addWidget(self.chap_discription_lbl)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, -1, -1)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"	background-color: rgb(233, 233, 233);\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_30.addWidget(self.label_6)

        self.tot_vid_lbl = QLabel(self.frame_18)
        self.tot_vid_lbl.setObjectName(u"tot_vid_lbl")

        self.horizontalLayout_30.addWidget(self.tot_vid_lbl)


        self.verticalLayout_19.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"	background-color: rgb(233, 233, 233);\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_31.addWidget(self.label_8)

        self.tot_due_lbl = QLabel(self.frame_19)
        self.tot_due_lbl.setObjectName(u"tot_due_lbl")

        self.horizontalLayout_31.addWidget(self.tot_due_lbl)


        self.verticalLayout_19.addWidget(self.frame_19)


        self.horizontalLayout_29.addWidget(self.frame_17)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.886, y2:0.915, stop:0 rgba(202, 72, 152, 255), stop:0.909091 rgba(255, 75, 108, 255));\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.886, y2:0.915, stop:0 rgba(202, 40, 140, 255), stop:0.909091 rgba(255, 40, 79, 255));\n"
"}\n"
"\n"
"\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_25)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.chap_start_btn = QPushButton(self.frame_25)
        self.chap_start_btn.setObjectName(u"chap_start_btn")
        self.chap_start_btn.setMinimumSize(QSize(0, 60))
        self.chap_start_btn.setStyleSheet(u"QPushButton{\n"
"		background-image: url(:/image/style/big_play.png);\n"
" background-position: center;\n"
"    background-repeat: no-repeat;\n"
"background-color:none;\n"
"border:none;\n"
"\n"
"}")

        self.verticalLayout_20.addWidget(self.chap_start_btn)


        self.horizontalLayout_32.addWidget(self.frame_25)


        self.horizontalLayout_29.addWidget(self.frame_20)


        self.verticalLayout_11.addWidget(self.frame_16)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.horizontalLayout_21.addWidget(self.frame_12)

        self.frame_26 = QFrame(self.chapter_root)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(250, 0))
        self.frame_26.setMaximumSize(QSize(16777215, 16777215))
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0.0457727, y1:0.017, x2:1, y2:0.999, stop:0 rgba(57, 58, 68, 255), stop:1 rgba(23, 25, 54, 255));\n"
"border-radius:15;\n"
"\n"
"}")
        self.frame_26.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_26)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background:none;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.progress_bg = QFrame(self.frame_27)
        self.progress_bg.setObjectName(u"progress_bg")
        self.progress_bg.setMinimumSize(QSize(180, 180))
        self.progress_bg.setMaximumSize(QSize(180, 180))
        self.progress_bg.setStyleSheet(u"QFrame{\n"
"border-radius:90px;\n"
"	background-color: rgba(7, 15, 56, 120);\n"
"\n"
"}")
        self.progress_bg.setFrameShape(QFrame.StyledPanel)
        self.progress_bg.setFrameShadow(QFrame.Raised)
        self.circular_progress = QFrame(self.progress_bg)
        self.circular_progress.setObjectName(u"circular_progress")
        self.circular_progress.setGeometry(QRect(0, 0, 180, 180))
        self.circular_progress.setMinimumSize(QSize(180, 180))
        self.circular_progress.setMaximumSize(QSize(180, 180))
        self.circular_progress.setStyleSheet(u"QFrame{\n"
"\n"
" border-radius:90px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 157, 0), stop:0.75 rgba(32, 166, 255, 255));\n"
"}")
        self.circular_progress.setFrameShape(QFrame.StyledPanel)
        self.circular_progress.setFrameShadow(QFrame.Raised)
        self.frame_28 = QFrame(self.progress_bg)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(10, 10, 160, 160))
        self.frame_28.setMinimumSize(QSize(160, 160))
        self.frame_28.setMaximumSize(QSize(160, 160))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"border-radius:80;\n"
"	background-color: rgb(77, 77, 127);\n"
"\n"
"\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_28)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(21, 21, 116, 60))
        self.label_7.setMinimumSize(QSize(0, 60))
        font8 = QFont()
        font8.setFamily(u"Nirmala UI Semilight")
        font8.setPointSize(10)
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"background:none;\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame_28)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 70, 53, 80))
        self.label_9.setMinimumSize(QSize(0, 80))
        font9 = QFont()
        font9.setFamily(u"Source Sans Pro Light")
        font9.setPointSize(40)
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"background:none;\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_33.addWidget(self.progress_bg)


        self.verticalLayout_24.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setStyleSheet(u"background:none;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_29)


        self.horizontalLayout_21.addWidget(self.frame_26)


        self.horizontalLayout_20.addWidget(self.chapter_root)

        self.pages.addWidget(self.chapto_owerview)

        self.horizontalLayout_34.addWidget(self.pages)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.middle_frm)


        self.horizontalLayout_3.addWidget(self.root_frm)


        self.retranslateUi(main_ui)

        self.pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(main_ui)
    # setupUi

    def retranslateUi(self, main_ui):
        main_ui.setWindowTitle(QCoreApplication.translate("main_ui", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("main_ui", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText("")
        self.title_lbl.setText(QCoreApplication.translate("main_ui", u"Home", None))
#if QT_CONFIG(tooltip)
        self.ful_scrn_btn.setToolTip(QCoreApplication.translate("main_ui", u"Ful screen", None))
#endif // QT_CONFIG(tooltip)
        self.ful_scrn_btn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("main_ui", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maxmize_btn.setToolTip(QCoreApplication.translate("main_ui", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxmize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("main_ui", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
#if QT_CONFIG(tooltip)
        self.chap_btn.setToolTip(QCoreApplication.translate("main_ui", u"<html><head/><body><p>Chapters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chap_btn.setText("")
#if QT_CONFIG(tooltip)
        self.assest_btn.setToolTip(QCoreApplication.translate("main_ui", u"Our products", None))
#endif // QT_CONFIG(tooltip)
        self.assest_btn.setText("")
#if QT_CONFIG(tooltip)
        self.about_btn.setToolTip(QCoreApplication.translate("main_ui", u"About us", None))
#endif // QT_CONFIG(tooltip)
        self.about_btn.setText("")
#if QT_CONFIG(tooltip)
        self.tool_btn.setToolTip(QCoreApplication.translate("main_ui", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.tool_btn.setText("")
#if QT_CONFIG(tooltip)
        self.play_lst_btn.setToolTip(QCoreApplication.translate("main_ui", u"Currently playing list", None))
#endif // QT_CONFIG(tooltip)
        self.play_lst_btn.setText("")
#if QT_CONFIG(tooltip)
        self.ext_btn.setToolTip(QCoreApplication.translate("main_ui", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.ext_btn.setText("")
        self.changed_lenth_lbl.setText(QCoreApplication.translate("main_ui", u"00.00.00", None))
        self.total_lenth_lbl.setText(QCoreApplication.translate("main_ui", u"00.00.00", None))
        self.player_ful_scrn_btn.setText("")
        self.player_status_lbl.setText(QCoreApplication.translate("main_ui", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.prev_btn.setToolTip(QCoreApplication.translate("main_ui", u"backward", None))
#endif // QT_CONFIG(tooltip)
        self.prev_btn.setText("")
#if QT_CONFIG(tooltip)
        self.play_btn.setToolTip(QCoreApplication.translate("main_ui", u"Play/Pause", None))
#endif // QT_CONFIG(tooltip)
        self.play_btn.setText("")
#if QT_CONFIG(tooltip)
        self.next_btn.setToolTip(QCoreApplication.translate("main_ui", u"Foward", None))
#endif // QT_CONFIG(tooltip)
        self.next_btn.setText("")
#if QT_CONFIG(tooltip)
        self.stop_btn.setToolTip(QCoreApplication.translate("main_ui", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.stop_btn.setText("")
        self.pushButton.setText("")
        self.vol_btn.setText("")
        self.home_conten_lbl.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn_2.setToolTip(QCoreApplication.translate("main_ui", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn_2.setText("")
        self.label_2.setText(QCoreApplication.translate("main_ui", u"Class@home", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("main_ui", u"Version 1.0.0 Mahasona : (64-bit)\n"
"Author : CodeLab IT Solutions\n"
"Partnership : TRSoftway", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("main_ui", u"\n"
"Class@home\n"
"Copyright \u00a9 2022 The Class@home Authors. All rights reserved.\n"
"\n"
"Class@home is made available to you under the  License of CodeLab IT Solutions and this a closed source software and strictly prohobited to re-distibute and allkinde of edits. Read Eula and instructions before use this software.", None))
        self.about_fb_btn.setText("")
        self.about_wp_btn.setText("")
        self.about_call_btn.setText("")
        self.about_mail_btn.setText("")
        self.label.setText(QCoreApplication.translate("main_ui", u"TextLabel", None))
        self.c_btn1.setText(QCoreApplication.translate("main_ui", u"m<uq m\u00df\u00c9f\u00feoh ", None))
        self.c_btn2.setText(QCoreApplication.translate("main_ui", u"fojeks m\u00df\u00c9f\u00feoh ", None))
        self.c_btn3.setText(QCoreApplication.translate("main_ui", u";=kajk m\u00df\u00c9f\u00feoh ", None))
        self.c_btn4.setText("")
        self.c_btn5.setText("")
        self.c_btn6.setText("")
        self.label_5.setText(QCoreApplication.translate("main_ui", u"mdv\u00ef ud,dj", None))
        self.chap_discription_lbl.setPlainText("")
        self.label_6.setText(QCoreApplication.translate("main_ui", u"Total Videos    :", None))
        self.tot_vid_lbl.setText("")
        self.label_8.setText(QCoreApplication.translate("main_ui", u"Total Duration :", None))
        self.tot_due_lbl.setText("")
        self.chap_start_btn.setText("")
        self.label_7.setText(QCoreApplication.translate("main_ui", u"<strong>Chapter</Strong> Completed", None))
        self.label_9.setText(QCoreApplication.translate("main_ui", u"<html><head/><body><p>0<span style=\" vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi

