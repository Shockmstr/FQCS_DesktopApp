from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.main_window import Ui_MainWindow
from widgets.measurement_screen import MeasurementScreen
from widgets.test_detect_pair_screen import TestDetectPairScreen
from widgets.color_preprocess_config_screen import ColorPreprocessConfigScreen

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.bind_exit_program()
        
        #screen 2
        self.measurement_screen = MeasurementScreen()
        # self.setCentralWidget(self.measurement_screen)

        #screen 3
        self.test_detect_pair_screen = TestDetectPairScreen()
        # self.setCentralWidget(self.test_detect_pair_screen)

        #screen 4
        self.color_preprocess_config_screen = ColorPreprocessConfigScreen()
        self.setCentralWidget(self.color_preprocess_config_screen)

        #event handler
    def exit_program(self):
        self.close()

        #binding
    def bind_exit_program(self):
        self.ui.actionExit.triggered.connect(self.exit_program)    