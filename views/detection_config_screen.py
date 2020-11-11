# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detection_config_screenDfhtdZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DetectionConfigScreen(object):
    def setupUi(self, DetectionConfigScreen):
        if not DetectionConfigScreen.objectName():
            DetectionConfigScreen.setObjectName(u"DetectionConfigScreen")
        DetectionConfigScreen.resize(1355, 792)
        DetectionConfigScreen.setAutoFillBackground(False)
        DetectionConfigScreen.setStyleSheet(u"background:#E5E5E5")
        self.verticalLayout = QVBoxLayout(DetectionConfigScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.containerScreen = QWidget(DetectionConfigScreen)
        self.containerScreen.setObjectName(u"containerScreen")
        self.containerScreen.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.containerScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.screen2 = QLabel(self.containerScreen)
        self.screen2.setObjectName(u"screen2")
        self.screen2.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen2, 0, 1, 1, 1)

        self.screen1 = QLabel(self.containerScreen)
        self.screen1.setObjectName(u"screen1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen1.sizePolicy().hasHeightForWidth())
        self.screen1.setSizePolicy(sizePolicy)
        self.screen1.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen1, 0, 0, 1, 1)

        self.screen3 = QLabel(self.containerScreen)
        self.screen3.setObjectName(u"screen3")
        self.screen3.setStyleSheet(u"background-color: #AFF;font-weight:bold;")
        self.screen3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.screen3, 1, 0, 1, 1)

        self.screen4 = QWidget(self.containerScreen)
        self.screen4.setObjectName(u"screen4")
        self.gridLayout_7 = QGridLayout(self.screen4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_2 = QWidget(self.screen4)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupCbbTemplate = QGroupBox(self.widget_2)
        self.groupCbbTemplate.setObjectName(u"groupCbbTemplate")
        self.verticalLayout_3 = QVBoxLayout(self.groupCbbTemplate)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.txtNewCamera = QLineEdit(self.groupCbbTemplate)
        self.txtNewCamera.setObjectName(u"txtNewCamera")
        self.txtNewCamera.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.txtNewCamera)


        self.horizontalLayout_2.addWidget(self.groupCbbTemplate)

        self.btnAdd = QToolButton(self.widget_2)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)

        self.gridLayout_7.addWidget(self.widget_2, 0, 1, 1, 1)

        self.tblCameraConfig = QTableWidget(self.screen4)
        if (self.tblCameraConfig.columnCount() < 2):
            self.tblCameraConfig.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCameraConfig.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCameraConfig.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblCameraConfig.setObjectName(u"tblCameraConfig")
        self.tblCameraConfig.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblCameraConfig.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblCameraConfig.setRowCount(0)
        self.tblCameraConfig.setColumnCount(2)

        self.gridLayout_7.addWidget(self.tblCameraConfig, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.screen4, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.containerScreen)

        self.containerConfig = QWidget(DetectionConfigScreen)
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
        self.groubCbbCamera = QGroupBox(self.containerLeft)
        self.groubCbbCamera.setObjectName(u"groubCbbCamera")
        self.verticalLayout_7 = QVBoxLayout(self.groubCbbCamera)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.cbbCamera = QComboBox(self.groubCbbCamera)
        self.cbbCamera.addItem("")
        self.cbbCamera.addItem("")
        self.cbbCamera.setObjectName(u"cbbCamera")
        self.cbbCamera.setAutoFillBackground(False)
        self.cbbCamera.setStyleSheet(u"height:22px")
        self.cbbCamera.setFrame(True)

        self.verticalLayout_7.addWidget(self.cbbCamera)


        self.verticalLayout_10.addWidget(self.groubCbbCamera)

        self.groupCbbResize = QGroupBox(self.containerLeft)
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
        self.cbbWidth.setFrame(True)

        self.horizontalLayout_4.addWidget(self.cbbWidth)

        self.cbbHeight = QComboBox(self.groupCbbResize)
        self.cbbHeight.setObjectName(u"cbbHeight")
        self.cbbHeight.setStyleSheet(u"height:22px")

        self.horizontalLayout_4.addWidget(self.cbbHeight)


        self.verticalLayout_10.addWidget(self.groupCbbResize)

        self.groupCbbMethod = QGroupBox(self.containerLeft)
        self.groupCbbMethod.setObjectName(u"groupCbbMethod")
        self.verticalLayout_9 = QVBoxLayout(self.groupCbbMethod)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.cbbMethod = QComboBox(self.groupCbbMethod)
        self.cbbMethod.addItem("")
        self.cbbMethod.addItem("")
        self.cbbMethod.setObjectName(u"cbbMethod")
        self.cbbMethod.setAutoFillBackground(False)
        self.cbbMethod.setStyleSheet(u"height:22px")
        self.cbbMethod.setFrame(True)

        self.verticalLayout_9.addWidget(self.cbbMethod)


        self.verticalLayout_10.addWidget(self.groupCbbMethod)


        self.horizontalLayout.addWidget(self.containerLeft)

        self.stackContainerMid = QStackedWidget(self.containerParam)
        self.stackContainerMid.setObjectName(u"stackContainerMid")
        self.stackContainerMid.setStyleSheet(u"#stackContainerMid {\n"
"	border: 1px solid #A5A5A5\n"
"}")
        self.containerMidEdge = QWidget()
        self.containerMidEdge.setObjectName(u"containerMidEdge")
        self.gridLayout_2 = QGridLayout(self.containerMidEdge)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.grbboxSldContrast = QGroupBox(self.containerMidEdge)
        self.grbboxSldContrast.setObjectName(u"grbboxSldContrast")
        self.verticalLayout_12 = QVBoxLayout(self.grbboxSldContrast)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.sldContrast = QSlider(self.grbboxSldContrast)
        self.sldContrast.setObjectName(u"sldContrast")
        self.sldContrast.setMinimum(-40)
        self.sldContrast.setMaximum(40)
        self.sldContrast.setSingleStep(1)
        self.sldContrast.setPageStep(5)
        self.sldContrast.setValue(-40)
        self.sldContrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.sldContrast)


        self.gridLayout_2.addWidget(self.grbboxSldContrast, 5, 4, 1, 1)

        self.grbboxSldErode = QGroupBox(self.containerMidEdge)
        self.grbboxSldErode.setObjectName(u"grbboxSldErode")
        self.verticalLayout_14 = QVBoxLayout(self.grbboxSldErode)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.sldErode = QSlider(self.grbboxSldErode)
        self.sldErode.setObjectName(u"sldErode")
        self.sldErode.setMaximum(10)
        self.sldErode.setPageStep(2)
        self.sldErode.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.sldErode)


        self.gridLayout_2.addWidget(self.grbboxSldErode, 6, 7, 1, 1)

        self.grbboxSldDilate = QGroupBox(self.containerMidEdge)
        self.grbboxSldDilate.setObjectName(u"grbboxSldDilate")
        self.verticalLayout_18 = QVBoxLayout(self.grbboxSldDilate)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.sldDilate = QSlider(self.grbboxSldDilate)
        self.sldDilate.setObjectName(u"sldDilate")
        self.sldDilate.setMaximum(10)
        self.sldDilate.setPageStep(2)
        self.sldDilate.setOrientation(Qt.Horizontal)

        self.verticalLayout_18.addWidget(self.sldDilate)


        self.gridLayout_2.addWidget(self.grbboxSldDilate, 5, 7, 1, 1)

        self.grpboxSldBlur = QGroupBox(self.containerMidEdge)
        self.grpboxSldBlur.setObjectName(u"grpboxSldBlur")
        self.verticalLayout_19 = QVBoxLayout(self.grpboxSldBlur)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.sldBlur = QSlider(self.grpboxSldBlur)
        self.sldBlur.setObjectName(u"sldBlur")
        self.sldBlur.setMaximum(10)
        self.sldBlur.setPageStep(2)
        self.sldBlur.setOrientation(Qt.Horizontal)

        self.verticalLayout_19.addWidget(self.sldBlur)


        self.gridLayout_2.addWidget(self.grpboxSldBlur, 0, 7, 1, 1)

        self.grpboxSldBrightness = QGroupBox(self.containerMidEdge)
        self.grpboxSldBrightness.setObjectName(u"grpboxSldBrightness")
        self.verticalLayout_20 = QVBoxLayout(self.grpboxSldBrightness)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.sldBrightness = QSlider(self.grpboxSldBrightness)
        self.sldBrightness.setObjectName(u"sldBrightness")
        self.sldBrightness.setMaximum(30)
        self.sldBrightness.setSingleStep(1)
        self.sldBrightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_20.addWidget(self.sldBrightness)


        self.gridLayout_2.addWidget(self.grpboxSldBrightness, 0, 4, 1, 1)

        self.grbboxSldThreshold = QGroupBox(self.containerMidEdge)
        self.grbboxSldThreshold.setObjectName(u"grbboxSldThreshold")
        self.verticalLayout_13 = QVBoxLayout(self.grbboxSldThreshold)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sldThreshold1 = QSlider(self.grbboxSldThreshold)
        self.sldThreshold1.setObjectName(u"sldThreshold1")
        self.sldThreshold1.setMaximum(51)
        self.sldThreshold1.setSingleStep(1)
        self.sldThreshold1.setPageStep(5)
        self.sldThreshold1.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sldThreshold1)


        self.gridLayout_2.addWidget(self.grbboxSldThreshold, 0, 6, 1, 1)

        self.grbboxSldThreshold2 = QGroupBox(self.containerMidEdge)
        self.grbboxSldThreshold2.setObjectName(u"grbboxSldThreshold2")
        self.verticalLayout_15 = QVBoxLayout(self.grbboxSldThreshold2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.sldThreshold2 = QSlider(self.grbboxSldThreshold2)
        self.sldThreshold2.setObjectName(u"sldThreshold2")
        self.sldThreshold2.setMaximum(51)
        self.sldThreshold2.setSingleStep(1)
        self.sldThreshold2.setPageStep(5)
        self.sldThreshold2.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.sldThreshold2)


        self.gridLayout_2.addWidget(self.grbboxSldThreshold2, 5, 6, 1, 1)

        self.stackContainerMid.addWidget(self.containerMidEdge)
        self.containerMidThresh = QWidget()
        self.containerMidThresh.setObjectName(u"containerMidThresh")
        self.gridLayout_3 = QGridLayout(self.containerMidThresh)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.subContainer = QWidget(self.containerMidThresh)
        self.subContainer.setObjectName(u"subContainer")
        self.subContainer.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.subContainer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.grpboxLightAdj = QGroupBox(self.subContainer)
        self.grpboxLightAdj.setObjectName(u"grpboxLightAdj")
        self.verticalLayout_23 = QVBoxLayout(self.grpboxLightAdj)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.sldLightAdj = QSlider(self.grpboxLightAdj)
        self.sldLightAdj.setObjectName(u"sldLightAdj")
        self.sldLightAdj.setMaximum(255)
        self.sldLightAdj.setPageStep(5)
        self.sldLightAdj.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.sldLightAdj)


        self.gridLayout_4.addWidget(self.grpboxLightAdj, 1, 0, 1, 1)

        self.grpboxBkgThreshold = QGroupBox(self.subContainer)
        self.grpboxBkgThreshold.setObjectName(u"grpboxBkgThreshold")
        sizePolicy.setHeightForWidth(self.grpboxBkgThreshold.sizePolicy().hasHeightForWidth())
        self.grpboxBkgThreshold.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.grpboxBkgThreshold)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.sldBkgThresh = QSlider(self.grpboxBkgThreshold)
        self.sldBkgThresh.setObjectName(u"sldBkgThresh")
        self.sldBkgThresh.setMaximum(255)
        self.sldBkgThresh.setPageStep(5)
        self.sldBkgThresh.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.sldBkgThresh)


        self.gridLayout_4.addWidget(self.grpboxBkgThreshold, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 2, 1)

        self.grpCkbInvertThresh = QWidget(self.subContainer)
        self.grpCkbInvertThresh.setObjectName(u"grpCkbInvertThresh")
        self.verticalLayout_3 = QVBoxLayout(self.grpCkbInvertThresh)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ckbInvertThresh = QCheckBox(self.grpCkbInvertThresh)
        self.ckbInvertThresh.setObjectName(u"ckbInvertThresh")

        self.verticalLayout_3.addWidget(self.ckbInvertThresh)


        self.gridLayout_4.addWidget(self.grpCkbInvertThresh, 2, 0, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)

        self.gridLayout_3.addWidget(self.subContainer, 0, 0, 1, 1)

        self.stackContainerMid.addWidget(self.containerMidThresh)
        self.containerMidRange = QWidget()
        self.containerMidRange.setObjectName(u"containerMidRange")
        self.gridLayout_6 = QGridLayout(self.containerMidRange)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.subContainerRange = QWidget(self.containerMidRange)
        self.subContainerRange.setObjectName(u"subContainerRange")
        self.subContainerRange.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.subContainerRange)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupColorPickerTemplate = QGroupBox(self.subContainerRange)
        self.groupColorPickerTemplate.setObjectName(u"groupColorPickerTemplate")
        self.horizontalLayout_5 = QHBoxLayout(self.groupColorPickerTemplate)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.btnColorFrom = QPushButton(self.groupColorPickerTemplate)
        self.btnColorFrom.setObjectName(u"btnColorFrom")
        self.btnColorFrom.setStyleSheet(u"background-color:#F33")

        self.horizontalLayout_5.addWidget(self.btnColorFrom)

        self.lblConnectTemplate_2 = QLabel(self.groupColorPickerTemplate)
        self.lblConnectTemplate_2.setObjectName(u"lblConnectTemplate_2")
        self.lblConnectTemplate_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lblConnectTemplate_2)

        self.btnColorTo = QPushButton(self.groupColorPickerTemplate)
        self.btnColorTo.setObjectName(u"btnColorTo")
        self.btnColorTo.setStyleSheet(u"background-color:#3F3")

        self.horizontalLayout_5.addWidget(self.btnColorTo)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 4)

        self.gridLayout_5.addWidget(self.groupColorPickerTemplate, 0, 0, 1, 1)

        self.grpboxLightAdjRange = QGroupBox(self.subContainerRange)
        self.grpboxLightAdjRange.setObjectName(u"grpboxLightAdjRange")
        self.verticalLayout_24 = QVBoxLayout(self.grpboxLightAdjRange)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.sldLightAdjRange = QSlider(self.grpboxLightAdjRange)
        self.sldLightAdjRange.setObjectName(u"sldLightAdjRange")
        self.sldLightAdjRange.setMaximum(255)
        self.sldLightAdjRange.setPageStep(5)
        self.sldLightAdjRange.setOrientation(Qt.Horizontal)

        self.verticalLayout_24.addWidget(self.sldLightAdjRange)


        self.gridLayout_5.addWidget(self.grpboxLightAdjRange, 1, 0, 1, 1)

        self.grpCkbInvertRange = QWidget(self.subContainerRange)
        self.grpCkbInvertRange.setObjectName(u"grpCkbInvertRange")
        self.verticalLayout_4 = QVBoxLayout(self.grpCkbInvertRange)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ckbInvertRange = QCheckBox(self.grpCkbInvertRange)
        self.ckbInvertRange.setObjectName(u"ckbInvertRange")

        self.verticalLayout_4.addWidget(self.ckbInvertRange)


        self.gridLayout_5.addWidget(self.grpCkbInvertRange, 2, 0, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 3)

        self.gridLayout_6.addWidget(self.subContainerRange, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.stackContainerMid.addWidget(self.containerMidRange)

        self.horizontalLayout.addWidget(self.stackContainerMid)

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

        self.retranslateUi(DetectionConfigScreen)

        self.cbbHeight.setCurrentIndex(-1)
        self.stackContainerMid.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(DetectionConfigScreen)
    # setupUi

    def retranslateUi(self, DetectionConfigScreen):
        DetectionConfigScreen.setWindowTitle(QCoreApplication.translate("DetectionConfigScreen", u"Detection Config Screen", None))
        self.screen2.setText(QCoreApplication.translate("DetectionConfigScreen", u"SCREEN", None))
        self.screen1.setText(QCoreApplication.translate("DetectionConfigScreen", u"SCREEN", None))
        self.screen3.setText(QCoreApplication.translate("DetectionConfigScreen", u"SCREEN", None))
        self.groupCbbTemplate.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Add New", None))
        self.txtNewCamera.setPlaceholderText(QCoreApplication.translate("DetectionConfigScreen", u"Name", None))
        self.btnAdd.setText(QCoreApplication.translate("DetectionConfigScreen", u"+", None))
        ___qtablewidgetitem = self.tblCameraConfig.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DetectionConfigScreen", u"Camera Name", None));
        ___qtablewidgetitem1 = self.tblCameraConfig.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DetectionConfigScreen", u"Role", None));
        self.lblTitle.setText(QCoreApplication.translate("DetectionConfigScreen", u"DEFINE SAMPLE MODEL", None))
        self.groubCbbCamera.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Camera", None))
        self.cbbCamera.setItemText(0, QCoreApplication.translate("DetectionConfigScreen", u"Item 1", None))
        self.cbbCamera.setItemText(1, QCoreApplication.translate("DetectionConfigScreen", u"Item 2", None))

        self.cbbCamera.setPlaceholderText(QCoreApplication.translate("DetectionConfigScreen", u"Select Camera", None))
        self.groupCbbResize.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Resize (Width - Height)", None))
        self.cbbWidth.setItemText(0, QCoreApplication.translate("DetectionConfigScreen", u"Item 1", None))
        self.cbbWidth.setItemText(1, QCoreApplication.translate("DetectionConfigScreen", u"Item 2", None))

        self.cbbWidth.setPlaceholderText(QCoreApplication.translate("DetectionConfigScreen", u"Width", None))
        self.cbbHeight.setCurrentText(QCoreApplication.translate("DetectionConfigScreen", u"Height", None))
        self.cbbHeight.setPlaceholderText(QCoreApplication.translate("DetectionConfigScreen", u"Height", None))
        self.groupCbbMethod.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Method", None))
        self.cbbMethod.setItemText(0, QCoreApplication.translate("DetectionConfigScreen", u"Item 1", None))
        self.cbbMethod.setItemText(1, QCoreApplication.translate("DetectionConfigScreen", u"Item 2", None))

        self.cbbMethod.setPlaceholderText(QCoreApplication.translate("DetectionConfigScreen", u"Select Method", None))
        self.grbboxSldContrast.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Contrast: -200", None))
        self.grbboxSldErode.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Erode: 0", None))
        self.grbboxSldDilate.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Dilate: 0", None))
        self.grpboxSldBlur.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Blur: 0", None))
        self.grpboxSldBrightness.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Brightness: 0", None))
        self.grbboxSldThreshold.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Threshold 1: 0", None))
        self.grbboxSldThreshold2.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Threshold 2: 0", None))
        self.grpboxLightAdj.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Light Adjustment: 0", None))
        self.grpboxBkgThreshold.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Background Threshold: 0", None))
        self.ckbInvertThresh.setText(QCoreApplication.translate("DetectionConfigScreen", u"Invert", None))
        self.groupColorPickerTemplate.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Color Range", None))
        self.btnColorFrom.setText("")
        self.lblConnectTemplate_2.setText(QCoreApplication.translate("DetectionConfigScreen", u"---", None))
        self.btnColorTo.setText("")
        self.grpboxLightAdjRange.setTitle(QCoreApplication.translate("DetectionConfigScreen", u"Light Adjustment: 0", None))
        self.ckbInvertRange.setText(QCoreApplication.translate("DetectionConfigScreen", u"Invert", None))
        self.btnCapture.setText(QCoreApplication.translate("DetectionConfigScreen", u"CAPTURE", None))
        self.btnBack.setText(QCoreApplication.translate("DetectionConfigScreen", u"BACK", None))
        self.btnNext.setText(QCoreApplication.translate("DetectionConfigScreen", u"NEXT", None))
    # retranslateUi

