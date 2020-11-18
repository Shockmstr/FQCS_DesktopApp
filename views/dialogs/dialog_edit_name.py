# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_edit_nameotXhzu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogEditName(object):
    def setupUi(self, DialogEditName):
        if not DialogEditName.objectName():
            DialogEditName.setObjectName(u"DialogEditName")
        DialogEditName.resize(483, 122)
        self.verticalLayout = QVBoxLayout(DialogEditName)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inpEditName = QLineEdit(DialogEditName)
        self.inpEditName.setObjectName(u"inpEditName")

        self.verticalLayout.addWidget(self.inpEditName)

        self.dialogEditNameBtnBox = QDialogButtonBox(DialogEditName)
        self.dialogEditNameBtnBox.setObjectName(u"dialogEditNameBtnBox")
        self.dialogEditNameBtnBox.setOrientation(Qt.Horizontal)
        self.dialogEditNameBtnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.dialogEditNameBtnBox)


        self.retranslateUi(DialogEditName)
        self.dialogEditNameBtnBox.accepted.connect(DialogEditName.accept)
        self.dialogEditNameBtnBox.rejected.connect(DialogEditName.reject)

        QMetaObject.connectSlotsByName(DialogEditName)
    # setupUi

    def retranslateUi(self, DialogEditName):
        DialogEditName.setWindowTitle(QCoreApplication.translate("DialogEditName", u"Edit name", None))
        self.inpEditName.setInputMask("")
        self.inpEditName.setText("")
        self.inpEditName.setPlaceholderText(QCoreApplication.translate("DialogEditName", u"Input name", None))
    # retranslateUi

