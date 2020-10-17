# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowMAzLTo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1355, 820)
        MainWindow.setStyleSheet(u"background:#E5E5E5")
        self.actionLoadCfg = QAction(MainWindow)
        self.actionLoadCfg.setObjectName(u"actionLoadCfg")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSaveCfg = QAction(MainWindow)
        self.actionSaveCfg.setObjectName(u"actionSaveCfg")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralStackWidget = QStackedWidget(self.centralwidget)
        self.centralStackWidget.setObjectName(u"centralStackWidget")

        self.verticalLayout.addWidget(self.centralStackWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1355, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSaveCfg)
        self.menuFile.addAction(self.actionLoadCfg)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FQCS", None))
        self.actionLoadCfg.setText(QCoreApplication.translate("MainWindow", u"Load configuration", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSaveCfg.setText(QCoreApplication.translate("MainWindow", u"Save configuration", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

