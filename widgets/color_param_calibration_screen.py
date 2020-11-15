from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer, Signal, Qt
from widgets.image_widget import ImageWidget
from app_models.detector_config import DetectorConfig
import cv2
from FQCS import detector, helper, manager
from app import helpers
import numpy as np
import os
import imutils
import trio
from views.color_param_calibration_screen import Ui_ColorParamCalibScreen


class ColorParamCalibrationScreen(QWidget):
    CAMERA_LOADED = False
    IMAGE_LOADED = False
    __detected_pair = None
    backscreen: Signal
    nextscreen: Signal
    __max_blue = 0
    __max_green = 0
    __max_red = 0

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui = Ui_ColorParamCalibScreen()
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        self.manager_changed()

    # binding
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        DetectorConfig.instance().manager_changed.connect(self.manager_changed)
        self.ui.cbbCamera.setPlaceholderText("Choose Cam")
        self.ui.cbbCamera.setCurrentIndex(-1)
        self.ui.cbbCamera.currentIndexChanged.connect(self.cbbCamera_chose)
        self.ui.inpSuppThreshold.textChanged.connect(
            self.inp_sup_thresh_change)
        self.ui.sldAllowDiff.valueChanged.connect(self.sld_allow_diff_change)
        self.ui.sldAmpRate.valueChanged.connect(self.sld_amp_rate_change)
        self.ui.ampThreshBlue.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshGreen.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshRed.textChanged.connect(self.amp_threshold_change)

    def amp_threshold_change(self):
        amp_thresh_green_value = float(self.ui.ampThreshGreen.text())
        amp_thresh_red_value = float(self.ui.ampThreshRed.text())
        amp_thresh_blue_value = float(self.ui.ampThreshBlue.text())
        self.__current_cfg["color_cfg"]["amplify_thresh"] = (
            amp_thresh_red_value, amp_thresh_green_value,
            amp_thresh_blue_value)

    def sld_amp_rate_change(self):
        value = self.ui.sldAmpRate.value()
        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " + str(value))
        self.__current_cfg["color_cfg"]["amplify_rate"] = value

    def inp_sup_thresh_change(self):
        value = self.ui.inpSuppThreshold.value()
        self.__current_cfg["color_cfg"]["supp_thresh"] = value

    def sld_allow_diff_change(self):
        value = self.ui.sldAllowDiff.value() / 100
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference (%): " +
                                         str(value))
        self.__current_cfg["color_cfg"]["max_diff"] = value

    def cbbCamera_chose(self):
        self.image1 = ImageWidget()
        self.label_w = self.ui.screen1.width()
        self.label_h = self.ui.screen1.height()
        self.imageLayout = self.ui.screen1.parentWidget().layout()
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
        index = self.ui.cbbCamera.currentData()

    def manager_changed(self):
        self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        if self.__current_cfg is None: return
        amplify_rate = self.__current_cfg["color_cfg"]["amplify_rate"]
        supp_thresh = self.__current_cfg["color_cfg"]["supp_thresh"]
        max_diff = self.__current_cfg["color_cfg"]["max_diff"]

        self.ui.sldAllowDiff.setValue(max_diff * 100)
        self.ui.sldAmpRate.setValue(amplify_rate)
        self.ui.inpSuppThreshold.setValue(supp_thresh)
        self.ui.ampThreshBlue.setValue(0)  # self-created value
        self.ui.ampThreshGreen.setValue(0)  # self-created value
        self.ui.ampThreshRed.setValue(0)  # self-created value

        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " +
                                       str(amplify_rate))
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference (%): " +
                                         str(max_diff))

    def __view_image_sample(self):
        manager = DetectorConfig.instance().manager
        left = manager.get_sample_left()
        right = manager.get_sample_right()
        m_left, m_right = self.__preprocess_color(left, right)
        img_size = (156, self.label_h - 30)
        m_left = cv2.resize(m_left, img_size, interpolation=cv2.INTER_AREA)
        m_right = cv2.resize(m_right, img_size, interpolation=cv2.INTER_AREA)
        self.image_sample_left.imshow(m_left)
        self.image_sample_right.imshow(m_right)

    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        img_size = (156, self.label_h - 30)
        contour, detected, detected_pair = self.__process_pair(self.img.copy())
        contour_resized = cv2.resize(contour, self.dim)
        self.image1.imshow(contour_resized)
        if detected_pair is not None:
            left, right = self.__preprocess_color(detected_pair[0],
                                                  detected_pair[1])
            left = cv2.flip(left, 1)
            trio.run(self.__find_amp_threshold, left, right)
            left = cv2.resize(left, img_size)
            right = cv2.resize(right, img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)
            self.__detected_pair = detected_pair

    async def __find_amp_threshold(self, img_left, img_right):
        manager = DetectorConfig.instance().manager
        sample_left_path = manager.get_sample_left()
        sample_right_path = manager.get_sample_right()
        sample_left, sample_right = self.__preprocess_color(
            sample_left_path, sample_right_path)

        left_task, right_task = await manager.compare_colors(
            self.__current_cfg, img_left, img_right, sample_left, sample_right,
            None)
        _, _, left_hist, _ = left_task
        _, _, right_hist, _ = right_task
        blue = max(left_hist[0], right_hist[0])
        green = max(left_hist[1], right_hist[1])
        red = max(left_hist[2], right_hist[2])
        if (blue > self.__max_blue): self.__max_blue = blue
        if (green > self.__max_green): self.__max_green = green
        if (red > self.__max_red): self.__max_red = red
        amp_thresh = (float(self.__max_red), float(self.__max_green),
                      float(self.__max_blue))
        self.ui.ampThreshRed.setValue(amp_thresh[0])
        self.ui.ampThreshGreen.setValue(amp_thresh[1])
        self.ui.ampThreshBlue.setValue(amp_thresh[2])
        self.__current_cfg["color_cfg"]["amplify_thresh"] = amp_thresh

    def showEvent(self, event):
        self.image_detect_left = ImageWidget()
        self.image_detect_right = ImageWidget()
        self.image_sample_left = ImageWidget()
        self.image_sample_right = ImageWidget()
        self.label_w = self.ui.screen2.width()
        self.label_h = self.ui.screen2.height()

        self.screen2_layout = self.ui.screen2.layout()
        self.screen2_layout.replaceWidget(self.ui.screen2Left,
                                          self.image_detect_left)
        self.screen2_layout.replaceWidget(self.ui.screen2Right,
                                          self.image_detect_right)

        self.screen3_layout = self.ui.screen3.layout()
        self.screen3_layout.replaceWidget(self.ui.screen3Left,
                                          self.image_sample_left)
        self.screen3_layout.replaceWidget(self.ui.screen3Right,
                                          self.image_sample_right)

        self.image_detect_left.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.image_detect_right.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.image_sample_left.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.image_sample_right.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.__view_image_sample()

    #image process function
    def __preprocess_color(self, sample_left, sample_right):
        manager = DetectorConfig.instance().manager
        pre_sample_left = manager.preprocess(self.__current_cfg, sample_left,
                                             True)
        pre_sample_right = manager.preprocess(self.__current_cfg, sample_right,
                                              False)
        return pre_sample_left, pre_sample_right

    def __process_pair(self, image):
        manager = DetectorConfig.instance().manager
        boxes, proc = manager.extract_boxes(self.__current_cfg, image)
        final_grouped, sizes, check_group_idx, pair, split_left, split_right, image_detect = manager.detect_groups_and_checked_pair(
            self.__current_cfg, boxes, image)
        unit = self.__current_cfg["length_unit"]
        for idx, group in enumerate(final_grouped):
            for b_idx, b in enumerate(group):
                c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
                cur_size = sizes[idx][b_idx]
                lH, lW = cur_size
                helper.draw_boxes_and_sizes(image, idx, box, lH, lW, unit, tl,
                                            br)
        if (pair is not None):
            manager.check_group(check_group_idx, final_grouped)
            left, right = pair
            left, right = left[0], right[0]
            left = cv2.flip(left, 1)
            max_width = max((left.shape[0], right.shape[0]))
            temp_left = imutils.resize(left, height=max_width)
            temp_right = imutils.resize(right, height=max_width)
            detected = np.concatenate((temp_left, temp_right), axis=1)
            return image, detected, [left, right]
        return image, None, None