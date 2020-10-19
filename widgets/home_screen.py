from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.home_screen import Ui_HomeScreen


class ProgressScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)

    # data binding
    def binding(self):
