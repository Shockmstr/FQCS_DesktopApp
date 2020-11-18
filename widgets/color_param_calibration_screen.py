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
import datetime
from app_constants import ISO_DATE_FORMAT


class ColorParamCalibrationScreen(QWidget):
    __detected_pair = None
    backscreen: Signal
    nextscreen: Signal
    captured = Signal()
    __max_blue = 0
    __max_green = 0
    __max_red = 0
    __amp_thresh_edited = False

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__current_cfg = None
        self.ui = Ui_ColorParamCalibScreen()
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        self.image1 = ImageWidget()
        self.imageLayout = self.ui.screen1.parentWidget().layout()
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
        self.ui.screen1.deleteLater()

        self.image_detect_left = ImageWidget()
        self.image_detect_right = ImageWidget()
        self.image_sample_left = ImageWidget()
        self.image_sample_right = ImageWidget()
        self.screen2_layout = self.ui.screen2.layout()
        self.screen2_layout.replaceWidget(self.ui.screen2Left,
                                          self.image_detect_left)
        self.screen2_layout.replaceWidget(self.ui.screen2Right,
                                          self.image_detect_right)
        self.ui.screen2Left.deleteLater()
        self.ui.screen2Right.deleteLater()

        self.screen3_layout = self.ui.screen3.layout()
        self.screen3_layout.replaceWidget(self.ui.screen3Left,
                                          self.image_sample_left)
        self.screen3_layout.replaceWidget(self.ui.screen3Right,
                                          self.image_sample_right)
        self.ui.screen3Left.deleteLater()
        self.ui.screen3Right.deleteLater()

        self.image_detect_left.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.image_detect_right.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.image_sample_left.ui.lblImage.setAlignment(Qt.AlignCenter)
        self.image_sample_right.ui.lblImage.setAlignment(Qt.AlignCenter)
        return

    def showEvent(self, event):
        _, self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui.inpResult.setHtml("<b>RESULT</b>")
        self.__view_image_sample()
        self.__set_btn_capture_text()
        self.__load_config()

    # binding
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        self.ui.inpSuppThreshold.textChanged.connect(
            self.inp_sup_thresh_change)
        self.ui.sldAllowDiff.valueChanged.connect(self.sld_allow_diff_change)
        self.ui.sldAmpRate.valueChanged.connect(self.sld_amp_rate_change)
        self.ui.ampThreshBlue.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshGreen.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshRed.textChanged.connect(self.amp_threshold_change)
        self.ui.chkColorCompare.stateChanged.connect(
            self.chk_color_enabled_state_changed)
        self.ui.btnEditAmpThresh.clicked.connect(
            self.btn_edit_amp_thresh_clicked)

    def btn_capture_clicked(self):
        self.captured.emit()
        self.__set_btn_capture_text()

    def __set_btn_capture_text(self):
        timer_active = DetectorConfig.instance().get_timer().isActive()
        self.ui.btnCapture.setText("CAPTURE" if not timer_active else "STOP")

    def amp_threshold_change(self):
        amp_thresh_green_value = float(self.ui.ampThreshGreen.text())
        amp_thresh_red_value = float(self.ui.ampThreshRed.text())
        amp_thresh_blue_value = float(self.ui.ampThreshBlue.text())
        self.__current_cfg["color_cfg"]["amplify_thresh"] = (
            amp_thresh_blue_value, amp_thresh_green_value,
            amp_thresh_red_value)

    def sld_amp_rate_change(self):
        value = self.ui.sldAmpRate.value()
        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " + str(value))
        self.__current_cfg["color_cfg"]["amplify_rate"] = value

    def inp_sup_thresh_change(self):
        value = self.ui.inpSuppThreshold.value()
        self.__current_cfg["color_cfg"]["supp_thresh"] = value

    def sld_allow_diff_change(self):
        value = self.ui.sldAllowDiff.value()
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference (%): " +
                                         str(value))
        self.__current_cfg["color_cfg"]["max_diff"] = value / 100

    def chk_color_enabled_state_changed(self):
        checked = self.ui.chkColorCompare.isChecked()
        self.__current_cfg["is_color_enable"] = checked

    def __load_config(self):
        color_cfg = self.__current_cfg["color_cfg"]
        amplify_rate = color_cfg["amplify_rate"]
        supp_thresh = color_cfg["supp_thresh"]
        max_diff = color_cfg["max_diff"]
        is_color_enable = self.__current_cfg["is_color_enable"]
        amp_thresh = color_cfg["amplify_thresh"]

        self.ui.sldAllowDiff.setValue(max_diff * 100)
        self.ui.sldAmpRate.setValue(amplify_rate)
        self.ui.inpSuppThreshold.setValue(supp_thresh)
        self.ui.ampThreshBlue.setValue(amp_thresh[0])
        self.ui.ampThreshGreen.setValue(amp_thresh[1])
        self.ui.ampThreshRed.setValue(amp_thresh[2])

        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " +
                                       str(amplify_rate))
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference (%): " +
                                         str(max_diff * 100))
        self.ui.chkColorCompare.setChecked(is_color_enable)

        self.ui.btnEditAmpThresh.setText("Edit")
        self.ui.ampThreshRed.setEnabled(False)
        self.ui.ampThreshGreen.setEnabled(False)
        self.ui.ampThreshBlue.setEnabled(False)

    def __view_image_sample(self):
        manager = DetectorConfig.instance().get_manager()
        left = manager.get_sample_left()
        right = manager.get_sample_right()
        m_left, m_right = self.__preprocess_color(left, right)
        label_h = self.ui.screen2.height()
        img_size = (156, label_h - 30)
        m_left = cv2.resize(m_left, img_size, interpolation=cv2.INTER_AREA)
        m_right = cv2.resize(m_right, img_size, interpolation=cv2.INTER_AREA)
        self.image_sample_left.imshow(m_left)
        self.image_sample_right.imshow(m_right)

    def view_cam(self, image):
        # read image in BGR format
        label_w = self.image1.width()
        label_h = self.image1.height()
        dim = (label_w, label_h)
        if image is None:
            self.image1.imshow(image)
            self.image_detect_left.imshow(image)
            self.image_detect_right.imshow(image)
            return
        img_size = (156, label_h - 30)
        contour, detected, detected_pair = self.__process_pair(image.copy())
        contour_resized = cv2.resize(contour, dim)
        self.image1.imshow(contour_resized)
        if detected_pair is not None:
            left, right = self.__preprocess_color(detected_pair[0],
                                                  detected_pair[1])
            trio.run(self.__find_amp_threshold, left, right)
            left = cv2.resize(left, img_size)
            right = cv2.resize(right, img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)
            self.__detected_pair = detected_pair

    async def __find_amp_threshold(self, img_left, img_right):
        manager = DetectorConfig.instance().get_manager()
        sample_left = manager.get_sample_left()
        sample_right = manager.get_sample_right()
        sample_left, sample_right = self.__preprocess_color(
            sample_left, sample_right)

        left_task, right_task = await manager.compare_colors(
            self.__current_cfg, img_left, img_right, sample_left, sample_right,
            not self.__amp_thresh_edited, None)
        _, avg_diff_l, left_hist, is_diff_l = left_task
        _, avg_diff_r, right_hist, is_diff_r = right_task
        blue = max(left_hist[0], right_hist[0])
        green = max(left_hist[1], right_hist[1])
        red = max(left_hist[2], right_hist[2])
        max_blue, max_green, max_red = self.__max_blue, self.__max_green, self.__max_red
        if (blue > max_blue): max_blue = blue
        if (green > max_green): max_green = green
        if (red > max_red): max_red = red
        amp_thresh = (float(max_blue), float(max_green), float(max_red))
        if self.__amp_thresh_edited:
            self.__max_blue = max_blue
            self.__max_red = max_red
            self.__max_green = max_green
            self.ui.ampThreshBlue.setValue(amp_thresh[0])
            self.ui.ampThreshGreen.setValue(amp_thresh[1])
            self.ui.ampThreshRed.setValue(amp_thresh[2])
            self.__current_cfg["color_cfg"]["amplify_thresh"] = amp_thresh

        # result display
        cur = datetime.datetime.now()
        cur_date_str = cur.strftime(ISO_DATE_FORMAT)
        result_text = f"<b>RESULT</b><br/>" + f"<b>Time</b>: {cur_date_str}<br/>"
        avg_diff_l *= 100
        avg_diff_r *= 100
        r, g, b = amp_thresh[0], amp_thresh[1], amp_thresh[2]
        result_text += f"<b>Current different value</b>: {r:.2f}, {g:.2f}, {b:.2f}<br/>"
        result_text += f"<b>Left different</b>: {avg_diff_l:.2f}%<br/>"
        result_text += f"<b>Right different</b>: {avg_diff_r:.2f}%<br/>"
        if not self.__amp_thresh_edited:
            left_result_text = "PASSED" if not is_diff_l else "FAILED"
            right_result_text = "PASSED" if not is_diff_r else "FAILED"
            result_text += f"<b>Result</b>: Left {left_result_text} - Right {right_result_text}"
        self.ui.inpResult.setHtml(result_text)

    def btn_edit_amp_thresh_clicked(self, event):
        if self.__amp_thresh_edited:
            self.ui.ampThreshRed.setEnabled(False)
            self.ui.ampThreshGreen.setEnabled(False)
            self.ui.ampThreshBlue.setEnabled(False)
            self.ui.btnEditAmpThresh.setText("Edit")
            self.__amp_thresh_edited = False
        else:
            self.ui.ampThreshRed.setEnabled(True)
            self.ui.ampThreshGreen.setEnabled(True)
            self.ui.ampThreshBlue.setEnabled(True)
            self.ui.btnEditAmpThresh.setText("Save")
            self.__amp_thresh_edited = True

    #image process function
    def __preprocess_color(self, sample_left, sample_right):
        manager = DetectorConfig.instance().get_manager()
        pre_sample_left = manager.preprocess(self.__current_cfg, sample_left,
                                             True)
        pre_sample_right = manager.preprocess(self.__current_cfg, sample_right,
                                              False)
        return pre_sample_left, pre_sample_right

    def __process_pair(self, image):
        manager = DetectorConfig.instance().get_manager()
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
            label_w = self.image1.width()
            label_h = self.image1.height()
            images = [left, right]
            self.__detected_pair = images
            final_img = helpers.concat_images(images, label_w, label_h)
            return image, final_img, images
        return image, None, None