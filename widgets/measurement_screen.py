from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from widgets.image_widget import ImageWidget
import numpy as np
import os
import cv2
import imutils
from app_models.detector_config import DetectorConfig
from views.measurement_screen import Ui_MeasurementScreen
from views.detection_config_screen import Ui_DetectionConfigScreen
from FQCS import detector, helper, manager


class MeasurementScreen(QWidget):
    CAMERA_LOADED = False
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui = Ui_MeasurementScreen()
        self.ui.setupUi(self)
        self.manager = manager.FQCSManager()
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.binding()
        self.load_cfg()

    # binding
    def binding(self):
        self.ui.sldMaximumHeight.valueChanged.connect(self.min_height_change)
        self.ui.sldMaximumWidth.valueChanged.connect(self.min_width_change)
        self.ui.sldDectectPosition.valueChanged.connect(self.position_change)
        self.ui.sldDetectRange.valueChanged.connect(self.detect_range_change)
        self.ui.inpLeftActualLength.textChanged.connect(
            self.actual_length_change)
        self.ui.inpAllowDiff.textChanged.connect(self.allow_diff_change)
        self.ui.inpLengthUnit.textChanged.connect(self.length_unit_change)

    def min_width_change(self):
        value = self.ui.sldMaximumWidth.value()
        self.detector_cfg["min_width_per"] = value / 100
        self.ui.groupSliderWidth.setTitle("Maximum width (%): " + str(value))

    def min_height_change(self):
        value = self.ui.sldMaximumHeight.value()
        self.detector_cfg["min_height_per"] = value / 100
        self.ui.groupSliderHeight.setTitle("Maximum height (%): " + str(value))

    def position_change(self):
        value = self.ui.sldDectectPosition.value()
        self.detector_cfg["stop_condition"] = value / 100 * self.label_width
        self.ui.groupSliderPosition.setTitle("Detect position: " + str(value))

    def length_unit_change(self):
        value = str(self.ui.inpLengthUnit.text())
        self.ui.groupInputAllowDiff.setTitle(f"Allow Difference ({value})")
        self.detector_cfg["length_unit"] = value

    def detect_range_change(self):
        value = str(self.ui.sldDetectRange.value() / 100)
        self.detector_cfg["detect_range"] = (float(value),
                                             float(1 - float(value)))
        self.ui.groupSliderDetectRange.setTitle("Detect range: " + value)

    def actual_length_change(self, text):
        value = float(self.ui.inpLeftActualLength.text())
        total_px = int(self.ui.inpLeftDetectedLength.text())
        self.detector_cfg["length_per_10px"] = helper.calculate_length_per10px(
            total_px, value)

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
        orig = image.copy()
        orig = self.draw_rectangle_on_image(orig)
        orig = self.draw_position_line_on_image(orig)
        orig = self.draw_detect_range(orig)
        self.dim = (self.label_w, self.label_h)
        contour = self.process_image(image.copy())
        img_resized = cv2.resize(orig, self.dim)
        contour_resized = cv2.resize(contour, self.dim)
        self.image1.imshow(img_resized)
        self.image2.imshow(contour_resized)

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

    # draw functions
    def draw_rectangle_on_image(self, image):
        self.label_width = image.shape[1]
        self.label_height = image.shape[0]

        height_value = self.ui.sldMaximumHeight.value()
        width_value = self.ui.sldMaximumWidth.value()

        rect_width = int(self.label_width * width_value / 100)
        rect_height = int(self.label_height * height_value / 100)
        # draw Green rectangle image into image
        return cv2.rectangle(image, (0, 0), (rect_width, rect_height),
                             (0, 0, 255), 3)
        # if img is None:
        #     sys.exit("Could not read the image")

    def draw_position_line_on_image(self, image):
        value = self.ui.sldDectectPosition.value()
        self.label_width = image.shape[1]
        self.label_height = image.shape[0]

        position = int(self.label_width * (value + 50) / 100)

        return cv2.line(image, (position, 0), (position, self.label_height),
                        (255, 0, 0), 3)
        # if img is None:
        #     sys.exit("Could not read the image")

    def draw_detect_range(self, image):
        # convert 0 - 50 to scale of 0.0 to 0.5 (step 0.01)
        # return value
        self.label_width = image.shape[1]
        self.label_height = image.shape[0]

        value = str(self.ui.sldDetectRange.value() / 100)

        left_line_ratio = float(value) / 1
        right_line_ratio = 1 - left_line_ratio

        left_line_point = int(left_line_ratio * self.label_width)
        right_line_point = int(right_line_ratio * self.label_width)
        self.detector_cfg["detect_range"] = (float(value),
                                             float(1 - float(value)))

        image = cv2.line(image, (left_line_point, 0),
                         (left_line_point, self.label_height), (0, 255, 0), 3)
        image = cv2.line(image, (right_line_point, 0),
                         (right_line_point, self.label_height), (0, 255, 0), 3)
        return image

    def process_image(self, image):
        manager = DetectorConfig.instance().manager
        boxes, proc = manager.extract_boxes(self.detector_cfg, image)
        for idx, b in enumerate(boxes):
            c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
            helper.draw_boxes(image, box)
        return image

    def load_cfg(self):
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        if self.detector_cfg is None: return
        min_width = self.detector_cfg["min_width_per"] * 100
        min_height = self.detector_cfg["min_height_per"] * 100
        # length_per_10px = self.detector_cfg["lenght_per_10px"] #
        length_unit = self.detector_cfg["length_unit"]
        stop_condition = self.detector_cfg["stop_condition"]
        detect_range = self.detector_cfg["detect_range"][0] * 100
        max_size_diff = self.detector_cfg["max_size_diff"]

        self.ui.sldMaximumWidth.setValue(min_width)
        self.ui.sldMaximumHeight.setValue(min_height)
        self.ui.inpLengthUnit.setText(length_unit)
        self.ui.groupInputAllowDiff.setTitle(
            f"Allow Difference ({length_unit})")
        self.ui.sldDectectPosition.setValue(stop_condition)
        self.ui.sldDetectRange.setValue(detect_range)
        self.ui.inpAllowDiff.setValue(max_size_diff)
