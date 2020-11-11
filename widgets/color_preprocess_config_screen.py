from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, Qt

from views.color_preprocess_config_screen import Ui_color_preprocess_config_screen
from widgets.image_widget import ImageWidget
from app_models.detector_config import DetectorConfig
from FQCS import detector, helper
from app import helpers
import numpy as np
import os
import cv2


class ColorPreprocessConfigScreen(QWidget):
    BLUR_STEP = 0.01
    SATURATION_STEP = 0.5
    BRIGHTNESS_STEP = 0.1
    CONTRAST_STEP = 5
    CAMERA_LOADED = False
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui = Ui_color_preprocess_config_screen()
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.image1 = None
        self.image2 = None
        self.binding()
        self.load_cfg()

    # binding
    def binding(self):
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
        self.ui.chkColorCompare.stateChanged.connect(
            self.color_compare_state_change)

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

    def color_compare_state_change(self):
        if self.ui.chkColorCompare.isChecked():
            self.detector_cfg["is_color_enable"] = True
        else:
            self.detector_cfg["is_color_enable"] = False

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
        if (self.ui.cbbResizeHeight.currentIndex() != -1
                and self.ui.cbbResizeWidth.currentIndex() != -1):
            width_value = int(self.ui.cbbResizeWidth.currentText())
            height_value = int(self.ui.cbbResizeHeight.currentText())
            img_size = (width_value, height_value)
            self.detector_cfg["color_cfg"]["img_size"] = img_size
            self.view_image()

    def view_image(self):
        manager = DetectorConfig.instance().manager
        if (self.image1 is not None and self.image2 is not None):
            left = manager.get_sample_left()
            right = manager.get_sample_right()
            modified_left, modified_right = self.preprocess_color(left, right)
            img_size = (256, self.label_h - 50)
            modified_left = cv2.resize(modified_left,
                                       img_size,
                                       interpolation=cv2.INTER_AREA)
            modified_right = cv2.resize(modified_right,
                                        img_size,
                                        interpolation=cv2.INTER_AREA)
            self.image1.imshow(modified_left)
            self.image2.imshow(modified_right)

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.image2 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.imageLayout.replaceWidget(self.ui.screen2, self.image2)
            self.image1.ui.lblImage.setAlignment(Qt.AlignCenter)
            self.image2.ui.lblImage.setAlignment(Qt.AlignCenter)
            self.CAMERA_LOADED = True

    def showEvent(self, event):
        self.replace_camera_widget()

    def preprocess_color(self, sample_left, sample_right):
        manager = DetectorConfig.instance().manager
        pre_sample_left = manager.preprocess(self.detector_cfg, sample_left,
                                             True)
        pre_sample_right = manager.preprocess(self.detector_cfg, sample_right,
                                              False)
        return pre_sample_left, pre_sample_right

    def load_cfg(self):
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        if self.detector_cfg is None: return
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

        self.ui.sldSaturation.setValue(
            round(saturation / self.SATURATION_STEP, 1))
        self.ui.groupSldSaturation.setTitle("Saturation: " + str(saturation))

        self.ui.sldBrightLeft.setValue(
            round(brightness_left / self.BRIGHTNESS_STEP, 1))
        self.ui.groupSldBrightLeft.setTitle("Brightness left: " +
                                            str(brightness_left))

        self.ui.sldBrightRight.setValue(
            round(brightness_right / self.BRIGHTNESS_STEP, 1))
        self.ui.groupSldBrightRight.setTitle("Brightness right: " +
                                             str(brightness_right))

        self.ui.sldConstrastLeft.setValue(
            round(contrast_left / self.CONTRAST_STEP, 0))
        self.ui.groupSldConstrastLeft.setTitle("Contrast left: " +
                                               str(contrast_left))

        self.ui.sldConstrastRight.setValue(
            round(contrast_right / self.CONTRAST_STEP, 0))
        self.ui.groupSldConstrastRight.setTitle("Contrast right: " +
                                                str(contrast_right))
