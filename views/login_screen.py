# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screenTVXyad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(1319, 809)
        LoginScreen.setAutoFillBackground(False)
        LoginScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(LoginScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(LoginScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.containerScreen.setStyleSheet(u"background: #FFFFFF	")
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.containerMain = QWidget(self.containerScreen)
        self.containerMain.setObjectName(u"containerMain")
        self.verticalLayout_4 = QVBoxLayout(self.containerMain)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblFqcs = QLabel(self.containerMain)
        self.lblFqcs.setObjectName(u"lblFqcs")
        font = QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lblFqcs.setFont(font)
        self.lblFqcs.setMargin(25)

        self.verticalLayout_4.addWidget(self.lblFqcs, 0, Qt.AlignHCenter)

        self.containerInfoSection = QWidget(self.containerMain)
        self.containerInfoSection.setObjectName(u"containerInfoSection")
        self.containerInfoSection.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.containerInfoSection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.containerInfoSection)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout.addWidget(self.widget)

        self.containerAccPass = QWidget(self.containerInfoSection)
        self.containerAccPass.setObjectName(u"containerAccPass")
        self.verticalLayout_2 = QVBoxLayout(self.containerAccPass)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupAcc = QGroupBox(self.containerAccPass)
        self.groupAcc.setObjectName(u"groupAcc")
        font1 = QFont()
        font1.setPointSize(13)
        self.groupAcc.setFont(font1)
        self.verticalLayout_7 = QVBoxLayout(self.groupAcc)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(30, 0, 30, 0)
        self.inpAcc = QLineEdit(self.groupAcc)
        self.inpAcc.setObjectName(u"inpAcc")

        self.verticalLayout_7.addWidget(self.inpAcc)


        self.verticalLayout_2.addWidget(self.groupAcc)

        self.groupPass = QGroupBox(self.containerAccPass)
        self.groupPass.setObjectName(u"groupPass")
        self.groupPass.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.groupPass)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(30, 0, 30, 0)
        self.inpPass = QLineEdit(self.groupPass)
        self.inpPass.setObjectName(u"inpPass")
        self.inpPass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_8.addWidget(self.inpPass)


        self.verticalLayout_2.addWidget(self.groupPass)


        self.horizontalLayout.addWidget(self.containerAccPass)

        self.widget_3 = QWidget(self.containerInfoSection)
        self.widget_3.setObjectName(u"widget_3")

        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.containerInfoSection)

        self.containerButtons = QWidget(self.containerMain)
        self.containerButtons.setObjectName(u"containerButtons")
        self.verticalLayout_3 = QVBoxLayout(self.containerButtons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(500, -1, 500, -1)
        self.btnLogin = QPushButton(self.containerButtons)
        self.btnLogin.setObjectName(u"btnLogin")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnLogin.setFont(font2)
        self.btnLogin.setStyleSheet(u"background-color: grey; height: 45;")

        self.verticalLayout_3.addWidget(self.btnLogin)


        self.verticalLayout_4.addWidget(self.containerButtons, 0, Qt.AlignTop)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 5)

        self.gridLayout.addWidget(self.containerMain, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.containerScreen)

        self.verticalLayout.setStretch(0, 8)

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"Form", None))
        self.lblFqcs.setText(QCoreApplication.translate("LoginScreen", u"FQCS", None))
        self.groupAcc.setTitle(QCoreApplication.translate("LoginScreen", u"ACCOUNT", None))
        self.inpAcc.setInputMask("")
        self.inpAcc.setText("")
        self.inpAcc.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Input something", None))
        self.groupPass.setTitle(QCoreApplication.translate("LoginScreen", u"PASSWORD", None))
        self.inpPass.setInputMask("")
        self.inpPass.setText("")
        self.inpPass.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Input something", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginScreen", u"LOGIN", None))
    # retranslateUi

