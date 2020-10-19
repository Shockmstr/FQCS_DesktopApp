from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.progress_screen import Ui_ProgressScreen


class ProgressScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)

    # data binding
    def binding(self):
        pass
