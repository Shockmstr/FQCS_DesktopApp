# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_error_detect_screenPUEtZn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SideErrorDetectScreen(object):
    def setupUi(self, SideErrorDetectScreen):
        if not SideErrorDetectScreen.objectName():
            SideErrorDetectScreen.setObjectName(u"SideErrorDetectScreen")
        SideErrorDetectScreen.resize(1440, 784)
        SideErrorDetectScreen.setAutoFillBackground(False)
        SideErrorDetectScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(SideErrorDetectScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(SideErrorDetectScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.screen4 = QLabel(self.containerScreen)
        self.screen4.setObjectName(u"screen4")
        self.screen4.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen4, 1, 1, 1, 1)

        self.horizontalWidget = QWidget(self.containerScreen)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(self.horizontalWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

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


        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(SideErrorDetectScreen)
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
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 12)

        self.horizontalLayout.addWidget(self.containerLeft)

        self.containerMid = QWidget(self.containerParam)
        self.containerMid.setObjectName(u"containerMid")
        self.containerMid.setStyleSheet(u"#containerMid {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.gridLayout_2 = QGridLayout(self.containerMid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupScoreThresh = QGroupBox(self.containerMid)
        self.groupScoreThresh.setObjectName(u"groupScoreThresh")
        self.verticalLayout_4 = QVBoxLayout(self.groupScoreThresh)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.sldScoreThresh = QSlider(self.groupScoreThresh)
        self.sldScoreThresh.setObjectName(u"sldScoreThresh")
        self.sldScoreThresh.setEnabled(False)
        self.sldScoreThresh.setMinimum(0)
        self.sldScoreThresh.setMaximum(100)
        self.sldScoreThresh.setValue(0)
        self.sldScoreThresh.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.sldScoreThresh)


        self.gridLayout_2.addWidget(self.groupScoreThresh, 2, 1, 1, 1)

        self.groupMaxInstances = QGroupBox(self.containerMid)
        self.groupMaxInstances.setObjectName(u"groupMaxInstances")
        self.horizontalLayout_7 = QHBoxLayout(self.groupMaxInstances)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.inpMaxInstances = QSpinBox(self.groupMaxInstances)
        self.inpMaxInstances.setObjectName(u"inpMaxInstances")
        self.inpMaxInstances.setEnabled(False)
        self.inpMaxInstances.setMinimum(1)
        self.inpMaxInstances.setMaximum(100)

        self.horizontalLayout_7.addWidget(self.inpMaxInstances)


        self.gridLayout_2.addWidget(self.groupMaxInstances, 0, 1, 1, 1)

        self.groupCbbResize = QGroupBox(self.containerMid)
        self.groupCbbResize.setObjectName(u"groupCbbResize")
        self.horizontalLayout_4 = QHBoxLayout(self.groupCbbResize)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.cbbWidth = QComboBox(self.groupCbbResize)
        self.cbbWidth.addItem("")
        self.cbbWidth.addItem("")
        self.cbbWidth.setObjectName(u"cbbWidth")
        self.cbbWidth.setEnabled(False)
        self.cbbWidth.setAutoFillBackground(False)
        self.cbbWidth.setStyleSheet(u"height:22px")
        self.cbbWidth.setEditable(False)

        self.horizontalLayout_4.addWidget(self.cbbWidth)

        self.cbbHeight = QComboBox(self.groupCbbResize)
        self.cbbHeight.addItem("")
        self.cbbHeight.addItem("")
        self.cbbHeight.setObjectName(u"cbbHeight")
        self.cbbHeight.setEnabled(False)
        self.cbbHeight.setAutoFillBackground(False)
        self.cbbHeight.setStyleSheet(u"height:22px")
        self.cbbHeight.setEditable(False)

        self.horizontalLayout_4.addWidget(self.cbbHeight)


        self.gridLayout_2.addWidget(self.groupCbbResize, 0, 0, 1, 1)

        self.groupIoUThresh = QGroupBox(self.containerMid)
        self.groupIoUThresh.setObjectName(u"groupIoUThresh")
        self.verticalLayout_3 = QVBoxLayout(self.groupIoUThresh)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.sldIoUThresh = QSlider(self.groupIoUThresh)
        self.sldIoUThresh.setObjectName(u"sldIoUThresh")
        self.sldIoUThresh.setEnabled(False)
        self.sldIoUThresh.setMaximum(100)
        self.sldIoUThresh.setValue(0)
        self.sldIoUThresh.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sldIoUThresh)


        self.gridLayout_2.addWidget(self.groupIoUThresh, 1, 1, 1, 1)

        self.groupModel = QGroupBox(self.containerMid)
        self.groupModel.setObjectName(u"groupModel")
        self.horizontalLayout_6 = QHBoxLayout(self.groupModel)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.inpModelChoice = QLineEdit(self.groupModel)
        self.inpModelChoice.setObjectName(u"inpModelChoice")
        self.inpModelChoice.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.inpModelChoice)


        self.gridLayout_2.addWidget(self.groupModel, 0, 2, 1, 1)

        self.groupClasses = QGroupBox(self.containerMid)
        self.groupClasses.setObjectName(u"groupClasses")
        self.horizontalLayout_5 = QHBoxLayout(self.groupClasses)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.inpClasses = QLineEdit(self.groupClasses)
        self.inpClasses.setObjectName(u"inpClasses")
        self.inpClasses.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.inpClasses)


        self.gridLayout_2.addWidget(self.groupClasses, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

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

        self.btnChoosePicture = QPushButton(self.containerVerticalBtn)
        self.btnChoosePicture.setObjectName(u"btnChoosePicture")

        self.verticalLayout_17.addWidget(self.btnChoosePicture)


        self.verticalLayout_16.addWidget(self.containerVerticalBtn, 0, Qt.AlignTop)

        self.btnDetect = QPushButton(self.containerRight)
        self.btnDetect.setObjectName(u"btnDetect")

        self.verticalLayout_16.addWidget(self.btnDetect)

        self.containerNavBtn = QWidget(self.containerRight)
        self.containerNavBtn.setObjectName(u"containerNavBtn")
        self.horizontalLayout_3 = QHBoxLayout(self.containerNavBtn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.containerNavBtn)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout_3.addWidget(self.btnBack)

        self.btnFinish = QPushButton(self.containerNavBtn)
        self.btnFinish.setObjectName(u"btnFinish")

        self.horizontalLayout_3.addWidget(self.btnFinish)


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

        self.retranslateUi(SideErrorDetectScreen)

        QMetaObject.connectSlotsByName(SideErrorDetectScreen)
    # setupUi

    def retranslateUi(self, SideErrorDetectScreen):
        SideErrorDetectScreen.setWindowTitle(QCoreApplication.translate("SideErrorDetectScreen", u"Form", None))
        self.screen4.setText(QCoreApplication.translate("SideErrorDetectScreen", u"SCREEN", None))
        self.screen2.setText(QCoreApplication.translate("SideErrorDetectScreen", u"SCREEN", None))
        self.screen1.setText(QCoreApplication.translate("SideErrorDetectScreen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("SideErrorDetectScreen", u"DEFECTS DETECTION - PARAMETERS CONFIGURATION", None))
        self.groupScoreThresh.setTitle(QCoreApplication.translate("SideErrorDetectScreen", u"Score threshold", None))
        self.groupMaxInstances.setTitle(QCoreApplication.translate("SideErrorDetectScreen", u"Max Instances", None))
        self.groupCbbResize.setTitle(QCoreApplication.translate("SideErrorDetectScreen", u"Resize", None))
        self.cbbWidth.setItemText(0, QCoreApplication.translate("SideErrorDetectScreen", u"Item 1", None))
        self.cbbWidth.setItemText(1, QCoreApplication.translate("SideErrorDetectScreen", u"Item 2", None))

        self.cbbWidth.setCurrentText(QCoreApplication.translate("SideErrorDetectScreen", u"Width", None))
        self.cbbWidth.setPlaceholderText(QCoreApplication.translate("SideErrorDetectScreen", u"Width", None))
        self.cbbHeight.setItemText(0, QCoreApplication.translate("SideErrorDetectScreen", u"Item 1", None))
        self.cbbHeight.setItemText(1, QCoreApplication.translate("SideErrorDetectScreen", u"Item 2", None))

        self.cbbHeight.setCurrentText(QCoreApplication.translate("SideErrorDetectScreen", u"Height", None))
        self.cbbHeight.setPlaceholderText(QCoreApplication.translate("SideErrorDetectScreen", u"Height", None))
        self.groupIoUThresh.setTitle(QCoreApplication.translate("SideErrorDetectScreen", u"IoU threshold", None))
        self.groupModel.setTitle(QCoreApplication.translate("SideErrorDetectScreen", u"Model", None))
        self.inpModelChoice.setInputMask("")
        self.inpModelChoice.setText(QCoreApplication.translate("SideErrorDetectScreen", u"yolov4.h5", None))
        self.inpModelChoice.setPlaceholderText(QCoreApplication.translate("SideErrorDetectScreen", u"Input something", None))
        self.groupClasses.setTitle(QCoreApplication.translate("SideErrorDetectScreen", u"Classes", None))
        self.inpClasses.setInputMask("")
        self.inpClasses.setText("")
        self.inpClasses.setPlaceholderText(QCoreApplication.translate("SideErrorDetectScreen", u"Input something", None))
        self.btnCapture.setText(QCoreApplication.translate("SideErrorDetectScreen", u"CAPTURE", None))
        self.btnChoosePicture.setText(QCoreApplication.translate("SideErrorDetectScreen", u"CHOOSE PICTURE", None))
        self.btnDetect.setText(QCoreApplication.translate("SideErrorDetectScreen", u"DETECT", None))
        self.btnBack.setText(QCoreApplication.translate("SideErrorDetectScreen", u"BACK", None))
        self.btnFinish.setText(QCoreApplication.translate("SideErrorDetectScreen", u"FINISH", None))
    # retranslateUi

