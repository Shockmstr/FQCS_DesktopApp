from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.main_window import Ui_MainWindow
from widgets.measurement_screen import MeasurementScreen
from widgets.test_detect_pair_screen import TestDetectPairScreen
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
        self.detection_screen = DetectionConfigScreen(nextscreen=self.change_measurement_screen)

        #screen 2
        self.measurement_screen = MeasurementScreen(backscreen=self.change_detection_screen, nextscreen=self.change_detect_pair_screen)

        #screen 3
        self.test_detect_pair_screen = TestDetectPairScreen(backscreen=self.change_measurement_screen, nextscreen=None)

        #add to Stacked Widget
        self.ui.centralStackWidget.addWidget(self.detection_screen)
        self.ui.centralStackWidget.addWidget(self.measurement_screen)
        self.ui.centralStackWidget.addWidget(self.test_detect_pair_screen)
        
        #event handler
    def exit_program(self):
        self.close()
    
    def change_detection_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.detection_screen)

    def change_measurement_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.measurement_screen)

    def change_detect_pair_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.test_detect_pair_screen)

        #binding
    def bind_exit_program(self):
        self.ui.actionExit.triggered.connect(self.exit_program)    
    
    