from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.login_screen import Ui_LoginScreen


class LoginScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.binding()
        self.showFullScreen()

    # data binding
    def binding(self):
        return