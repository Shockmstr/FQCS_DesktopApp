from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.error_detect_screen import Ui_ErrorDetectScreen


class ErrorDetectScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_ErrorDetectScreen()
        self.ui.setupUi(self)
        self.bind_backscreen(backscreen=backscreen)
        self.bind_nextscreen(nextscreen=nextscreen)

    # data binding
    def binding(self):
        self.ui.btnNext.clicked.connect(nextscreen)
        self.ui.btnBack.clicked.connect(backscreen)
