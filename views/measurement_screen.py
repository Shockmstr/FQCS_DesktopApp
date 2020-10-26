# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'measurement_screenpCXrno.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MeasurementScreen(object):
    def setupUi(self, MeasurementScreen):
        if not MeasurementScreen.objectName():
            MeasurementScreen.setObjectName(u"MeasurementScreen")
        MeasurementScreen.resize(1440, 786)
        MeasurementScreen.setAutoFillBackground(False)
        MeasurementScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(MeasurementScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(MeasurementScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.screen1 = QLabel(self.containerScreen)
        self.screen1.setObjectName(u"screen1")
        self.screen1.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen1, 0, 0, 1, 1)

        self.screen2 = QLabel(self.containerScreen)
        self.screen2.setObjectName(u"screen2")
        self.screen2.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen2, 0, 1, 1, 1)

        self.screen3 = QLabel(self.containerScreen)
        self.screen3.setObjectName(u"screen3")
        self.screen3.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen3, 1, 0, 1, 1)

        self.screen4 = QLabel(self.containerScreen)
        self.screen4.setObjectName(u"screen4")
        self.screen4.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen4, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(MeasurementScreen)
        self.containerConfig.setObjectName(u"containerConfig")
        self.containerConfig.setAutoFillBackground(False)
        self.containerConfig.setStyleSheet(u"background-color: #EEEEEE")
        self.verticalLayout_2 = QVBoxLayout(self.containerConfig)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTitle = QLabel(self.containerConfig)
        self.lblTitle.setObjectName(u"lblTitle")
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
        self.groupSliderWidth = QGroupBox(self.containerMid)
        self.groupSliderWidth.setObjectName(u"groupSliderWidth")
        self.verticalLayout_11 = QVBoxLayout(self.groupSliderWidth)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.sldMaxinumWidth = QSlider(self.groupSliderWidth)
        self.sldMaxinumWidth.setObjectName(u"sldMaxinumWidth")
        self.sldMaxinumWidth.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.sldMaxinumWidth)


        self.gridLayout_2.addWidget(self.groupSliderWidth, 0, 0, 1, 1)

        self.groupLeftActualLength = QGroupBox(self.containerMid)
        self.groupLeftActualLength.setObjectName(u"groupLeftActualLength")
        self.verticalLayout_14 = QVBoxLayout(self.groupLeftActualLength)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.inpLeftActualLength = QLineEdit(self.groupLeftActualLength)
        self.inpLeftActualLength.setObjectName(u"inpLeftActualLength")

        self.verticalLayout_14.addWidget(self.inpLeftActualLength)


        self.gridLayout_2.addWidget(self.groupLeftActualLength, 1, 1, 1, 1)

        self.groupSliderPosition = QGroupBox(self.containerMid)
        self.groupSliderPosition.setObjectName(u"groupSliderPosition")
        self.verticalLayout_13 = QVBoxLayout(self.groupSliderPosition)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sldDectectPosition = QSlider(self.groupSliderPosition)
        self.sldDectectPosition.setObjectName(u"sldDectectPosition")
        self.sldDectectPosition.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sldDectectPosition)


        self.gridLayout_2.addWidget(self.groupSliderPosition, 0, 2, 1, 1)

        self.groupLeftDetectedLength = QGroupBox(self.containerMid)
        self.groupLeftDetectedLength.setObjectName(u"groupLeftDetectedLength")
        self.verticalLayout_15 = QVBoxLayout(self.groupLeftDetectedLength)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.inpLeftDetectedLength = QLineEdit(self.groupLeftDetectedLength)
        self.inpLeftDetectedLength.setObjectName(u"inpLeftDetectedLength")

        self.verticalLayout_15.addWidget(self.inpLeftDetectedLength)


        self.gridLayout_2.addWidget(self.groupLeftDetectedLength, 0, 1, 1, 1)

        self.groupSliderHeight = QGroupBox(self.containerMid)
        self.groupSliderHeight.setObjectName(u"groupSliderHeight")
        self.verticalLayout_12 = QVBoxLayout(self.groupSliderHeight)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.sldMaxinumHeight = QSlider(self.groupSliderHeight)
        self.sldMaxinumHeight.setObjectName(u"sldMaxinumHeight")
        self.sldMaxinumHeight.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.sldMaxinumHeight)


        self.gridLayout_2.addWidget(self.groupSliderHeight, 1, 0, 1, 1)

        self.groupLeftLengthUnit = QGroupBox(self.containerMid)
        self.groupLeftLengthUnit.setObjectName(u"groupLeftLengthUnit")
        self.verticalLayout_5 = QVBoxLayout(self.groupLeftLengthUnit)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.inpLengthUnit = QLineEdit(self.groupLeftLengthUnit)
        self.inpLengthUnit.setObjectName(u"inpLengthUnit")

        self.verticalLayout_5.addWidget(self.inpLengthUnit)


        self.gridLayout_2.addWidget(self.groupLeftLengthUnit, 2, 1, 1, 1)

        self.groupSliderDetectRange = QGroupBox(self.containerMid)
        self.groupSliderDetectRange.setObjectName(u"groupSliderDetectRange")
        self.verticalLayout_6 = QVBoxLayout(self.groupSliderDetectRange)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.sldDetectRange = QSlider(self.groupSliderDetectRange)
        self.sldDetectRange.setObjectName(u"sldDetectRange")
        self.sldDetectRange.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.sldDetectRange)


        self.gridLayout_2.addWidget(self.groupSliderDetectRange, 1, 2, 1, 1)

        self.groupInputAllowDiff = QGroupBox(self.containerMid)
        self.groupInputAllowDiff.setObjectName(u"groupInputAllowDiff")
        self.verticalLayout_7 = QVBoxLayout(self.groupInputAllowDiff)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.inpAllowDiff = QLineEdit(self.groupInputAllowDiff)
        self.inpAllowDiff.setObjectName(u"inpAllowDiff")

        self.verticalLayout_7.addWidget(self.inpAllowDiff)


        self.gridLayout_2.addWidget(self.groupInputAllowDiff, 2, 2, 1, 1)


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

        self.retranslateUi(MeasurementScreen)

        QMetaObject.connectSlotsByName(MeasurementScreen)
    # setupUi

    def retranslateUi(self, MeasurementScreen):
        MeasurementScreen.setWindowTitle(QCoreApplication.translate("MeasurementScreen", u"Form", None))
        self.screen1.setText(QCoreApplication.translate("MeasurementScreen", u"SCREEN", None))
        self.screen2.setText(QCoreApplication.translate("MeasurementScreen", u"SCREEN", None))
        self.screen3.setText(QCoreApplication.translate("MeasurementScreen", u"SCREEN", None))
        self.screen4.setText(QCoreApplication.translate("MeasurementScreen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("MeasurementScreen", u"DEFINE MEASUREMENT AND MIN AREA", None))
        self.groupSliderWidth.setTitle(QCoreApplication.translate("MeasurementScreen", u"Maxinum width(%)", None))
        self.groupLeftActualLength.setTitle(QCoreApplication.translate("MeasurementScreen", u"Left side actual length", None))
        self.inpLeftActualLength.setInputMask("")
        self.inpLeftActualLength.setText(QCoreApplication.translate("MeasurementScreen", u"27", None))
        self.inpLeftActualLength.setPlaceholderText(QCoreApplication.translate("MeasurementScreen", u"Input something", None))
        self.groupSliderPosition.setTitle(QCoreApplication.translate("MeasurementScreen", u"Detect position", None))
        self.groupLeftDetectedLength.setTitle(QCoreApplication.translate("MeasurementScreen", u"Left side detected length (px)", None))
        self.inpLeftDetectedLength.setInputMask("")
        self.inpLeftDetectedLength.setText(QCoreApplication.translate("MeasurementScreen", u"420", None))
        self.inpLeftDetectedLength.setPlaceholderText(QCoreApplication.translate("MeasurementScreen", u"Input something", None))
        self.groupSliderHeight.setTitle(QCoreApplication.translate("MeasurementScreen", u"Maxinum height(%)", None))
        self.groupLeftLengthUnit.setTitle(QCoreApplication.translate("MeasurementScreen", u"Length unit", None))
        self.inpLengthUnit.setInputMask("")
        self.inpLengthUnit.setText(QCoreApplication.translate("MeasurementScreen", u"cm", None))
        self.inpLengthUnit.setPlaceholderText(QCoreApplication.translate("MeasurementScreen", u"Input something", None))
        self.groupSliderDetectRange.setTitle(QCoreApplication.translate("MeasurementScreen", u"Detect range", None))
        self.groupInputAllowDiff.setTitle(QCoreApplication.translate("MeasurementScreen", u"Allow difference ({unit})", None))
        self.inpAllowDiff.setInputMask("")
        self.inpAllowDiff.setText(QCoreApplication.translate("MeasurementScreen", u"0.5", None))
        self.inpAllowDiff.setPlaceholderText(QCoreApplication.translate("MeasurementScreen", u"Input something", None))
        self.btnCapture.setText(QCoreApplication.translate("MeasurementScreen", u"CAPTURE", None))
        self.btnBack.setText(QCoreApplication.translate("MeasurementScreen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("MeasurementScreen", u"NEXT", None))
    # retranslateUi

