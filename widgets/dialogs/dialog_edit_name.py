from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Signal, Qt
from views.dialogs.dialog_edit_name import Ui_DialogEditName


class DialogEditName(QDialog):
    def __init__(self, current_name=None, parent=None):
        QDialog.__init__(self, parent)
        self.__current_name = current_name
        self.ui = Ui_DialogEditName()
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        self.ui.inpEditName.setText(self.__current_name)

    def get_inp_edit_name(self):
        return self.ui.inpEditName.text()

    # binding
    def binding(self):
        return
