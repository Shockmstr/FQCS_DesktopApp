from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.color_preprocess_config_screen import Ui_color_preprocess_config_screen


class ColorPreprocessConfigScreen(QWidget):
    BLUR_STEP = 0.01
    SATURATION_STEP = 0.5
    BRIGHTNESS_STEP = 0.1
    CONTRAST_STEP = 5

    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
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


    # handler
    def blur_value_change(self):
        value = round(self.ui.sldBlur.value() * self.BLUR_STEP, 2)
        self.ui.groupSldBlur.setTitle("Blur: " + str(value))

    def brightness_left_value_change(self):
        value = round(self.ui.sldBrightLeft.value() * self.BRIGHTNESS_STEP, 1)
        self.ui.groupSldBrightLeft.setTitle("Brightness left: " + str(value))

    def brightness_right_value_change(self):
        value = round(self.ui.sldBrightRight.value() * self.BRIGHTNESS_STEP, 1)
        self.ui.groupSldBrightRight.setTitle("Brightness right: " + str(value))

    def contrast_left_value_change(self):
        value = self.ui.sldConstrastLeft.value() * self.CONTRAST_STEP
        self.ui.groupSldConstrastLeft.setTitle("Contrast left: " + str(value))

    def contrast_right_value_change(self):
        value = self.ui.sldConstrastRight.value() * self.CONTRAST_STEP
        self.ui.groupSldConstrastRight.setTitle("Contrast right: " +
                                                str(value))

    def saturation_value_change(self):
        value = round(self.ui.sldSaturation.value() * self.SATURATION_STEP, 1)
        self.ui.groupSldSaturation.setTitle("Saturation: " + str(value))
