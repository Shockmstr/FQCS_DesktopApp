# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_detect_pair_screenygMGNv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_test_detect_pair_screen(object):
    def setupUi(self, test_detect_pair_screen):
        if not test_detect_pair_screen.objectName():
            test_detect_pair_screen.setObjectName(u"test_detect_pair_screen")
        test_detect_pair_screen.resize(1440, 848)
        test_detect_pair_screen.setAutoFillBackground(False)
        test_detect_pair_screen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(test_detect_pair_screen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(test_detect_pair_screen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 12)
        self.screen2 = QLabel(self.containerScreen)
        self.screen2.setObjectName(u"screen2")
        self.screen2.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen2, 0, 1, 1, 1)

        self.screen1 = QLabel(self.containerScreen)
        self.screen1.setObjectName(u"screen1")
        self.screen1.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen1, 0, 0, 1, 1)

        self.screen4 = QLabel(self.containerScreen)
        self.screen4.setObjectName(u"screen4")
        self.screen4.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen4, 1, 1, 1, 1)

        self.widget = QWidget(self.containerScreen)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.horizontalLayout_2.setStretch(0, 2)

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(test_detect_pair_screen)
        self.containerConfig.setObjectName(u"containerConfig")
        self.containerConfig.setAutoFillBackground(False)
        self.containerConfig.setStyleSheet(u"background-color: #EEEEEE")
        self.verticalLayout_2 = QVBoxLayout(self.containerConfig)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitle = QLabel(self.containerConfig)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet(u"text-align:center;\n"
"font-weight:bold;")
        self.lblTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblTitle)

        self.containerParam = QWidget(self.containerConfig)
        self.containerParam.setObjectName(u"containerParam")
        self.horizontalLayout = QHBoxLayout(self.containerParam)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerLeft = QWidget(self.containerParam)
        self.containerLeft.setObjectName(u"containerLeft")
        self.containerLeft.setStyleSheet(u"#containerLeft {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.containerLeft)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.horizontalLayout.addWidget(self.containerLeft)

        self.containerMid = QWidget(self.containerParam)
        self.containerMid.setObjectName(u"containerMid")
        self.containerMid.setStyleSheet(u"#containerMid {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.gridLayout_2 = QGridLayout(self.containerMid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.horizontalLayout.addWidget(self.containerMid)

        self.containerRight = QWidget(self.containerParam)
        self.containerRight.setObjectName(u"containerRight")
        self.containerRight.setStyleSheet(u"#containerRight {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.containerRight)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnCapture = QPushButton(self.containerRight)
        self.btnCapture.setObjectName(u"btnCapture")

        self.verticalLayout_3.addWidget(self.btnCapture)

        self.containerVerticalBtn = QWidget(self.containerRight)
        self.containerVerticalBtn.setObjectName(u"containerVerticalBtn")
        self.verticalLayout_17 = QVBoxLayout(self.containerVerticalBtn)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btnSaveSample = QPushButton(self.containerVerticalBtn)
        self.btnSaveSample.setObjectName(u"btnSaveSample")

        self.verticalLayout_17.addWidget(self.btnSaveSample)

        self.btnRetakeSample = QPushButton(self.containerVerticalBtn)
        self.btnRetakeSample.setObjectName(u"btnRetakeSample")

        self.verticalLayout_17.addWidget(self.btnRetakeSample, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.containerVerticalBtn)

        self.containerNavBtn = QWidget(self.containerRight)
        self.containerNavBtn.setObjectName(u"containerNavBtn")
        self.horizontalLayout_3 = QHBoxLayout(self.containerNavBtn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.containerNavBtn)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout_3.addWidget(self.btnBack)

        self.btnNext = QPushButton(self.containerNavBtn)
        self.btnNext.setObjectName(u"btnNext")

        self.horizontalLayout_3.addWidget(self.btnNext)


        self.verticalLayout_3.addWidget(self.containerNavBtn)


        self.horizontalLayout.addWidget(self.containerRight)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout_2.addWidget(self.containerParam)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)

        self.verticalLayout.addWidget(self.containerConfig)

        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(test_detect_pair_screen)

        QMetaObject.connectSlotsByName(test_detect_pair_screen)
    # setupUi

    def retranslateUi(self, test_detect_pair_screen):
        test_detect_pair_screen.setWindowTitle(QCoreApplication.translate("test_detect_pair_screen", u"Form", None))
        self.screen2.setText(QCoreApplication.translate("test_detect_pair_screen", u"SCREEN", None))
        self.screen1.setText(QCoreApplication.translate("test_detect_pair_screen", u"SCREEN", None))
        self.screen4.setText(QCoreApplication.translate("test_detect_pair_screen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("test_detect_pair_screen", u"TEST AND DEFINE SAMPLE", None))
        self.btnCapture.setText(QCoreApplication.translate("test_detect_pair_screen", u"CAPTURE", None))
        self.btnSaveSample.setText(QCoreApplication.translate("test_detect_pair_screen", u"SAVE SAMPLE", None))
        self.btnRetakeSample.setText(QCoreApplication.translate("test_detect_pair_screen", u"RETAKE SAMPLE", None))
        self.btnBack.setText(QCoreApplication.translate("test_detect_pair_screen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("test_detect_pair_screen", u"NEXT", None))
    # retranslateUi

