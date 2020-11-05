from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.progress_screen import Ui_ProgressScreen


class ProgressScreen(QWidget):
    stopped: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        self.stopped = self.ui.btnStop.clicked
        self.binding()

    # data binding
    def binding(self):
        return