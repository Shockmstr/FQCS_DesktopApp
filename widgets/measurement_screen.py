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
    backscreen: Signal
    nextscreen: Signal
    captured = Signal()
    __actual_length_edited = False

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__current_cfg = None
        self.ui = Ui_MeasurementScreen()
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        self.image1 = ImageWidget()
        self.image2 = ImageWidget()
        self.imageLayout = self.ui.screen1.parentWidget().layout()
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
        self.imageLayout.replaceWidget(self.ui.screen2, self.image2)
        self.ui.screen1.deleteLater()
        self.ui.screen2.deleteLater()

    def showEvent(self, event):
        _, self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        self.__set_btn_capture_text()
        self.__load_config()

    # binding
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        self.ui.sldMaximumHeight.valueChanged.connect(
            self.sld_min_height_change)
        self.ui.sldMaximumWidth.valueChanged.connect(self.sld_min_width_change)
        self.ui.sldDectectPosition.valueChanged.connect(
            self.sld_position_change)
        self.ui.sldDetectRange.valueChanged.connect(
            self.sld_detect_range_change)
        self.ui.btnEditActualLength.clicked.connect(
            self.btn_edit_actual_length_clicked)
        self.ui.inpAllowDiff.textChanged.connect(self.inp_allow_diff_changed)
        self.ui.inpLengthUnit.textChanged.connect(self.inp_length_unit_change)
        self.ui.chkMainCamera.stateChanged.connect(
            self.chk_main_camera_state_changed)

    def btn_capture_clicked(self):
        self.captured.emit()
        self.__set_btn_capture_text()

    def __set_btn_capture_text(self):
        timer_active = DetectorConfig.instance().get_timer().isActive()
        self.ui.btnCapture.setText("CAPTURE" if not timer_active else "STOP")

    def chk_main_camera_state_changed(self):
        is_checked = self.ui.chkMainCamera.isChecked()
        DetectorConfig.instance().get_manager().set_main_config(
            self.__current_cfg["name"] if is_checked else None)

    def sld_min_width_change(self):
        value = self.ui.sldMaximumWidth.value()
        self.__current_cfg["min_width_per"] = value / 100
        self.ui.groupSliderWidth.setTitle("Maximum width (%): " + str(value))

    def sld_min_height_change(self):
        value = self.ui.sldMaximumHeight.value()
        self.__current_cfg["min_height_per"] = value / 100
        self.ui.groupSliderHeight.setTitle("Maximum height (%): " + str(value))

    def sld_position_change(self):
        value = self.ui.sldDectectPosition.value()
        self.__current_cfg["stop_condition"] = -value
        self.ui.groupSliderPosition.setTitle("Detect position: " + str(-value))

    def inp_length_unit_change(self):
        value = str(self.ui.inpLengthUnit.text())
        self.ui.groupInputAllowDiff.setTitle(f"Allow Difference ({value})")
        self.__current_cfg["length_unit"] = value

    def sld_detect_range_change(self):
        value = str(self.ui.sldDetectRange.value() / 100)
        self.__current_cfg["detect_range"] = (float(value),
                                              float(1 - float(value)))
        self.ui.groupSliderDetectRange.setTitle("Detect range: " + value)

    def btn_edit_actual_length_clicked(self, event):
        if self.__actual_length_edited:
            value = float(self.ui.inpLeftActualLength.text())
            total_px = float(self.ui.inpLeftDetectedLength.text())
            if (total_px is not None and total_px > 0):
                self.__current_cfg["length_per_10px"] = 0 if (
                    value is None
                    or value == 0) else helper.calculate_length_per10px(
                        total_px, value)
            self.ui.inpLeftActualLength.setEnabled(False)
            self.ui.btnEditActualLength.setText("Edit")
        else:
            self.ui.inpLeftActualLength.setEnabled(True)
            self.ui.btnEditActualLength.setText("Save")
        self.__actual_length_edited = not self.__actual_length_edited

    def inp_allow_diff_changed(self, text):
        value = float(self.ui.inpAllowDiff.text())
        self.__current_cfg["max_size_diff"] = value

    # view camera
    def view_cam(self, image):
        # read image in BGR format
        label_w = self.image1.width()
        label_h = self.image1.height()
        if image is None:
            self.image1.imshow(image)
            self.image2.imshow(image)
            return
        orig = image.copy()
        orig = self.__draw_rectangle_on_image(orig)
        orig = self.__draw_position_line_on_image(orig)
        orig = self.__draw_detect_range(orig)
        dim = (label_w, label_h)
        contour, sizes = self.__process_image(image.copy())
        img_resized = cv2.resize(orig, dim)
        contour_resized = cv2.resize(contour, dim)
        left_length, actual_length = 0, 0
        if len(sizes) > 0:
            length_per_10px = self.__current_cfg["length_per_10px"]
            left_length = sizes[0][0]
            actual_length = 0 if length_per_10px is None or length_per_10px == 0 else helper.calculate_length(
                left_length, length_per_10px)
        self.ui.inpLeftDetectedLength.setText(f"{left_length:.2f}")
        if not self.__actual_length_edited:
            self.ui.inpLeftActualLength.setValue(actual_length)

        self.image1.imshow(img_resized)
        self.image2.imshow(contour_resized)

    # draw functions
    def __draw_rectangle_on_image(self, image):
        image_width = image.shape[1]
        image_height = image.shape[0]

        height_value = self.ui.sldMaximumHeight.value()
        width_value = self.ui.sldMaximumWidth.value()

        rect_width = int(image_width * width_value / 100)
        rect_height = int(image_height * height_value / 100)
        # draw Green rectangle image into image
        return cv2.rectangle(image, (0, 0), (rect_width, rect_height),
                             (0, 0, 255), 3)

    def __draw_position_line_on_image(self, image):
        value = self.ui.sldDectectPosition.value()
        image_width = image.shape[1]
        image_height = image.shape[0]

        position = int(image_width / 2 + value)

        return cv2.line(image, (position, 0), (position, image_height),
                        (255, 0, 0), 3)

    def __draw_detect_range(self, image):
        # convert 0 - 50 to scale of 0.0 to 0.5 (step 0.01)
        # return value
        image_width = image.shape[1]
        image_height = image.shape[0]

        value = str(self.ui.sldDetectRange.value() / 100)

        left_line_ratio = float(value) / 1
        right_line_ratio = 1 - left_line_ratio

        left_line_point = int(left_line_ratio * image_width)
        right_line_point = int(right_line_ratio * image_width)
        self.__current_cfg["detect_range"] = (float(value),
                                              float(1 - float(value)))

        image = cv2.line(image, (left_line_point, 0),
                         (left_line_point, image_height), (0, 255, 0), 3)
        image = cv2.line(image, (right_line_point, 0),
                         (right_line_point, image_height), (0, 255, 0), 3)
        return image

    def __process_image(self, image):
        manager = DetectorConfig.instance().get_manager()
        boxes, proc = manager.extract_boxes(self.__current_cfg, image)
        sizes = []
        for idx, b in enumerate(boxes):
            c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
            sizes.append((dimA, dimB))
            length_per_10px = self.__current_cfg["length_per_10px"]
            unit = self.__current_cfg["length_unit"]
            if length_per_10px is not None and length_per_10px != 0:
                dimA, dimB = helper.calculate_length(
                    dimA, length_per_10px), helper.calculate_length(
                        dimB, length_per_10px)
            helper.draw_boxes_and_sizes(image, None, box, dimA, dimB, unit, tl,
                                        br)
        return image, sizes

    def __load_config(self):
        min_width = self.__current_cfg["min_width_per"] * 100
        min_height = self.__current_cfg["min_height_per"] * 100
        length_unit = self.__current_cfg["length_unit"]
        stop_condition = self.__current_cfg["stop_condition"]
        detect_range = self.__current_cfg["detect_range"][0] * 100
        max_size_diff = self.__current_cfg["max_size_diff"]
        frame_width = self.__current_cfg["frame_width"]

        self.ui.sldMaximumWidth.setValue(min_width)
        self.ui.sldMaximumHeight.setValue(min_height)
        self.ui.inpLengthUnit.setText(length_unit)
        self.ui.groupInputAllowDiff.setTitle(
            f"Allow Difference ({length_unit})")
        self.ui.sldDectectPosition.setMinimum(-int(frame_width / 2))
        self.ui.sldDectectPosition.setMaximum(int(frame_width / 2))
        self.ui.sldDectectPosition.setValue(-stop_condition)
        self.ui.sldDetectRange.setValue(detect_range)
        self.ui.inpAllowDiff.setValue(max_size_diff)
        self.ui.chkMainCamera.setChecked(self.__current_cfg["is_main"])
        self.ui.inpLeftDetectedLength.setText(str(0))
        self.ui.inpLeftActualLength.setValue(0)
        self.ui.inpLeftActualLength.setEnabled(False)
        self.ui.btnEditActualLength.setText("Edit")
        self.__actual_length_edited = False
