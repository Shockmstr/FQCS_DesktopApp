from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ..app.helpers import * 

from views.color_param_calibration_screen import Ui_ColorParamCalibScreen


class ColorParamCalibrationScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_ColorParamCalibScreen()
        self.ui.setupUi(self)
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen: (), nextscreen: ()):
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnNext.clicked.connect(nextscreen)
        self.ui.cbbDisplayType.currentIndexChanged.connect(self.cbbDisplayType_chose)
        cam_array = get_all_camera_index(self)
        self.ui.cbbDisplayType.clear()
        for camera in cam_array:
            self.ui.cbbDisplayType.addItem("Camera " + str(camera), userData=camera)
        

    def cbbDisplayType_chose(self):
        self.replace_camera_widget()
        index = self.ui.cbbDisplayType.currentData()
        self.control_timer(index)

    def replace_camera_widget(self): #showEvent chay khi nao? Need tim hieu here/ co the thay the bang j nua dc ko?
        

        self.image1 = ImageWidget()
        self.label_w = self.ui.screen1.width()
        self.label_h = self.ui.screen1.height()
        self.imageLayout = self.ui.screen1.parentWidget().layout()     
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)   
