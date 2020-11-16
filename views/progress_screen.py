# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_screenvnPdsK.ui'
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
        self.sectionSideResult = QWidget(self.containerScreen)
        self.sectionSideResult.setObjectName(u"sectionSideResult")
        self.verticalLayout_3 = QVBoxLayout(self.sectionSideResult)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groubCbbCamera = QGroupBox(self.sectionSideResult)
        self.groubCbbCamera.setObjectName(u"groubCbbCamera")
        self.horizontalLayout_5 = QHBoxLayout(self.groubCbbCamera)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.cbbCamera = QComboBox(self.groubCbbCamera)
        self.cbbCamera.addItem("")
        self.cbbCamera.addItem("")
        self.cbbCamera.setObjectName(u"cbbCamera")
        self.cbbCamera.setAutoFillBackground(False)
        self.cbbCamera.setStyleSheet(u"height:22px")
        self.cbbCamera.setEditable(False)

        self.horizontalLayout_5.addWidget(self.cbbCamera)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groubCbbCamera)

        self.lblSideResult = QLabel(self.sectionSideResult)
        self.lblSideResult.setObjectName(u"lblSideResult")

        self.verticalLayout_3.addWidget(self.lblSideResult)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)

        self.gridLayout.addWidget(self.sectionSideResult, 1, 1, 1, 1)

        self.screen1 = QLabel(self.containerScreen)
        self.screen1.setObjectName(u"screen1")
        self.screen1.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen1, 0, 0, 1, 1)

        self.sectionInfo = QWidget(self.containerScreen)
        self.sectionInfo.setObjectName(u"sectionInfo")
        self.verticalLayout_5 = QVBoxLayout(self.sectionInfo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupCbbDisplayType = QGroupBox(self.sectionInfo)
        self.groupCbbDisplayType.setObjectName(u"groupCbbDisplayType")
        self.horizontalLayout_2 = QHBoxLayout(self.groupCbbDisplayType)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.cbbDisplayType = QComboBox(self.groupCbbDisplayType)
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.setObjectName(u"cbbDisplayType")
        self.cbbDisplayType.setAutoFillBackground(False)
        self.cbbDisplayType.setStyleSheet(u"height:22px")
        self.cbbDisplayType.setEditable(False)

        self.horizontalLayout_2.addWidget(self.cbbDisplayType)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_5.addWidget(self.groupCbbDisplayType)

        self.inpResult = QTextEdit(self.sectionInfo)
        self.inpResult.setObjectName(u"inpResult")
        self.inpResult.setEnabled(True)
        self.inpResult.setReadOnly(True)
        self.inpResult.setOverwriteMode(False)
        self.inpResult.setAcceptRichText(True)

        self.verticalLayout_5.addWidget(self.inpResult)


        self.gridLayout.addWidget(self.sectionInfo, 1, 0, 1, 1)

        self.sectionMainResult = QWidget(self.containerScreen)
        self.sectionMainResult.setObjectName(u"sectionMainResult")
        self.horizontalLayout_7 = QHBoxLayout(self.sectionMainResult)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.detected_L = QLabel(self.sectionMainResult)
        self.detected_L.setObjectName(u"detected_L")
        self.detected_L.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.detected_L.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.detected_L)

        self.sample_L = QLabel(self.sectionMainResult)
        self.sample_L.setObjectName(u"sample_L")
        self.sample_L.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.sample_L.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.sample_L)

        self.line = QFrame(self.sectionMainResult)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.detected_R = QLabel(self.sectionMainResult)
        self.detected_R.setObjectName(u"detected_R")
        self.detected_R.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.detected_R.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.detected_R)

        self.sample_R = QLabel(self.sectionMainResult)
        self.sample_R.setObjectName(u"sample_R")
        self.sample_R.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.sample_R.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.sample_R)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(3, 1)
        self.horizontalLayout_7.setStretch(4, 1)

        self.gridLayout.addWidget(self.sectionMainResult, 0, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

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
        self.groubCbbCamera.setTitle(QCoreApplication.translate("ProgressScreen", u"Show result from side camera", None))
        self.cbbCamera.setItemText(0, QCoreApplication.translate("ProgressScreen", u"Item 1", None))
        self.cbbCamera.setItemText(1, QCoreApplication.translate("ProgressScreen", u"Item 2", None))

        self.cbbCamera.setCurrentText(QCoreApplication.translate("ProgressScreen", u"Item 1", None))
        self.lblSideResult.setText(QCoreApplication.translate("ProgressScreen", u"Result placeholder", None))
        self.screen1.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.groupCbbDisplayType.setTitle(QCoreApplication.translate("ProgressScreen", u"Display Type", None))
        self.cbbDisplayType.setItemText(0, QCoreApplication.translate("ProgressScreen", u"Original", None))
        self.cbbDisplayType.setItemText(1, QCoreApplication.translate("ProgressScreen", u"Detection", None))
        self.cbbDisplayType.setItemText(2, QCoreApplication.translate("ProgressScreen", u"Contours", None))

        self.cbbDisplayType.setCurrentText(QCoreApplication.translate("ProgressScreen", u"Original", None))
        self.inpResult.setMarkdown(QCoreApplication.translate("ProgressScreen", u"**RESULT**\n"
"\n"
"", None))
        self.inpResult.setHtml(QCoreApplication.translate("ProgressScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">RESULT</span></p></body></html>", None))
        self.detected_L.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.sample_L.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.detected_R.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.sample_R.setText(QCoreApplication.translate("ProgressScreen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("ProgressScreen", u"PROGRESS", None))
        self.btnCapture.setText(QCoreApplication.translate("ProgressScreen", u"CAPTURE", None))
        self.btnReturnHome.setText(QCoreApplication.translate("ProgressScreen", u"RETURN HOME", None))
    # retranslateUi

