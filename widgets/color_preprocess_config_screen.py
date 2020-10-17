from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.color_preprocess_config_screen import Ui_color_preprocess_config_screen

class ColorPreprocessConfigScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.iu = Ui_color_preprocess_config_screen()
        self.iu.setupUi(self)

        self.bind_backscreen(backscreen=backscreen)
        self.bind_nextscreen(nextscreen=nextscreen)

    #data binding
    def bind_backsreen(self, backscreen: ()):
        self.ui.btnBack.clicked.connect(backscreen)

    def bind_nextscreen(self, nextscreen: ()):
        self.ui.btnNext.clicked.conncet(nextscreen)


