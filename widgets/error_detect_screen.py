from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.error_detect_screen import Ui_ErrorDetectScreen


class ErrorDetectScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_ErrorDetectScreen()
        self.ui.setupUi(self)
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen: (), nextscreen: ()):
        self.ui.btnFinish.clicked.connect(nextscreen)
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnFinish.clicked.connect(nextscreen)
