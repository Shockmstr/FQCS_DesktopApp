# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeasurementAndMinScreenrPqtZD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_measurement_screen(object):
    def setupUi(self, measurement_screen):
        if not measurement_screen.objectName():
            measurement_screen.setObjectName(u"measurement_screen")
        measurement_screen.resize(1440, 900)
        measurement_screen.setAutoFillBackground(False)
        measurement_screen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(measurement_screen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(measurement_screen)
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

        self.containerConfig = QWidget(measurement_screen)
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
        self.groupSliderTemplate = QGroupBox(self.containerMid)
        self.groupSliderTemplate.setObjectName(u"groupSliderTemplate")
        self.verticalLayout_11 = QVBoxLayout(self.groupSliderTemplate)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.sliderTemplate = QSlider(self.groupSliderTemplate)
        self.sliderTemplate.setObjectName(u"sliderTemplate")
        self.sliderTemplate.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.sliderTemplate)


        self.gridLayout_2.addWidget(self.groupSliderTemplate, 0, 0, 1, 1)

        self.groupInputTemplate = QGroupBox(self.containerMid)
        self.groupInputTemplate.setObjectName(u"groupInputTemplate")
        self.verticalLayout_14 = QVBoxLayout(self.groupInputTemplate)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.inpTemplate = QLineEdit(self.groupInputTemplate)
        self.inpTemplate.setObjectName(u"inpTemplate")

        self.verticalLayout_14.addWidget(self.inpTemplate)


        self.gridLayout_2.addWidget(self.groupInputTemplate, 1, 1, 1, 1)

        self.groupSliderTemplate_3 = QGroupBox(self.containerMid)
        self.groupSliderTemplate_3.setObjectName(u"groupSliderTemplate_3")
        self.verticalLayout_13 = QVBoxLayout(self.groupSliderTemplate_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sliderTemplate_3 = QSlider(self.groupSliderTemplate_3)
        self.sliderTemplate_3.setObjectName(u"sliderTemplate_3")
        self.sliderTemplate_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sliderTemplate_3)


        self.gridLayout_2.addWidget(self.groupSliderTemplate_3, 0, 2, 1, 1)

        self.groupInputTemplate_2 = QGroupBox(self.containerMid)
        self.groupInputTemplate_2.setObjectName(u"groupInputTemplate_2")
        self.verticalLayout_15 = QVBoxLayout(self.groupInputTemplate_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.inpTemplate_2 = QLineEdit(self.groupInputTemplate_2)
        self.inpTemplate_2.setObjectName(u"inpTemplate_2")

        self.verticalLayout_15.addWidget(self.inpTemplate_2)


        self.gridLayout_2.addWidget(self.groupInputTemplate_2, 0, 1, 1, 1)

        self.groupSliderTemplate_2 = QGroupBox(self.containerMid)
        self.groupSliderTemplate_2.setObjectName(u"groupSliderTemplate_2")
        self.verticalLayout_12 = QVBoxLayout(self.groupSliderTemplate_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.sliderTemplate_2 = QSlider(self.groupSliderTemplate_2)
        self.sliderTemplate_2.setObjectName(u"sliderTemplate_2")
        self.sliderTemplate_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.sliderTemplate_2)


        self.gridLayout_2.addWidget(self.groupSliderTemplate_2, 1, 0, 1, 1)

        self.groupInputTemplate_3 = QGroupBox(self.containerMid)
        self.groupInputTemplate_3.setObjectName(u"groupInputTemplate_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupInputTemplate_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.inpTemplate_3 = QLineEdit(self.groupInputTemplate_3)
        self.inpTemplate_3.setObjectName(u"inpTemplate_3")

        self.verticalLayout_5.addWidget(self.inpTemplate_3)


        self.gridLayout_2.addWidget(self.groupInputTemplate_3, 2, 1, 1, 1)

        self.groupSliderTemplate_4 = QGroupBox(self.containerMid)
        self.groupSliderTemplate_4.setObjectName(u"groupSliderTemplate_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupSliderTemplate_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.sliderTemplate_4 = QSlider(self.groupSliderTemplate_4)
        self.sliderTemplate_4.setObjectName(u"sliderTemplate_4")
        self.sliderTemplate_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.sliderTemplate_4)


        self.gridLayout_2.addWidget(self.groupSliderTemplate_4, 1, 2, 1, 1)

        self.groupInputTemplate_4 = QGroupBox(self.containerMid)
        self.groupInputTemplate_4.setObjectName(u"groupInputTemplate_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupInputTemplate_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.inpTemplate_4 = QLineEdit(self.groupInputTemplate_4)
        self.inpTemplate_4.setObjectName(u"inpTemplate_4")

        self.verticalLayout_7.addWidget(self.inpTemplate_4)


        self.gridLayout_2.addWidget(self.groupInputTemplate_4, 2, 2, 1, 1)


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
        self.btnTemplate = QPushButton(self.containerVerticalBtn)
        self.btnTemplate.setObjectName(u"btnTemplate")

        self.verticalLayout_17.addWidget(self.btnTemplate, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.containerVerticalBtn, 0, Qt.AlignTop)

        self.containerNavBtn = QWidget(self.containerRight)
        self.containerNavBtn.setObjectName(u"containerNavBtn")
        self.horizontalLayout_3 = QHBoxLayout(self.containerNavBtn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnTemplate_2 = QPushButton(self.containerNavBtn)
        self.btnTemplate_2.setObjectName(u"btnTemplate_2")

        self.horizontalLayout_3.addWidget(self.btnTemplate_2)

        self.btnTemplate_3 = QPushButton(self.containerNavBtn)
        self.btnTemplate_3.setObjectName(u"btnTemplate_3")

        self.horizontalLayout_3.addWidget(self.btnTemplate_3)


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

        self.retranslateUi(measurement_screen)

        QMetaObject.connectSlotsByName(measurement_screen)
    # setupUi

    def retranslateUi(self, measurement_screen):
        measurement_screen.setWindowTitle(QCoreApplication.translate("measurement_screen", u"Form", None))
        self.screen1.setText(QCoreApplication.translate("measurement_screen", u"SCREEN", None))
        self.screen2.setText(QCoreApplication.translate("measurement_screen", u"SCREEN", None))
        self.screen3.setText(QCoreApplication.translate("measurement_screen", u"SCREEN", None))
        self.screen4.setText(QCoreApplication.translate("measurement_screen", u"SCREEN", None))
        self.lblTitle.setText(QCoreApplication.translate("measurement_screen", u"DEFINE MEASUREMENT AND MIN AREA", None))
        self.groupSliderTemplate.setTitle(QCoreApplication.translate("measurement_screen", u"Mininum width(%)", None))
        self.groupInputTemplate.setTitle(QCoreApplication.translate("measurement_screen", u"Left side actual length", None))
        self.inpTemplate.setInputMask("")
        self.inpTemplate.setText(QCoreApplication.translate("measurement_screen", u"27", None))
        self.inpTemplate.setPlaceholderText(QCoreApplication.translate("measurement_screen", u"Input something", None))
        self.groupSliderTemplate_3.setTitle(QCoreApplication.translate("measurement_screen", u"Detect position", None))
        self.groupInputTemplate_2.setTitle(QCoreApplication.translate("measurement_screen", u"Left side detected length (px)", None))
        self.inpTemplate_2.setInputMask("")
        self.inpTemplate_2.setText(QCoreApplication.translate("measurement_screen", u"420", None))
        self.inpTemplate_2.setPlaceholderText(QCoreApplication.translate("measurement_screen", u"Input something", None))
        self.groupSliderTemplate_2.setTitle(QCoreApplication.translate("measurement_screen", u"Maxinum height(%)", None))
        self.groupInputTemplate_3.setTitle(QCoreApplication.translate("measurement_screen", u"Length unit", None))
        self.inpTemplate_3.setInputMask("")
        self.inpTemplate_3.setText(QCoreApplication.translate("measurement_screen", u"cm", None))
        self.inpTemplate_3.setPlaceholderText(QCoreApplication.translate("measurement_screen", u"Input something", None))
        self.groupSliderTemplate_4.setTitle(QCoreApplication.translate("measurement_screen", u"Detect range", None))
        self.groupInputTemplate_4.setTitle(QCoreApplication.translate("measurement_screen", u"Allow difference ({unit})", None))
        self.inpTemplate_4.setInputMask("")
        self.inpTemplate_4.setText(QCoreApplication.translate("measurement_screen", u"0.5", None))
        self.inpTemplate_4.setPlaceholderText(QCoreApplication.translate("measurement_screen", u"Input something", None))
        self.btnTemplate.setText(QCoreApplication.translate("measurement_screen", u"CAPTURE", None))
        self.btnTemplate_2.setText(QCoreApplication.translate("measurement_screen", u"BACK", None))
        self.btnTemplate_3.setText(QCoreApplication.translate("measurement_screen", u"NEXT", None))
    # retranslateUi

