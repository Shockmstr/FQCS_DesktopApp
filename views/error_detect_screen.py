# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_detect_screenuZDNwI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ErrorDetectScreen(object):
    def setupUi(self, ErrorDetectScreen):
        if not ErrorDetectScreen.objectName():
            ErrorDetectScreen.setObjectName(u"ErrorDetectScreen")
        ErrorDetectScreen.resize(1440, 784)
        ErrorDetectScreen.setAutoFillBackground(False)
        ErrorDetectScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(ErrorDetectScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(ErrorDetectScreen)
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


        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(ErrorDetectScreen)
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
        self.chkDefectDetection = QCheckBox(self.containerLeft)
        self.chkDefectDetection.setObjectName(u"chkDefectDetection")

        self.verticalLayout_10.addWidget(self.chkDefectDetection)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.containerLeft)

        self.containerMid = QWidget(self.containerParam)
        self.containerMid.setObjectName(u"containerMid")
        self.containerMid.setStyleSheet(u"#containerMid {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.gridLayout_2 = QGridLayout(self.containerMid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupMinimumScore = QGroupBox(self.containerMid)
        self.groupMinimumScore.setObjectName(u"groupMinimumScore")
        self.verticalLayout_5 = QVBoxLayout(self.groupMinimumScore)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.inpMinimumScore = QSpinBox(self.groupMinimumScore)
        self.inpMinimumScore.setObjectName(u"inpMinimumScore")
        self.inpMinimumScore.setMinimum(0)
        self.inpMinimumScore.setMaximum(100)

        self.verticalLayout_5.addWidget(self.inpMinimumScore)


        self.gridLayout_2.addWidget(self.groupMinimumScore, 2, 1, 1, 1)

        self.groupIouThreshold = QGroupBox(self.containerMid)
        self.groupIouThreshold.setObjectName(u"groupIouThreshold")
        self.verticalLayout_14 = QVBoxLayout(self.groupIouThreshold)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.inpIouThreshold = QSpinBox(self.groupIouThreshold)
        self.inpIouThreshold.setObjectName(u"inpIouThreshold")
        self.inpIouThreshold.setMinimum(0)
        self.inpIouThreshold.setMaximum(100)

        self.verticalLayout_14.addWidget(self.inpIouThreshold)


        self.gridLayout_2.addWidget(self.groupIouThreshold, 1, 1, 1, 1)

        self.groupCbbResize = QGroupBox(self.containerMid)
        self.groupCbbResize.setObjectName(u"groupCbbResize")
        self.horizontalLayout_4 = QHBoxLayout(self.groupCbbResize)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.cbbWidth = QComboBox(self.groupCbbResize)
        self.cbbWidth.addItem("")
        self.cbbWidth.addItem("")
        self.cbbWidth.setObjectName(u"cbbWidth")
        self.cbbWidth.setAutoFillBackground(False)
        self.cbbWidth.setStyleSheet(u"height:22px")
        self.cbbWidth.setEditable(True)

        self.horizontalLayout_4.addWidget(self.cbbWidth)

        self.cbbHeight = QComboBox(self.groupCbbResize)
        self.cbbHeight.addItem("")
        self.cbbHeight.addItem("")
        self.cbbHeight.setObjectName(u"cbbHeight")
        self.cbbHeight.setAutoFillBackground(False)
        self.cbbHeight.setStyleSheet(u"height:22px")
        self.cbbHeight.setEditable(True)

        self.horizontalLayout_4.addWidget(self.cbbHeight)


        self.gridLayout_2.addWidget(self.groupCbbResize, 0, 0, 1, 1)

        self.groupMaxInstances = QGroupBox(self.containerMid)
        self.groupMaxInstances.setObjectName(u"groupMaxInstances")
        self.verticalLayout_15 = QVBoxLayout(self.groupMaxInstances)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.inpMaxInstances = QSpinBox(self.groupMaxInstances)
        self.inpMaxInstances.setObjectName(u"inpMaxInstances")
        self.inpMaxInstances.setMinimum(1)
        self.inpMaxInstances.setMaximum(100)

        self.verticalLayout_15.addWidget(self.inpMaxInstances)


        self.gridLayout_2.addWidget(self.groupMaxInstances, 0, 1, 1, 1)

        self.groupModel = QGroupBox(self.containerMid)
        self.groupModel.setObjectName(u"groupModel")
        self.horizontalLayout_6 = QHBoxLayout(self.groupModel)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.inpModelChoice = QLineEdit(self.groupModel)
        self.inpModelChoice.setObjectName(u"inpModelChoice")

        self.horizontalLayout_6.addWidget(self.inpModelChoice)

        self.btnChooseModel = QPushButton(self.groupModel)
        self.btnChooseModel.setObjectName(u"btnChooseModel")

        self.horizontalLayout_6.addWidget(self.btnChooseModel)


        self.gridLayout_2.addWidget(self.groupModel, 0, 2, 1, 1)

        self.groupClasses = QGroupBox(self.containerMid)
        self.groupClasses.setObjectName(u"groupClasses")
        self.horizontalLayout_5 = QHBoxLayout(self.groupClasses)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.inpClasses = QLineEdit(self.groupClasses)
        self.inpClasses.setObjectName(u"inpClasses")

        self.horizontalLayout_5.addWidget(self.inpClasses)

        self.btnChooseClasses = QPushButton(self.groupClasses)
        self.btnChooseClasses.setObjectName(u"btnChooseClasses")

        self.horizontalLayout_5.addWidget(self.btnChooseClasses, 0, Qt.AlignRight)


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

        self.retranslateUi(ErrorDetectScreen)

        QMetaObject.connectSlotsByName(ErrorDetectScreen)
    # setupUi

    def retranslateUi(self, ErrorDetectScreen):
        ErrorDetectScreen.setWindowTitle(QCoreApplication.translate("ErrorDetectScreen", u"Form", None))
        self.screen4.setText(QCoreApplication.translate("ErrorDetectScreen", u"SCREEN", None))
        self.groupCbbDisplayType.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"Display Type", None))
        self.cbbDisplayType.setItemText(0, QCoreApplication.translate("ErrorDetectScreen", u"Item 1", None))
        self.cbbDisplayType.setItemText(1, QCoreApplication.translate("ErrorDetectScreen", u"Item 2", None))

        self.cbbDisplayType.setCurrentText(QCoreApplication.translate("ErrorDetectScreen", u"Item 1", None))
        self.screen2.setText(QCoreApplication.translate("ErrorDetectScreen", u"SCREEN", None))
        self.screen1.setText(QCoreApplication.translate("ErrorDetectScreen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("ErrorDetectScreen", u"DEFECTS DETECTION - PARAMETERS CONFIGURATION", None))
        self.chkDefectDetection.setText(QCoreApplication.translate("ErrorDetectScreen", u"Enable defects detection", None))
        self.groupMinimumScore.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"Minimum score", None))
        self.groupIouThreshold.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"IoU threshold", None))
        self.groupCbbResize.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"Resize", None))
        self.cbbWidth.setItemText(0, QCoreApplication.translate("ErrorDetectScreen", u"Item 1", None))
        self.cbbWidth.setItemText(1, QCoreApplication.translate("ErrorDetectScreen", u"Item 2", None))

        self.cbbWidth.setCurrentText(QCoreApplication.translate("ErrorDetectScreen", u"Width", None))
        self.cbbWidth.setPlaceholderText(QCoreApplication.translate("ErrorDetectScreen", u"Width", None))
        self.cbbHeight.setItemText(0, QCoreApplication.translate("ErrorDetectScreen", u"Item 1", None))
        self.cbbHeight.setItemText(1, QCoreApplication.translate("ErrorDetectScreen", u"Item 2", None))

        self.cbbHeight.setCurrentText(QCoreApplication.translate("ErrorDetectScreen", u"Height", None))
        self.cbbHeight.setPlaceholderText(QCoreApplication.translate("ErrorDetectScreen", u"Height", None))
        self.groupMaxInstances.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"Max Instances", None))
        self.groupModel.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"Model", None))
        self.inpModelChoice.setInputMask("")
        self.inpModelChoice.setText(QCoreApplication.translate("ErrorDetectScreen", u"yolov4.h5", None))
        self.inpModelChoice.setPlaceholderText(QCoreApplication.translate("ErrorDetectScreen", u"Input something", None))
        self.btnChooseModel.setText(QCoreApplication.translate("ErrorDetectScreen", u"...", None))
        self.groupClasses.setTitle(QCoreApplication.translate("ErrorDetectScreen", u"Classes", None))
        self.inpClasses.setInputMask("")
        self.inpClasses.setText("")
        self.inpClasses.setPlaceholderText(QCoreApplication.translate("ErrorDetectScreen", u"Input something", None))
        self.btnChooseClasses.setText(QCoreApplication.translate("ErrorDetectScreen", u"...", None))
        self.btnCapture.setText(QCoreApplication.translate("ErrorDetectScreen", u"CAPTURE", None))
        self.btnChoosePicture.setText(QCoreApplication.translate("ErrorDetectScreen", u"CHOOSE PICTURE", None))
        self.btnBack.setText(QCoreApplication.translate("ErrorDetectScreen", u"BACK", None))
        self.btnFinish.setText(QCoreApplication.translate("ErrorDetectScreen", u"FINISH", None))
    # retranslateUi

