# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_screenLMeusb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProgressScreen(object):
    def setupUi(self, ProgressScreen):
        if not ProgressScreen.objectName():
            ProgressScreen.setObjectName(u"ProgressScreen")
        ProgressScreen.resize(1440, 790)
        ProgressScreen.setAutoFillBackground(False)
        ProgressScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(ProgressScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(ProgressScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalWidget = QWidget(self.containerScreen)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(self.horizontalWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupCbbDisplayType = QGroupBox(self.widget_2)
        self.groupCbbDisplayType.setObjectName(u"groupCbbDisplayType")
        self.verticalLayout_4 = QVBoxLayout(self.groupCbbDisplayType)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.cbbDisplayType = QComboBox(self.groupCbbDisplayType)
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.setObjectName(u"cbbDisplayType")
        self.cbbDisplayType.setAutoFillBackground(False)
        self.cbbDisplayType.setStyleSheet(u"height:22px")
        self.cbbDisplayType.setEditable(True)

        self.verticalLayout_4.addWidget(self.cbbDisplayType)


        self.verticalLayout_6.addWidget(self.groupCbbDisplayType, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.horizontalWidget)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_2.addWidget(self.widget)


        self.gridLayout.addWidget(self.horizontalWidget, 1, 0, 1, 1)

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

        self.widget_3 = QWidget(self.containerScreen)
        self.widget_3.setObjectName(u"widget_3")
        self.grpImageResult = QWidget(self.widget_3)
        self.grpImageResult.setObjectName(u"grpImageResult")
        self.grpImageResult.setGeometry(QRect(0, 50, 701, 261))
        self.horizontalLayout_4 = QHBoxLayout(self.grpImageResult)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.detected_L = QLabel(self.grpImageResult)
        self.detected_L.setObjectName(u"detected_L")
        self.detected_L.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.detected_L.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.detected_L)

        self.sample_L = QLabel(self.grpImageResult)
        self.sample_L.setObjectName(u"sample_L")
        self.sample_L.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.sample_L.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.sample_L)

        self.line = QFrame(self.grpImageResult)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.detected_R = QLabel(self.grpImageResult)
        self.detected_R.setObjectName(u"detected_R")
        self.detected_R.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.detected_R.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.detected_R)

        self.sample_R = QLabel(self.grpImageResult)
        self.sample_R.setObjectName(u"sample_R")
        self.sample_R.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.sample_R.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.sample_R)

        self.groubCbbCamera = QGroupBox(self.widget_3)
        self.groubCbbCamera.setObjectName(u"groubCbbCamera")
        self.groubCbbCamera.setGeometry(QRect(0, 0, 335, 47))
        self.verticalLayout_5 = QVBoxLayout(self.groubCbbCamera)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.cbbCamera = QComboBox(self.groubCbbCamera)
        self.cbbCamera.addItem("")
        self.cbbCamera.addItem("")
        self.cbbCamera.setObjectName(u"cbbCamera")
        self.cbbCamera.setAutoFillBackground(False)
        self.cbbCamera.setStyleSheet(u"height:22px")
        self.cbbCamera.setEditable(True)

        self.verticalLayout_5.addWidget(self.cbbCamera)


        self.gridLayout.addWidget(self.widget_3, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(ProgressScreen)
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
        self.verticalLayout_16 = QVBoxLayout(self.containerRight)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.containerVerticalBtn = QWidget(self.containerRight)
        self.containerVerticalBtn.setObjectName(u"containerVerticalBtn")
        self.verticalLayout_17 = QVBoxLayout(self.containerVerticalBtn)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btnCapture = QPushButton(self.containerVerticalBtn)
        self.btnCapture.setObjectName(u"btnCapture")

        self.verticalLayout_17.addWidget(self.btnCapture)


        self.verticalLayout_16.addWidget(self.containerVerticalBtn, 0, Qt.AlignTop)

        self.containerNavBtn = QWidget(self.containerRight)
        self.containerNavBtn.setObjectName(u"containerNavBtn")
        self.horizontalLayout_3 = QHBoxLayout(self.containerNavBtn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnReturnHome = QPushButton(self.containerNavBtn)
        self.btnReturnHome.setObjectName(u"btnReturnHome")

        self.horizontalLayout_3.addWidget(self.btnReturnHome)


        self.verticalLayout_16.addWidget(self.containerNavBtn, 0, Qt.AlignBottom)


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

        self.retranslateUi(ProgressScreen)

        QMetaObject.connectSlotsByName(ProgressScreen)
    # setupUi

    def retranslateUi(self, ProgressScreen):
        ProgressScreen.setWindowTitle(QCoreApplication.translate("ProgressScreen", u"Form", None))
        self.groupCbbDisplayType.setTitle(QCoreApplication.translate("ProgressScreen", u"Display Type", None))
        self.cbbDisplayType.setItemText(0, QCoreApplication.translate("ProgressScreen", u"Item 1", None))
        self.cbbDisplayType.setItemText(1, QCoreApplication.translate("ProgressScreen", u"Item 2", None))

        self.cbbDisplayType.setCurrentText(QCoreApplication.translate("ProgressScreen", u"Item 1", None))
        self.screen2.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.screen1.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.detected_L.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.sample_L.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.detected_R.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.sample_R.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.groubCbbCamera.setTitle(QCoreApplication.translate("ProgressScreen", u"Camera", None))
        self.cbbCamera.setItemText(0, QCoreApplication.translate("ProgressScreen", u"Item 1", None))
        self.cbbCamera.setItemText(1, QCoreApplication.translate("ProgressScreen", u"Item 2", None))

        self.cbbCamera.setCurrentText(QCoreApplication.translate("ProgressScreen", u"Item 1", None))
        self.lblTitle.setText(QCoreApplication.translate("ProgressScreen", u"PROGRESS", None))
        self.btnCapture.setText(QCoreApplication.translate("ProgressScreen", u"CAPTURE", None))
        self.btnReturnHome.setText(QCoreApplication.translate("ProgressScreen", u"RETURN HOME", None))
    # retranslateUi

