# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_widgetrtoWcH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageWidget(object):
    def setupUi(self, ImageWidget):
        if not ImageWidget.objectName():
            ImageWidget.setObjectName(u"ImageWidget")
        ImageWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ImageWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblImage = QLabel(ImageWidget)
        self.lblImage.setObjectName(u"lblImage")

        self.verticalLayout.addWidget(self.lblImage)


        self.retranslateUi(ImageWidget)

        QMetaObject.connectSlotsByName(ImageWidget)
    # setupUi

    def retranslateUi(self, ImageWidget):
        ImageWidget.setWindowTitle(QCoreApplication.translate("ImageWidget", u"Form", None))
        self.lblImage.setText("")
    # retranslateUi

