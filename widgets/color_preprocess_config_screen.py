from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.color_preprocess_config_screen import Ui_color_preprocess_config_screen
from models.detector_config import DetectorConfig, DetectorConfigSingleton
from FQCS import detector, helper

class ColorPreprocessConfigScreen(QWidget):
    BLUR_STEP = 0.01
    SATURATION_STEP = 0.5
    BRIGHTNESS_STEP = 0.1
    CONTRAST_STEP = 5

    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.detector_cfg = DetectorConfigSingleton.get_instance().config
        # self.detector_cfg["color_cfg"] = detector.default_color_config
        self.ui = Ui_color_preprocess_config_screen()
        self.ui.setupUi(self)
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen: (), nextscreen: ()):
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnNext.clicked.connect(nextscreen)

        self.ui.sldBlur.valueChanged.connect(self.blur_value_change)
        self.ui.sldBrightLeft.valueChanged.connect(
            self.brightness_left_value_change)
        self.ui.sldBrightRight.valueChanged.connect(
            self.brightness_right_value_change)
        self.ui.sldConstrastLeft.valueChanged.connect(
            self.contrast_left_value_change)
        self.ui.sldConstrastRight.valueChanged.connect(
            self.contrast_right_value_change)
        self.ui.sldSaturation.valueChanged.connect(
            self.saturation_value_change)

        resize_number = ["32", "64", "128", "256", "512", "1024"]
        self.ui.cbbResizeWidth.clear()   
        self.ui.cbbResizeWidth.addItems(resize_number)
        self.ui.cbbResizeWidth.setCurrentIndex(-1)
        self.ui.cbbResizeWidth.setPlaceholderText("Width")

        self.ui.cbbResizeHeight.clear()
        self.ui.cbbResizeHeight.addItems(resize_number)
        self.ui.cbbResizeHeight.setCurrentIndex(-1)
        self.ui.cbbResizeHeight.setPlaceholderText("Height")

        self.ui.cbbResizeWidth.activated.connect(self.cbbResize_chosen)
        self.ui.cbbResizeHeight.activated.connect(self.cbbResize_chosen)
    # handler
    def blur_value_change(self):
        value = round(self.ui.sldBlur.value() * self.BLUR_STEP, 2)
        self.detector_cfg["color_cfg"]["blur_val"] = value
        self.ui.groupSldBlur.setTitle("Blur: " + str(value))

    def brightness_left_value_change(self):
        value = round(self.ui.sldBrightLeft.value() * self.BRIGHTNESS_STEP, 1)
        self.detector_cfg["color_cfg"]["alpha_l"] = value
        self.ui.groupSldBrightLeft.setTitle("Brightness left: " + str(value))

    def brightness_right_value_change(self):
        value = round(self.ui.sldBrightRight.value() * self.BRIGHTNESS_STEP, 1)
        self.detector_cfg["color_cfg"]["alpha_r"] = value
        self.ui.groupSldBrightRight.setTitle("Brightness right: " + str(value))

    def contrast_left_value_change(self):
        value = self.ui.sldConstrastLeft.value() * self.CONTRAST_STEP
        self.detector_cfg["color_cfg"]["beta_l"] = value
        self.ui.groupSldConstrastLeft.setTitle("Contrast left: " + str(value))

    def contrast_right_value_change(self):
        value = self.ui.sldConstrastRight.value() * self.CONTRAST_STEP
        self.detector_cfg["color_cfg"]["beta_r"] = value
        self.ui.groupSldConstrastRight.setTitle("Contrast right: " +
                                                str(value))

    def saturation_value_change(self):
        value = round(self.ui.sldSaturation.value() * self.SATURATION_STEP, 1)
        self.detector_cfg["color_cfg"]["sat_adj"] = value
        self.ui.groupSldSaturation.setTitle("Saturation: " + str(value))

    def cbbResize_chosen(self):
        if (self.ui.cbbResizeHeight.currentIndex() != -1 and self.ui.cbbResizeWidth.currentIndex() != -1):
            width_value = int(self.ui.cbbResizeWidth.currentText())
            height_value = int(self.ui.cbbResizeHeight.currentText())
            img_size = (width_value, height_value)
            self.detector_cfg["color_cfg"]["img_size"] = img_size
            print(self.detector_cfg["color_cfg"])

    # def cbbResizeHeight_chosen(self):
    #     width_value = int(self.ui.cbbResizeWidth.currentText())
    #     height_value = int(self.ui.cbbResizeHeight.currentText())
    #     img_size = (width_value, height_value)
    #     self.detector_cfg["color_cfg"]["img_size"] = img_size