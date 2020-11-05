from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.home_screen import Ui_HomeScreen


class HomeScreen(QWidget):
    action_edit: Signal
    action_start: Signal
    action_exit: Signal
    action_logout: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)
        self.action_edit = self.ui.btnEditConfig.clicked
        self.action_start = self.ui.btnStart.clicked
        self.action_exit = self.ui.btnExit.clicked
        self.action_logout = self.ui.btnLogout.clicked
        self.binding()

    # data binding
    def binding(self):
        return
