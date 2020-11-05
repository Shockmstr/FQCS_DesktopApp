# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_preprocess_config_screenpJYSDo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_color_preprocess_config_screen(object):
    def setupUi(self, color_preprocess_config_screen):
        if not color_preprocess_config_screen.objectName():
            color_preprocess_config_screen.setObjectName(u"color_preprocess_config_screen")
        color_preprocess_config_screen.resize(1440, 900)
        color_preprocess_config_screen.setAutoFillBackground(False)
        color_preprocess_config_screen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(color_preprocess_config_screen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(color_preprocess_config_screen)
        self.containerScreen.setObjectName(u"containerScreen")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerScreen.sizePolicy().hasHeightForWidth())
        self.containerScreen.setSizePolicy(sizePolicy)
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


        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(color_preprocess_config_screen)
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

        self.verticalLayout_10.addWidget(self.chkColorCompare, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.verticalLayout_10.setStretch(0, 1)

        self.horizontalLayout.addWidget(self.containerLeft)

        self.containerMid = QWidget(self.containerParam)
        self.containerMid.setObjectName(u"containerMid")
        self.containerMid.setStyleSheet(u"#containerMid {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.gridLayout_2 = QGridLayout(self.containerMid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupCbbResize = QGroupBox(self.containerMid)
        self.groupCbbResize.setObjectName(u"groupCbbResize")
        self.horizontalLayout_4 = QHBoxLayout(self.groupCbbResize)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.cbbResizeWidth = QComboBox(self.groupCbbResize)
        self.cbbResizeWidth.addItem("")
        self.cbbResizeWidth.addItem("")
        self.cbbResizeWidth.setObjectName(u"cbbResizeWidth")
        self.cbbResizeWidth.setAutoFillBackground(False)
        self.cbbResizeWidth.setStyleSheet(u"height:22px")
        self.cbbResizeWidth.setFrame(True)

        self.horizontalLayout_4.addWidget(self.cbbResizeWidth)

        self.cbbResizeHeight = QComboBox(self.groupCbbResize)
        self.cbbResizeHeight.addItem("")
        self.cbbResizeHeight.addItem("")
        self.cbbResizeHeight.setObjectName(u"cbbResizeHeight")
        self.cbbResizeHeight.setAutoFillBackground(False)
        self.cbbResizeHeight.setStyleSheet(u"height:22px")
        self.cbbResizeHeight.setFrame(True)

        self.horizontalLayout_4.addWidget(self.cbbResizeHeight)


        self.gridLayout_2.addWidget(self.groupCbbResize, 0, 0, 1, 1)

        self.groupSldBrightLeft = QGroupBox(self.containerMid)
        self.groupSldBrightLeft.setObjectName(u"groupSldBrightLeft")
        self.verticalLayout_12 = QVBoxLayout(self.groupSldBrightLeft)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.sldBrightLeft = QSlider(self.groupSldBrightLeft)
        self.sldBrightLeft.setObjectName(u"sldBrightLeft")
        self.sldBrightLeft.setMaximum(30)
        self.sldBrightLeft.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.sldBrightLeft)


        self.gridLayout_2.addWidget(self.groupSldBrightLeft, 0, 1, 1, 1)

        self.groupSldConstrastLeft = QGroupBox(self.containerMid)
        self.groupSldConstrastLeft.setObjectName(u"groupSldConstrastLeft")
        self.verticalLayout_6 = QVBoxLayout(self.groupSldConstrastLeft)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.sldConstrastLeft = QSlider(self.groupSldConstrastLeft)
        self.sldConstrastLeft.setObjectName(u"sldConstrastLeft")
        self.sldConstrastLeft.setMinimum(-40)
        self.sldConstrastLeft.setMaximum(40)
        self.sldConstrastLeft.setValue(-40)
        self.sldConstrastLeft.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.sldConstrastLeft)


        self.gridLayout_2.addWidget(self.groupSldConstrastLeft, 1, 1, 1, 1)

        self.groupSldBrightRight = QGroupBox(self.containerMid)
        self.groupSldBrightRight.setObjectName(u"groupSldBrightRight")
        self.verticalLayout_13 = QVBoxLayout(self.groupSldBrightRight)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sldBrightRight = QSlider(self.groupSldBrightRight)
        self.sldBrightRight.setObjectName(u"sldBrightRight")
        self.sldBrightRight.setMaximum(30)
        self.sldBrightRight.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sldBrightRight)


        self.gridLayout_2.addWidget(self.groupSldBrightRight, 0, 2, 1, 1)

        self.groupSldBlur = QGroupBox(self.containerMid)
        self.groupSldBlur.setObjectName(u"groupSldBlur")
        self.verticalLayout_3 = QVBoxLayout(self.groupSldBlur)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.sldBlur = QSlider(self.groupSldBlur)
        self.sldBlur.setObjectName(u"sldBlur")
        self.sldBlur.setMaximum(100)
        self.sldBlur.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.sldBlur)


        self.gridLayout_2.addWidget(self.groupSldBlur, 1, 0, 1, 1)

        self.groupSldSaturation = QGroupBox(self.containerMid)
        self.groupSldSaturation.setObjectName(u"groupSldSaturation")
        self.verticalLayout_4 = QVBoxLayout(self.groupSldSaturation)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.sldSaturation = QSlider(self.groupSldSaturation)
        self.sldSaturation.setObjectName(u"sldSaturation")
        self.sldSaturation.setMaximum(10)
        self.sldSaturation.setPageStep(2)
        self.sldSaturation.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.sldSaturation)


        self.gridLayout_2.addWidget(self.groupSldSaturation, 2, 0, 1, 1)

        self.groupSldConstrastRight = QGroupBox(self.containerMid)
        self.groupSldConstrastRight.setObjectName(u"groupSldConstrastRight")
        self.verticalLayout_7 = QVBoxLayout(self.groupSldConstrastRight)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.sldConstrastRight = QSlider(self.groupSldConstrastRight)
        self.sldConstrastRight.setObjectName(u"sldConstrastRight")
        self.sldConstrastRight.setMinimum(-40)
        self.sldConstrastRight.setMaximum(40)
        self.sldConstrastRight.setValue(-40)
        self.sldConstrastRight.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.sldConstrastRight)


        self.gridLayout_2.addWidget(self.groupSldConstrastRight, 1, 2, 1, 1)


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

        self.retranslateUi(color_preprocess_config_screen)

        QMetaObject.connectSlotsByName(color_preprocess_config_screen)
    # setupUi

    def retranslateUi(self, color_preprocess_config_screen):
        color_preprocess_config_screen.setWindowTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Form", None))
        self.screen1.setText(QCoreApplication.translate("color_preprocess_config_screen", u"SCREEN", None))
        self.screen2.setText(QCoreApplication.translate("color_preprocess_config_screen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("color_preprocess_config_screen", u"COLOR COMPARISION - PREPROCESS", None))
        self.chkColorCompare.setText(QCoreApplication.translate("color_preprocess_config_screen", u"Enable Color Comparison", None))
        self.groupCbbResize.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Resize (Width - Height)", None))
        self.cbbResizeWidth.setItemText(0, QCoreApplication.translate("color_preprocess_config_screen", u"Item 1", None))
        self.cbbResizeWidth.setItemText(1, QCoreApplication.translate("color_preprocess_config_screen", u"Item 2", None))

        self.cbbResizeHeight.setItemText(0, QCoreApplication.translate("color_preprocess_config_screen", u"Item 1", None))
        self.cbbResizeHeight.setItemText(1, QCoreApplication.translate("color_preprocess_config_screen", u"Item 2", None))

        self.groupSldBrightLeft.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Brightness left: 0", None))
        self.groupSldConstrastLeft.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Contrast left: -200", None))
        self.groupSldBrightRight.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Brightness right: 0", None))
        self.groupSldBlur.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Blur: 0", None))
        self.groupSldSaturation.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Saturation: 0", None))
        self.groupSldConstrastRight.setTitle(QCoreApplication.translate("color_preprocess_config_screen", u"Contrast right: -200", None))
        self.btnBack.setText(QCoreApplication.translate("color_preprocess_config_screen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("color_preprocess_config_screen", u"NEXT", None))
    # retranslateUi

