from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from models.detector_config import DetectorConfigSingleton, DetectorConfig
from app.helpers import *
from views.error_detect_screen import Ui_ErrorDetectScreen


class ErrorDetectScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_ErrorDetectScreen()
        self.detector_cfg = DetectorConfigSingleton.get_instance().config
        self.ui.setupUi(self)
        self.init_ui_values()
        self.binding(backscreen=backscreen, nextscreen=nextscreen)
    
    def init_ui_values(self):
        self.height_value = 0
        self.width_value = 0
        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)

        frame_resize_values = [
            "160", "240", "320", "400", "480", "660", "720", "800", "880",
            "960", "1040", "1120", "1200", "1280"
        ]
        self.ui.cbbHeight.clear()
        for value in frame_resize_values:
            self.ui.cbbHeight.addItem(value, userData=int(value))

        self.ui.cbbWidth.clear()
        for value in frame_resize_values:
            self.ui.cbbWidth.addItem(value, userData=int(value))

        # def load_default_config():
        #     self.detector_cfg["err_cfg"] = self.

    # binding
    def binding(self, backscreen: (), nextscreen: ()):
        self.ui.btnFinish.clicked.connect(nextscreen)
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnFinish.clicked.connect(nextscreen)
        self.ui.inpMaxInstances.textChanged.connect(self.max_instances_change)
        self.ui.inpMinimumScore.textChanged.connect(self.min_socre_change)
        self.ui.inpIouThreshold.textChanged.connect(self.iou_threshold_change)
        self.ui.cbbHeight.currentIndexChanged.connect(self.image_resize)
        self.ui.cbbWidth.currentIndexChanged.connect(self.image_resize)

    # hander
    def min_socre_change(self):
        value = self.ui.inpMinimumScore.value()
        self.detector_cfg["err_cfg"]["yolo_score_threshold"] = value
        print(value)

    def max_instances_change(self):
        value = self.ui.inpMaxInstances.value()
        self.detector_cfg["err_cfg"]["yolo_max_boxes"] = value 
        print(value)

    def iou_threshold_change(self):
        value = self.ui.inpIouThreshold.value()
        self.detector_cfg["err_cfg"]["yolo_iou_threshold"] = value
        print(value)

    def cbbHeight_changed(self):
        value = self.ui.cbbHeight.currentData()
        return value

    def cbbWidth_changed(self):
        value = self.ui.cbbWidth.currentData()
        return value

    def image_resize(self):
        if self.sender() == self.ui.cbbHeight:
            self.height_value = self.ui.cbbHeight.currentData()
        if self.sender() == self.ui.cbbWidth:
            self.width_value = self.ui.cbbWidth.currentData()
            
        print(self.height_value, self.width_value)



    

    