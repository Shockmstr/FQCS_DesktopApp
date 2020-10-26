from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.progress_screen import Ui_ProgressScreen


class ProgressScreen(QWidget):
    def __init__(self, homeScreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        self.binding(homeScreen = homeScreen)
        
    # data binding
    def binding(self, homeScreen: ()):
        self.ui.btnStop.clicked.connect(homeScreen)
