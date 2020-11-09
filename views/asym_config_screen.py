# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asym_config_screenXArKPD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AsymConfigScreen(object):
    def setupUi(self, AsymConfigScreen):
        if not AsymConfigScreen.objectName():
            AsymConfigScreen.setObjectName(u"AsymConfigScreen")
        AsymConfigScreen.resize(1440, 784)
        AsymConfigScreen.setAutoFillBackground(False)
        AsymConfigScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(AsymConfigScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(AsymConfigScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.screen1 = QLabel(self.containerScreen)
        self.screen1.setObjectName(u"screen1")
        self.screen1.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen1, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupCbbTemplate = QGroupBox(self.containerScreen)
        self.groupCbbTemplate.setObjectName(u"groupCbbTemplate")
        self.verticalLayout_20 = QVBoxLayout(self.groupCbbTemplate)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.cbbDisplayType = QComboBox(self.groupCbbTemplate)
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.addItem("")
        self.cbbDisplayType.setObjectName(u"cbbDisplayType")
        self.cbbDisplayType.setAutoFillBackground(False)
        self.cbbDisplayType.setStyleSheet(u"height:22px")

        self.verticalLayout_20.addWidget(self.cbbDisplayType)


        self.horizontalLayout_2.addWidget(self.groupCbbTemplate, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.screen2 = QWidget(self.containerScreen)
        self.screen2.setObjectName(u"screen2")
        self.horizontalLayout_4 = QHBoxLayout(self.screen2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.screen2Left = QPushButton(self.screen2)
        self.screen2Left.setObjectName(u"screen2Left")

        self.horizontalLayout_4.addWidget(self.screen2Left)

        self.screen2Right = QPushButton(self.screen2)
        self.screen2Right.setObjectName(u"screen2Right")

        self.horizontalLayout_4.addWidget(self.screen2Right)


        self.gridLayout.addWidget(self.screen2, 0, 1, 1, 1)

        self.screen3 = QWidget(self.containerScreen)
        self.screen3.setObjectName(u"screen3")
        self.horizontalLayout_5 = QHBoxLayout(self.screen3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.screen3Left = QPushButton(self.screen3)
        self.screen3Left.setObjectName(u"screen3Left")

        self.horizontalLayout_5.addWidget(self.screen3Left)

        self.screen3Right = QPushButton(self.screen3)
        self.screen3Right.setObjectName(u"screen3Right")

        self.horizontalLayout_5.addWidget(self.screen3Right)


        self.gridLayout.addWidget(self.screen3, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(AsymConfigScreen)
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
        self.groupSpinTemplate_4 = QGroupBox(self.containerMid)
        self.groupSpinTemplate_4.setObjectName(u"groupSpinTemplate_4")
        self.verticalLayout_12 = QVBoxLayout(self.groupSpinTemplate_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.inpReCalcFactorLeft = QDoubleSpinBox(self.groupSpinTemplate_4)
        self.inpReCalcFactorLeft.setObjectName(u"inpReCalcFactorLeft")

        self.verticalLayout_12.addWidget(self.inpReCalcFactorLeft)


        self.gridLayout_2.addWidget(self.groupSpinTemplate_4, 1, 1, 1, 1)

        self.groupSpinTemplate_5 = QGroupBox(self.containerMid)
        self.groupSpinTemplate_5.setObjectName(u"groupSpinTemplate_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupSpinTemplate_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.inpPSNR = QSpinBox(self.groupSpinTemplate_5)
        self.inpPSNR.setObjectName(u"inpPSNR")

        self.verticalLayout_15.addWidget(self.inpPSNR)


        self.gridLayout_2.addWidget(self.groupSpinTemplate_5, 2, 0, 1, 1)

        self.groupSpinTemplate_3 = QGroupBox(self.containerMid)
        self.groupSpinTemplate_3.setObjectName(u"groupSpinTemplate_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupSpinTemplate_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.inpC2 = QDoubleSpinBox(self.groupSpinTemplate_3)
        self.inpC2.setObjectName(u"inpC2")
        self.inpC2.setMaximum(99999.000000000000000)

        self.verticalLayout_11.addWidget(self.inpC2)


        self.gridLayout_2.addWidget(self.groupSpinTemplate_3, 1, 0, 1, 1)

        self.groupInputTemplate = QGroupBox(self.containerMid)
        self.groupInputTemplate.setObjectName(u"groupInputTemplate")
        self.verticalLayout_19 = QVBoxLayout(self.groupInputTemplate)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.inpSegments = QLineEdit(self.groupInputTemplate)
        self.inpSegments.setObjectName(u"inpSegments")

        self.verticalLayout_19.addWidget(self.inpSegments)


        self.gridLayout_2.addWidget(self.groupInputTemplate, 2, 2, 1, 1)

        self.grpBoxAmpRate = QGroupBox(self.containerMid)
        self.grpBoxAmpRate.setObjectName(u"grpBoxAmpRate")
        self.verticalLayout_7 = QVBoxLayout(self.grpBoxAmpRate)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.sldAmpRate = QSlider(self.grpBoxAmpRate)
        self.sldAmpRate.setObjectName(u"sldAmpRate")
        self.sldAmpRate.setMaximum(20)
        self.sldAmpRate.setPageStep(5)
        self.sldAmpRate.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.sldAmpRate)


        self.gridLayout_2.addWidget(self.grpBoxAmpRate, 0, 2, 1, 1)

        self.groupSpinTemplate_2 = QGroupBox(self.containerMid)
        self.groupSpinTemplate_2.setObjectName(u"groupSpinTemplate_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupSpinTemplate_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.inpAmpThresh = QDoubleSpinBox(self.groupSpinTemplate_2)
        self.inpAmpThresh.setObjectName(u"inpAmpThresh")

        self.verticalLayout_6.addWidget(self.inpAmpThresh)


        self.gridLayout_2.addWidget(self.groupSpinTemplate_2, 0, 1, 1, 1)

        self.groupSpinTemplate = QGroupBox(self.containerMid)
        self.groupSpinTemplate.setObjectName(u"groupSpinTemplate")
        self.verticalLayout_4 = QVBoxLayout(self.groupSpinTemplate)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.inpC1 = QDoubleSpinBox(self.groupSpinTemplate)
        self.inpC1.setObjectName(u"inpC1")
        self.inpC1.setMaximum(99999.000000000000000)

        self.verticalLayout_4.addWidget(self.inpC1)


        self.gridLayout_2.addWidget(self.groupSpinTemplate, 0, 0, 1, 1)

        self.grpBoxMinSimilarity = QGroupBox(self.containerMid)
        self.grpBoxMinSimilarity.setObjectName(u"grpBoxMinSimilarity")
        self.verticalLayout_13 = QVBoxLayout(self.grpBoxMinSimilarity)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sldMinSimilarity = QSlider(self.grpBoxMinSimilarity)
        self.sldMinSimilarity.setObjectName(u"sldMinSimilarity")
        self.sldMinSimilarity.setMaximum(100)
        self.sldMinSimilarity.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sldMinSimilarity)


        self.gridLayout_2.addWidget(self.grpBoxMinSimilarity, 1, 2, 1, 1)

        self.groupSpinTemplate_6 = QGroupBox(self.containerMid)
        self.groupSpinTemplate_6.setObjectName(u"groupSpinTemplate_6")
        self.verticalLayout_18 = QVBoxLayout(self.groupSpinTemplate_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.inpReCalcFactorRight = QDoubleSpinBox(self.groupSpinTemplate_6)
        self.inpReCalcFactorRight.setObjectName(u"inpReCalcFactorRight")

        self.verticalLayout_18.addWidget(self.inpReCalcFactorRight)


        self.gridLayout_2.addWidget(self.groupSpinTemplate_6, 2, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
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

        self.retranslateUi(AsymConfigScreen)

        QMetaObject.connectSlotsByName(AsymConfigScreen)
    # setupUi

    def retranslateUi(self, AsymConfigScreen):
        AsymConfigScreen.setWindowTitle(QCoreApplication.translate("AsymConfigScreen", u"Form", None))
        self.screen1.setText(QCoreApplication.translate("AsymConfigScreen", u"SCREEN", None))
        self.groupCbbTemplate.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Display Type:", None))
        self.cbbDisplayType.setItemText(0, QCoreApplication.translate("AsymConfigScreen", u"Item 1", None))
        self.cbbDisplayType.setItemText(1, QCoreApplication.translate("AsymConfigScreen", u"Item 2", None))

        self.screen2Left.setText(QCoreApplication.translate("AsymConfigScreen", u"PushButton", None))
        self.screen2Right.setText(QCoreApplication.translate("AsymConfigScreen", u"PushButton", None))
        self.screen3Left.setText(QCoreApplication.translate("AsymConfigScreen", u"PushButton", None))
        self.screen3Right.setText(QCoreApplication.translate("AsymConfigScreen", u"PushButton", None))
        self.lblTitle.setText(QCoreApplication.translate("AsymConfigScreen", u"SAMPLE COMPARISON CONFIG", None))
        self.groupSpinTemplate_4.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Re-calc factor (left)", None))
        self.groupSpinTemplate_5.setTitle(QCoreApplication.translate("AsymConfigScreen", u"PSNR Trigger", None))
        self.groupSpinTemplate_3.setTitle(QCoreApplication.translate("AsymConfigScreen", u"C2", None))
        self.groupInputTemplate.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Segments", None))
        self.inpSegments.setInputMask("")
        self.inpSegments.setText("")
        self.inpSegments.setPlaceholderText(QCoreApplication.translate("AsymConfigScreen", u"Input something", None))
        self.grpBoxAmpRate.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Amplification rate: 0", None))
        self.groupSpinTemplate_2.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Amplification thresh", None))
        self.groupSpinTemplate.setTitle(QCoreApplication.translate("AsymConfigScreen", u"C1", None))
        self.grpBoxMinSimilarity.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Minimum similarity (%): 0", None))
        self.groupSpinTemplate_6.setTitle(QCoreApplication.translate("AsymConfigScreen", u"Re-calc factor (right)", None))
        self.btnBack.setText(QCoreApplication.translate("AsymConfigScreen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("AsymConfigScreen", u"NEXT", None))
    # retranslateUi

