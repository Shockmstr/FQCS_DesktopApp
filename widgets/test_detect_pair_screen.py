from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.test_detect_pair_screen import Ui_test_detect_pair_screen

class TestDetectPairScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_test_detect_pair_screen()
        self.ui.setupUi(self)

    


