from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.home_screen import Ui_HomeScreen


class HomeScreen(QWidget):
    def __init__(self, configScreen: (), progressScreen: (), on_exit: ()):
        QWidget.__init__(self)
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)
        self.binding(configScreen = configScreen, progressScreen = progressScreen, on_exit = on_exit)

    # data binding
    def binding(self, configScreen: (), progressScreen: (), on_exit: ()):
        self.ui.btnEditConfig.clicked.connect(configScreen)
        self.ui.btnStart.clicked.connect(progressScreen)
        self.ui.btnExit.clicked.connect(on_exit)