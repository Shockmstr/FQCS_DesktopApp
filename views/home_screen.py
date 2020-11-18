# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_screenPcsbpz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        if not HomeScreen.objectName():
            HomeScreen.setObjectName(u"HomeScreen")
        HomeScreen.resize(1319, 809)
        HomeScreen.setAutoFillBackground(False)
        HomeScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(HomeScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(HomeScreen)
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
        self.horizontalLayout = QHBoxLayout(self.containerInfoSection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(300, -1, 300, -1)
        self.containerFrame = QWidget(self.containerInfoSection)
        self.containerFrame.setObjectName(u"containerFrame")
        self.containerFrame.setLayoutDirection(Qt.LeftToRight)
        self.containerFrame.setStyleSheet(u"border: 2px solid black")
        self.verticalLayout_5 = QVBoxLayout(self.containerFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.containerInformation = QWidget(self.containerFrame)
        self.containerInformation.setObjectName(u"containerInformation")
        self.containerInformation.setStyleSheet(u"border: none")
        self.verticalLayout_6 = QVBoxLayout(self.containerInformation)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lblTitle = QLabel(self.containerInformation)
        self.lblTitle.setObjectName(u"lblTitle")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.lblTitle.setFont(font1)
        self.lblTitle.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.lblTitle, 0, Qt.AlignHCenter)

        self.containerDetails = QWidget(self.containerInformation)
        self.containerDetails.setObjectName(u"containerDetails")
        self.verticalLayout_7 = QVBoxLayout(self.containerDetails)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lblConfigLocation = QLabel(self.containerDetails)
        self.lblConfigLocation.setObjectName(u"lblConfigLocation")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.lblConfigLocation.setFont(font2)
        self.lblConfigLocation.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_7.addWidget(self.lblConfigLocation)

        self.lblLocalServer = QLabel(self.containerDetails)
        self.lblLocalServer.setObjectName(u"lblLocalServer")
        self.lblLocalServer.setFont(font2)
        self.lblLocalServer.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_7.addWidget(self.lblLocalServer)

        self.lblLocalStorage = QLabel(self.containerDetails)
        self.lblLocalStorage.setObjectName(u"lblLocalStorage")
        self.lblLocalStorage.setFont(font2)
        self.lblLocalStorage.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_7.addWidget(self.lblLocalStorage)

        self.wPlaceholder = QWidget(self.containerDetails)
        self.wPlaceholder.setObjectName(u"wPlaceholder")
        self.horizontalLayout_2 = QHBoxLayout(self.wPlaceholder)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_7.addWidget(self.wPlaceholder)


        self.verticalLayout_6.addWidget(self.containerDetails)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 7)

        self.verticalLayout_5.addWidget(self.containerInformation)


        self.horizontalLayout.addWidget(self.containerFrame)


        self.verticalLayout_4.addWidget(self.containerInfoSection)

        self.containerButtons = QWidget(self.containerMain)
        self.containerButtons.setObjectName(u"containerButtons")
        self.verticalLayout_3 = QVBoxLayout(self.containerButtons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(500, -1, 500, -1)
        self.btnStart = QPushButton(self.containerButtons)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setFont(font1)
        self.btnStart.setStyleSheet(u"background-color: grey; height: 45;")

        self.verticalLayout_3.addWidget(self.btnStart)

        self.btnEditConfig = QPushButton(self.containerButtons)
        self.btnEditConfig.setObjectName(u"btnEditConfig")
        self.btnEditConfig.setFont(font1)
        self.btnEditConfig.setStyleSheet(u"background-color: grey; height: 45;")

        self.verticalLayout_3.addWidget(self.btnEditConfig)

        self.btnLogout = QPushButton(self.containerButtons)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setFont(font1)
        self.btnLogout.setStyleSheet(u"background-color: grey; height: 45;")

        self.verticalLayout_3.addWidget(self.btnLogout)

        self.btnExit = QPushButton(self.containerButtons)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setFont(font1)
        self.btnExit.setStyleSheet(u"background-color: grey; height: 45;")

        self.verticalLayout_3.addWidget(self.btnExit)


        self.verticalLayout_4.addWidget(self.containerButtons)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 5)

        self.gridLayout.addWidget(self.containerMain, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.containerScreen)

        self.verticalLayout.setStretch(0, 8)

        self.retranslateUi(HomeScreen)

        QMetaObject.connectSlotsByName(HomeScreen)
    # setupUi

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(QCoreApplication.translate("HomeScreen", u"Form", None))
        self.lblFqcs.setText(QCoreApplication.translate("HomeScreen", u"FQCS", None))
        self.lblTitle.setText(QCoreApplication.translate("HomeScreen", u"INFORMATION", None))
        self.lblConfigLocation.setText(QCoreApplication.translate("HomeScreen", u"**Current config location:** {{ConfigLocation}}", None))
        self.lblLocalServer.setText(QCoreApplication.translate("HomeScreen", u"**Local server:** {{LocalServer}}", None))
        self.lblLocalStorage.setText(QCoreApplication.translate("HomeScreen", u"**Local storage:** {{LocalStorage}}", None))
        self.btnStart.setText(QCoreApplication.translate("HomeScreen", u"START", None))
        self.btnEditConfig.setText(QCoreApplication.translate("HomeScreen", u"EDIT CONFIGURATION", None))
        self.btnLogout.setText(QCoreApplication.translate("HomeScreen", u"LOG OUT", None))
        self.btnExit.setText(QCoreApplication.translate("HomeScreen", u"EXIT", None))
    # retranslateUi

