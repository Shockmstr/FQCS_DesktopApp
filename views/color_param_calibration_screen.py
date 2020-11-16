# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_param_calibration_screenrXrrKP.ui'
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
        ColorParamCalibScreen.resize(1440, 900)
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

        self.screen2 = QWidget(self.containerScreen)
        self.screen2.setObjectName(u"screen2")
        self.horizontalLayout_5 = QHBoxLayout(self.screen2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.screen2Left = QPushButton(self.screen2)
        self.screen2Left.setObjectName(u"screen2Left")

        self.horizontalLayout_5.addWidget(self.screen2Left)

        self.screen2Right = QPushButton(self.screen2)
        self.screen2Right.setObjectName(u"screen2Right")

        self.horizontalLayout_5.addWidget(self.screen2Right)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.gridLayout.addWidget(self.screen2, 0, 1, 1, 1)

        self.screen3 = QWidget(self.containerScreen)
        self.screen3.setObjectName(u"screen3")
        self.horizontalLayout_6 = QHBoxLayout(self.screen3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.screen3Left = QPushButton(self.screen3)
        self.screen3Left.setObjectName(u"screen3Left")

        self.horizontalLayout_6.addWidget(self.screen3Left)

        self.screen3Right = QPushButton(self.screen3)
        self.screen3Right.setObjectName(u"screen3Right")

        self.horizontalLayout_6.addWidget(self.screen3Right)


        self.gridLayout.addWidget(self.screen3, 1, 1, 1, 1)

        self.sectionInfo = QWidget(self.containerScreen)
        self.sectionInfo.setObjectName(u"sectionInfo")
        self.verticalLayout_3 = QVBoxLayout(self.sectionInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inpResult = QTextEdit(self.sectionInfo)
        self.inpResult.setObjectName(u"inpResult")
        self.inpResult.setEnabled(True)
        self.inpResult.setReadOnly(True)
        self.inpResult.setOverwriteMode(False)
        self.inpResult.setAcceptRichText(True)

        self.verticalLayout_3.addWidget(self.inpResult)


        self.gridLayout.addWidget(self.sectionInfo, 1, 0, 1, 1)

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
        self.chkColorCompare = QCheckBox(self.containerLeft)
        self.chkColorCompare.setObjectName(u"chkColorCompare")

        self.verticalLayout_10.addWidget(self.chkColorCompare)

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
        self.grpSldAllowDiff = QGroupBox(self.containerMid)
        self.grpSldAllowDiff.setObjectName(u"grpSldAllowDiff")
        self.verticalLayout_13 = QVBoxLayout(self.grpSldAllowDiff)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sldAllowDiff = QSlider(self.grpSldAllowDiff)
        self.sldAllowDiff.setObjectName(u"sldAllowDiff")
        self.sldAllowDiff.setMinimum(1)
        self.sldAllowDiff.setMaximum(50)
        self.sldAllowDiff.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sldAllowDiff)


        self.gridLayout_2.addWidget(self.grpSldAllowDiff, 3, 0, 1, 1)

        self.grpSldSupThresh = QGroupBox(self.containerMid)
        self.grpSldSupThresh.setObjectName(u"grpSldSupThresh")
        self.verticalLayout_11 = QVBoxLayout(self.grpSldSupThresh)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.inpSuppThreshold = QSpinBox(self.grpSldSupThresh)
        self.inpSuppThreshold.setObjectName(u"inpSuppThreshold")

        self.verticalLayout_11.addWidget(self.inpSuppThreshold)


        self.gridLayout_2.addWidget(self.grpSldSupThresh, 0, 0, 1, 1)

        self.grpSldAmpRate = QGroupBox(self.containerMid)
        self.grpSldAmpRate.setObjectName(u"grpSldAmpRate")
        self.verticalLayout_12 = QVBoxLayout(self.grpSldAmpRate)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.sldAmpRate = QSlider(self.grpSldAmpRate)
        self.sldAmpRate.setObjectName(u"sldAmpRate")
        self.sldAmpRate.setMinimum(1)
        self.sldAmpRate.setMaximum(50)
        self.sldAmpRate.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.sldAmpRate)


        self.gridLayout_2.addWidget(self.grpSldAmpRate, 1, 0, 1, 1)

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

        self.btnEditAmpThresh = QPushButton(self.groupInputTemplate_2)
        self.btnEditAmpThresh.setObjectName(u"btnEditAmpThresh")

        self.horizontalLayout_2.addWidget(self.btnEditAmpThresh)


        self.gridLayout_2.addWidget(self.groupInputTemplate_2, 0, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)

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
        self.screen2Left.setText(QCoreApplication.translate("ColorParamCalibScreen", u"PushButton", None))
        self.screen2Right.setText(QCoreApplication.translate("ColorParamCalibScreen", u"PushButton", None))
        self.screen3Left.setText(QCoreApplication.translate("ColorParamCalibScreen", u"PushButton", None))
        self.screen3Right.setText(QCoreApplication.translate("ColorParamCalibScreen", u"PushButton", None))
        self.inpResult.setMarkdown(QCoreApplication.translate("ColorParamCalibScreen", u"**RESULT**\n"
"\n"
"", None))
        self.inpResult.setHtml(QCoreApplication.translate("ColorParamCalibScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">RESULT</span></p></body></html>", None))
        self.lblTitle.setText(QCoreApplication.translate("ColorParamCalibScreen", u"COLOR COMPARISON - PARAMETERS CALIBRATION", None))
        self.chkColorCompare.setText(QCoreApplication.translate("ColorParamCalibScreen", u"Enable Color Comparison", None))
        self.grpSldAllowDiff.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Allowed Difference (%): 0", None))
        self.grpSldSupThresh.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Suppress Threshold", None))
        self.grpSldAmpRate.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Amplification Rate: 0", None))
        self.groupInputTemplate_2.setTitle(QCoreApplication.translate("ColorParamCalibScreen", u"Amplification Threshold", None))
        self.ampThreshRed.setSpecialValueText("")
        self.ampThreshGreen.setSpecialValueText("")
        self.ampThreshBlue.setSpecialValueText("")
        self.btnEditAmpThresh.setText(QCoreApplication.translate("ColorParamCalibScreen", u"Edit", None))
        self.btnCapture.setText(QCoreApplication.translate("ColorParamCalibScreen", u"CAPTURE", None))
        self.btnBack.setText(QCoreApplication.translate("ColorParamCalibScreen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("ColorParamCalibScreen", u"NEXT", None))
    # retranslateUi

