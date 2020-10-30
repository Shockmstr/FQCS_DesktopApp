from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets.image_widget import ImageWidget
import numpy as np
import cv2 as cv
from models.detector_config import DetectorConfig, DetectorConfigSingleton
from views.measurement_screen import Ui_MeasurementScreen
from views.detection_config_screen import Ui_DetectionConfigScreen

class MeasurementScreen(QWidget):
    CAMERA_LOADED = False

    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.detector_cfg = DetectorConfigSingleton.get_instance().config
        self.ui = Ui_MeasurementScreen()
        self.ui.setupUi(self)
        self.label_width = 0
        self.label_height = 0
        self.height_value =  0
        self.width_value = 0
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen:(), nextscreen: ()):
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnNext.clicked.connect(nextscreen)
        self.ui.sldMaximumHeight.valueChanged.connect(self.draw_rectangle_on_image)
        self.ui.sldMaximumWidth.valueChanged.connect(self.draw_rectangle_on_image)
        self.ui.sldDectectPosition.valueChanged.connect(self.draw_position_line_on_image)
        self.ui.sldDetectRange.valueChanged.connect(self.detect_range_change)
        self.ui.inpLeftActualLength.textChanged.connect(self.actual_length_change)
        self.ui.inpAllowDiff.textChanged.connect(self.allow_diff_change)
        self.ui.inpLengthUnit.textChanged.connect(self.length_unit_change)

    def draw_rectangle_on_image(self):
        if self.sender() == self.ui.sldMaximumWidth:
            self.width_value = self.ui.sldMaximumWidth.value()
            self.ui.groupSliderWidth.setTitle("Maximum width(%): " + str(self.width_value))
        if self.sender() == self.ui.sldMaximumHeight:
            self.height_value = self.ui.sldMaximumHeight.value()
            self.ui.groupSliderHeight.setTitle("Maximum height(%): " + str(self.height_value))
            
        self.label_width = self.img.shape[1]
        self.label_height = self.img.shape[0]

        rectange_width = int(self.label_width * self.width_value / 100)
        rectange_height = int(self.label_height * self.height_value / 100)

        self.detector_cfg["min_width_per"] = self.width_value / 100
        self.detector_cfg["min_height_per"] = self.height_value / 100
        # draw Green rectangle image into image
        return cv.rectangle(self.img,(0,0),(rectange_width,rectange_height),(0,255,0),3)
        # if img is None:
        #     sys.exit("Could not read the image")
        
        
    def draw_position_line_on_image(self):
        value = self.ui.sldDectectPosition.value()
        self.ui.groupSliderPosition.setTitle("Detect position: " + str(value))

        self.label_width = self.img.shape[1]
        self.label_height = self.img.shape[0]

        width = int(self.label_width * value / 100)

        self.detector_cfg["stop_condition"] = (value - 50) / 50
        
        return cv.line(self.img, (width,0), (width, self.label_height), (0, 255, 0), 3)
        # if img is None:
        #     sys.exit("Could not read the image")
        
        
        
        
    def calculate_length_per10px(total_px, total_length):
        return total_length / total_px * 10

    def length_unit_change(self):
        value = str(self.ui.inpLengthUnit.text())
        self.detector_cfg["length_unit"] = value
        
    def detect_range_change(self):
        # convert 0 - 50 to scale of 0.0 to 0.5 (step 0.01)
        # return value 
        value = str(self.ui.sldDetectRange.value() / 100)
        self.ui.groupSliderDetectRange.setTitle("Detect range: " + value)

        self.label_width = self.img.shape[1]
        self.label_height = self.img.shape[0]

        left_line_ratio = float(value) / 1
        right_line_ratio = 1 - left_line_ratio

        left_line_point = int(left_line_ratio * self.label_width)
        right_line_point = int(right_line_ratio * self.label_width)
        self.detector_cfg["detect_range"] = (float(value), float(1 - float(value)))

        image = cv.line(self.img, (left_line_point,0), (left_line_point, self.label_height), (0, 255, 0), 3)
        image = cv.line(self.img, (right_line_point,0), (right_line_point, self.label_height), (0, 255, 0), 3)
        return image
        

    def actual_length_change(self, text):
        value = float(self.ui.inpLeftActualLength.text())
        self.detector_cfg["length_per_10px"] = self.calculate_length_per10px(total_px, value)

    def allow_diff_change(self, text):
        value = float(self.ui.inpAllowDiff.text())
        try:
            if value < 0:
                raise 'Number should be greater than 0'
        except:
                raise 'Please enter number only'
        
        self.detector_cfg["max_size_diff"] = value

    # view camera
    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.img = self.draw_rectangle_on_image()
        self.img = self.draw_position_line_on_image()
        self.img = self.detect_range_change()
        self.dim = (self.label_w, self.label_h)
        self.img = cv.resize(self.img, self.dim)
        self.image1.imshow(self.img)

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.CAMERA_LOADED = True
