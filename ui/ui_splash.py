# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashOkDfok.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_splash_window(object):
    def setupUi(self, splash_window):
        if not splash_window.objectName():
            splash_window.setObjectName(u"splash_window")
        splash_window.resize(680, 400)
        splash_window.setMaximumSize(QSize(680, 400))
        self.centralwidget = QWidget(splash_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splash_back = QFrame(self.centralwidget)
        self.splash_back.setObjectName(u"splash_back")
        self.splash_back.setStyleSheet(u"QFrame{\n"
"\n"
"	background-image:url(\"J:/New UI/Splash/splash1.jpg\");\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"border-style:none;\n"
"	border-radius:20px;\n"
"\n"
"}")
        self.splash_back.setFrameShape(QFrame.StyledPanel)
        self.splash_back.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.splash_back)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 270, 511, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"	\n"
"	background-color: rgb(202, 202, 202);\n"
"	border: 1px solid;\n"
"border-radius:8px;\n"
"border-color:none;\n"
"text-align:center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"\n"
"	border-radius:8px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.000318182, y1:0.545, x2:0.966227, y2:0.489, stop:0 rgba(68, 129, 235, 255), stop:1 rgba(4, 190, 254, 255));\n"
"\n"
"}")
        self.progressBar.setValue(24)
        self.prog_lbl = QLabel(self.splash_back)
        self.prog_lbl.setObjectName(u"prog_lbl")
        self.prog_lbl.setGeometry(QRect(210, 240, 281, 20))
        self.prog_lbl.setStyleSheet(u"QLabel{\n"
"	color: rgb(35, 51, 64);\n"
"\n"
"}")
        self.prog_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.splash_back)

        splash_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(splash_window)

        QMetaObject.connectSlotsByName(splash_window)
    # setupUi

    def retranslateUi(self, splash_window):
        splash_window.setWindowTitle(QCoreApplication.translate("splash_window", u"MainWindow", None))
        self.prog_lbl.setText(QCoreApplication.translate("splash_window", u"Loading...", None))
    # retranslateUi

