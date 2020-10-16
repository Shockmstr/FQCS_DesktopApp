from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.measurement_screen import Ui_MeasurementScreen

class MeasurementScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MeasurementScreen()
        self.ui.setupUi(self)

    # event handler
    

    # data binding

