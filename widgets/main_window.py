from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.main_window import Ui_MainWindow
from widgets.detection_config_screen_layout import DetectionConfigScreen

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.showFullScreen()
        self.bind_exit_program()
        
        #screen 1
        self.detection_screen = DetectionConfigScreen()
        self.setCentralWidget(self.detection_screen)

        #event handler
    def exit_program(self):
        self.close()

        #binding
    def bind_exit_program(self):
        self.ui.actionExit.triggered.connect(self.exit_program)    