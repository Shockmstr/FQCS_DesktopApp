from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.color_preprocess_config_screen import Ui_color_preprocess_config_screen
from widgets.image_widget import ImageWidget
from models.detector_config import DetectorConfig, DetectorConfigSingleton
from FQCS import detector, helper
import numpy as np
import cv2

class ColorPreprocessConfigScreen(QWidget):
    BLUR_STEP = 0.01
    SATURATION_STEP = 0.5
    BRIGHTNESS_STEP = 0.1
    CONTRAST_STEP = 5
    CAMERA_LOADED = False

    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.detector_cfg = DetectorConfigSingleton.get_instance().config
        self.ui = Ui_color_preprocess_config_screen()
        self.ui.setupUi(self)
        self.binding(backscreen=backscreen, nextscreen=nextscreen)
        self.load_cfg()

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
        self.view_image()

    def brightness_left_value_change(self):
        value = round(self.ui.sldBrightLeft.value() * self.BRIGHTNESS_STEP, 1)
        self.detector_cfg["color_cfg"]["alpha_l"] = value
        self.ui.groupSldBrightLeft.setTitle("Brightness left: " + str(value))
        self.view_image()

    def brightness_right_value_change(self):
        value = round(self.ui.sldBrightRight.value() * self.BRIGHTNESS_STEP, 1)
        self.detector_cfg["color_cfg"]["alpha_r"] = value
        self.ui.groupSldBrightRight.setTitle("Brightness right: " + str(value))
        self.view_image()

    def contrast_left_value_change(self):
        value = self.ui.sldConstrastLeft.value() * self.CONTRAST_STEP
        self.detector_cfg["color_cfg"]["beta_l"] = value
        self.ui.groupSldConstrastLeft.setTitle("Contrast left: " + str(value))
        self.view_image()

    def contrast_right_value_change(self):
        value = self.ui.sldConstrastRight.value() * self.CONTRAST_STEP
        self.detector_cfg["color_cfg"]["beta_r"] = value
        self.ui.groupSldConstrastRight.setTitle("Contrast right: " +
                                                str(value))
        self.view_image()

    def saturation_value_change(self):
        value = round(self.ui.sldSaturation.value() * self.SATURATION_STEP, 1)
        self.detector_cfg["color_cfg"]["sat_adj"] = int(value)
        self.ui.groupSldSaturation.setTitle("Saturation: " + str(value))
        self.view_image()

    def cbbResize_chosen(self):
        if (self.ui.cbbResizeHeight.currentIndex() != -1 and self.ui.cbbResizeWidth.currentIndex() != -1):
            width_value = int(self.ui.cbbResizeWidth.currentText())
            height_value = int(self.ui.cbbResizeHeight.currentText())
            img_size = (width_value, height_value)
            self.detector_cfg["color_cfg"]["img_size"] = img_size
            self.view_image()

    def view_initial_image(self):
        width = self.ui.screen1.width()
        height = self.ui.screen1.height()
        left = cv2.imread("sample_left.jpg")
        right = cv2.imread("sample_right.jpg")
        img_size = (256,512)
        left = cv2.resize(left, img_size, interpolation=cv2.INTER_AREA)
        right = cv2.resize(right, img_size, interpolation=cv2.INTER_AREA)
        self.image1.imshow(left)
        self.image2.imshow(right)

    def view_image(self):
        width = self.ui.screen1.width()
        height = self.ui.screen1.height()
        left = cv2.imread("sample_left.jpg")
        right = cv2.imread("sample_right.jpg")
        m_left, m_right = self.preprocess_color(left, right)       
        img_size = (256,512)
        m_left = cv2.resize(m_left, img_size, interpolation=cv2.INTER_AREA)
        m_right = cv2.resize(m_right, img_size, interpolation=cv2.INTER_AREA)
        self.image1.imshow(m_left)
        self.image2.imshow(m_right)
        
        
    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.image2 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.imageLayout.replaceWidget(self.ui.screen2, self.image2)
            self.CAMERA_LOADED = True
        
    def showEvent(self, event):
        self.replace_camera_widget()
        self.view_initial_image()

    def preprocess_color(self, sample_left, sample_right):
        c_cfg = self.detector_cfg['color_cfg']
        print(c_cfg)
        pre_sample_left = detector.preprocess_for_color_diff(
            sample_left, c_cfg['img_size'], c_cfg['blur_val'],
            c_cfg['alpha_l'], c_cfg['beta_l'], c_cfg['sat_adj'])
        pre_sample_right = detector.preprocess_for_color_diff(
            sample_right, c_cfg['img_size'], c_cfg['blur_val'],
            c_cfg['alpha_r'], c_cfg['beta_r'], c_cfg['sat_adj'])
        return pre_sample_left, pre_sample_right    

    def load_cfg(self):
        #load from default
        color_cfg = self.detector_cfg["color_cfg"]
        img_size = color_cfg["img_size"]
        blur = color_cfg["blur_val"]
        brightness_left = color_cfg["alpha_l"]
        brightness_right = color_cfg["alpha_r"]
        contrast_left = color_cfg["beta_l"]
        contrast_right = color_cfg["beta_r"]
        saturation = color_cfg["sat_adj"]
        # set value
        self.ui.cbbResizeWidth.setCurrentText(str(img_size[0]))
        self.ui.cbbResizeHeight.setCurrentText(str(img_size[1]))

        self.ui.sldBlur.setValue(round(blur / self.BLUR_STEP, 2))
        self.ui.groupSldBlur.setTitle("Blur: " + str(blur))

        self.ui.sldSaturation.setValue(round(saturation / self.SATURATION_STEP, 1))
        self.ui.groupSldSaturation.setTitle("Saturation: " + str(saturation))

        self.ui.sldBrightLeft.setValue(round(brightness_left / self.BRIGHTNESS_STEP, 1))
        self.ui.groupSldBrightLeft.setTitle("Brightness left: " + str(brightness_left))

        self.ui.sldBrightRight.setValue(round(brightness_right / self.BRIGHTNESS_STEP, 1))
        self.ui.groupSldBrightRight.setTitle("Brightness right: " + str(brightness_right))

        self.ui.sldConstrastLeft.setValue(round(contrast_left / self.CONTRAST_STEP, 0))
        self.ui.groupSldConstrastLeft.setTitle("Contrast left: " + str(contrast_left))

        self.ui.sldConstrastRight.setValue(round(contrast_right / self.CONTRAST_STEP, 0))
        self.ui.groupSldConstrastRight.setTitle("Contrast right: " + str(contrast_right))
