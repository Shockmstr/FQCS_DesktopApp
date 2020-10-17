from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.color_preprocess_config_screen import Ui_color_preprocess_config_screen

class ColorPreprocessConfigScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_color_preprocess_config_screen()
        self.ui.setupUi(self)
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen:(), nextscreen: ()):
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnNext.clicked.connect(nextscreen)

