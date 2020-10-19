# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_param_calibration_screenOehDRv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ColorParamCalibScreen(object):
    def setupUi(self, ColorParamCalibScreen):
        if not ColorParamCalibScreen.objectName():
            ColorParamCalibScreen.setObjectName(u"ColorParamCalibScreen")
        ColorParamCalibScreen.resize(1355, 805)
        ColorParamCalibScreen.setAutoFillBackground(False)
        ColorParamCalibScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(ColorParamCalibScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(ColorParamCalibScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.screen1 = QLabel(self.containerScreen)
        self.screen1.setObjectName(u"screen1")
        self.screen1.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen1, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.grpboxDisplayType = QGroupBox(self.containerScreen)
        self.grpboxDisplayType.setObjectName(u"grpboxDisplayType")
        self.verticalLayout_3 = QVBoxLayout(self.grpboxDisplayType)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.cbbDisplayType = QComboBox(self.grpboxDisplayType)
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.setObjectName(u"cbbDisplayType")
        self.cbbDisplayType.setAutoFillBackground(False)
        self.cbbDisplayType.setStyleSheet(u"height:22px")

        self.verticalLayout_3.addWidget(self.cbbDisplayType)


        self.horizontalLayout_4.addWidget(self.grpboxDisplayType, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 3)

        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.screen2 = QLabel(self.containerScreen)
        self.screen2.setObjectName(u"screen2")
        self.screen2.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen2, 0, 1, 1, 1)

        self.screen4 = QLabel(self.containerScreen)
        self.screen4.setObjectName(u"screen4")
        self.screen4.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen4, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(ColorParamCalibScreen)
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
        self.grpSldSupThresh = QGroupBox(self.containerMid)
        self.grpSldSupThresh.setObjectName(u"grpSldSupThresh")
        self.verticalLayout_11 = QVBoxLayout(self.grpSldSupThresh)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.sldSupThresh = QSlider(self.grpSldSupThresh)
        self.sldSupThresh.setObjectName(u"sldSupThresh")
        self.sldSupThresh.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.sldSupThresh)


        self.gridLayout_2.addWidget(self.grpSldSupThresh, 0, 0, 1, 1)

        self.groupInputTemplate_2 = QGroupBox(self.containerMid)
        self.groupInputTemplate_2.setObjectName(u"groupInputTemplate_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupInputTemplate_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ampThreshRed = QSpinBox(self.groupInputTemplate_2)
        self.ampThreshRed.setObjectName(u"ampThreshRed")
        self.ampThreshRed.setStyleSheet(u"background-color: rgba(255, 0, 0, 100);")
        self.ampThreshRed.setAccelerated(True)
        self.ampThreshRed.setMaximum(99999)

        self.horizontalLayout_2.addWidget(self.ampThreshRed)

        self.ampThreshGreen = QSpinBox(self.groupInputTemplate_2)
        self.ampThreshGreen.setObjectName(u"ampThreshGreen")
        self.ampThreshGreen.setStyleSheet(u"background-color: rgba(0, 203, 0, 100);")
        self.ampThreshGreen.setAccelerated(True)
        self.ampThreshGreen.setMaximum(99999)

        self.horizontalLayout_2.addWidget(self.ampThreshGreen)

        self.ampThreshBlue = QSpinBox(self.groupInputTemplate_2)
        self.ampThreshBlue.setObjectName(u"ampThreshBlue")
        self.ampThreshBlue.setStyleSheet(u"background-color: rgba(0, 85, 255, 100);")
        self.ampThreshBlue.setAccelerated(True)
        self.ampThreshBlue.setMaximum(99999)

        self.horizontalLayout_2.addWidget(self.ampThreshBlue)


        self.gridLayout_2.addWidget(self.groupInputTemplate_2, 0, 1, 1, 1)

        self.grpSldAllowDiff = QGroupBox(self.containerMid)
        self.grpSldAllowDiff.setObjectName(u"grpSldAllowDiff")
        self.verticalLayout_13 = QVBoxLayout(self.grpSldAllowDiff)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sldAllowDiff = QSlider(self.grpSldAllowDiff)
        self.sldAllowDiff.setObjectName(u"sldAllowDiff")
        self.sldAllowDiff.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sldAllowDiff)


        self.gridLayout_2.addWidget(self.grpSldAllowDiff, 3, 0, 1, 1)

        self.grpSldAmpRate = QGroupBox(self.containerMid)
        self.grpSldAmpRate.setObjectName(u"grpSldAmpRate")
        self.verticalLayout_12 = QVBoxLayout(self.grpSldAmpRate)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.sldAmpRate = QSlider(self.grpSldAmpRate)
        self.sldAmpRate.setObjectName(u"sldAmpRate")
        self.sldAmpRate.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.sldAmpRate)


        self.gridLayout_2.addWidget(self.grpSldAmpRate, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)

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

        self.verticalLayout_17.addWidget(self.btnCapture, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.containerVerticalBtn, 0, Qt.AlignTop)

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

        self.retranslateUi(ColorParamCalibScreen)

        QMetaObject.connectSlotsByName(ColorParamCalibScreen)
    # setupUi

    def retranslateUi(self, ColorParamCalibScreen):
        ColorParamCalibScreen.setWindowTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Form", None))
        self.screen1.setText(QCoreApplication.translate("ColorParamCalibScreen", u"SCREEN", None))
        self.grpboxDisplayType.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Display Type", None))
        self.cbbDisplayType.setItemText(0, QCoreApplication.translate("ColorParamCalibScreen", u"Item 1", None))
        self.cbbDisplayType.setItemText(1, QCoreApplication.translate("ColorParamCalibScreen", u"Item 2", None))

        self.screen2.setText(QCoreApplication.translate("ColorParamCalibScreen", u"SCREEN", None))
        self.screen4.setText(QCoreApplication.translate("ColorParamCalibScreen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("ColorParamCalibScreen", u"COLOR COMPARISON - PARAMETERS CALIBRATION", None))
        self.grpSldSupThresh.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Suppress Threshold: 0", None))
        self.groupInputTemplate_2.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Amplification Threshold", None))
        self.ampThreshRed.setSpecialValueText(QCoreApplication.translate("ColorParamCalibScreen", u"Red", None))
        self.ampThreshGreen.setSpecialValueText(QCoreApplication.translate("ColorParamCalibScreen", u"Green", None))
        self.ampThreshBlue.setSpecialValueText(QCoreApplication.translate("ColorParamCalibScreen", u"Blue", None))
        self.grpSldAllowDiff.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Allowed Difference: 0%", None))
        self.grpSldAmpRate.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Amplification Rate: 0", None))
        self.btnCapture.setText(QCoreApplication.translate("ColorParamCalibScreen", u"CAPTURE", None))
        self.btnBack.setText(QCoreApplication.translate("ColorParamCalibScreen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("ColorParamCalibScreen", u"NEXT", None))
    # retranslateUi

