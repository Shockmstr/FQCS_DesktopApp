from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, Qt, QTimer
from views.asym_config_screen import Ui_AsymConfigScreen
from app_models.detector_config import DetectorConfig
from widgets.image_widget import ImageWidget
from FQCS import detector, helper
from app import helpers
import imutils
import cv2
import os
import numpy as np
import trio
import datetime
from app_constants import ISO_DATE_FORMAT
import json


class AsymConfigScreen(QWidget):
    MIN_SIMILARITY_STEP = 0.01
    backscreen: Signal
    nextscreen: Signal
    captured = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__current_cfg = None
        self.ui = Ui_AsymConfigScreen()
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

    # binding
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        self.ui.sldAmpRate.valueChanged.connect(
            self.sld_amplification_rate_changed)
        self.ui.sldMinSimilarity.valueChanged.connect(
            self.sld_min_similarity_changed)
        self.ui.inpReCalcFactorRight.textChanged.connect(
            self.inp_re_calc_right_changed)
        self.ui.inpReCalcFactorLeft.textChanged.connect(
            self.inp_re_calc_left_changed)
        self.ui.inpAmpThresh.textChanged.connect(
            self.inp_asym_amp_thresh_changed)
        self.ui.inpC1.textChanged.connect(self.inp_C1_changed)
        self.ui.inpC2.textChanged.connect(self.inp_C2_changed)
        self.ui.inpPSNR.textChanged.connect(self.inp_PSNR_changed)
        self.ui.cbbSegments.currentIndexChanged.connect(
            self.cbb_segments_current_index_changed)

    # handlers
    def btn_capture_clicked(self):
        self.captured.emit()
        self.__set_btn_capture_text()

    def __set_btn_capture_text(self):
        timer_active = DetectorConfig.instance().get_timer().isActive()
        self.ui.btnCapture.setText("CAPTURE" if not timer_active else "STOP")

    def sld_amplification_rate_changed(self):
        value = self.ui.sldAmpRate.value()
        self.__current_cfg["sim_cfg"]["asym_amp_rate"] = value
        self.ui.grpBoxAmpRate.setTitle("Amplification rate: " + str(value))

    def sld_min_similarity_changed(self):
        value = round(
            self.ui.sldMinSimilarity.value() * self.MIN_SIMILARITY_STEP, 2)
        self.__current_cfg["sim_cfg"]["min_similarity"] = value
        self.ui.grpBoxMinSimilarity.setTitle("Minimum similarity (%): " +
                                             str(value))

    def showEvent(self, event):
        _, self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui.inpResult.setHtml("<b>RESULT</b>")
        self.__set_btn_capture_text()
        self.__view_image_sample()
        self.__load_config()

    def cbb_segments_current_index_changed(self):
        selected = "[" + self.ui.cbbSegments.currentText() + "]"
        segments = json.loads(selected)
        self.__current_cfg["sim_cfg"]["segments_list"] = segments

    def __load_config(self):
        sim_cfg = self.__current_cfg["sim_cfg"]
        c1 = sim_cfg["C1"]
        c2 = sim_cfg["C2"]
        psnr = sim_cfg["psnr_trigger"]
        amp_thresh = sim_cfg["asym_amp_thresh"]
        amp_rate = sim_cfg["asym_amp_rate"]
        min_similarity = sim_cfg["min_similarity"]
        re_calc_factor_left = sim_cfg["re_calc_factor_left"]
        re_calc_factor_right = sim_cfg["re_calc_factor_right"]
        segments_list = sim_cfg["segments_list"]
        segments_str = str(segments_list).replace('[', '').replace(']', '')
        #---------------------------------------#
        min_similarity_slider_val = round(
            min_similarity / self.MIN_SIMILARITY_STEP, 0)
        if (amp_thresh is None): amp_thresh = 1
        sim_cfg["asym_amp_thresh"] = amp_thresh
        #---------------------------------------#
        self.ui.inpC1.setValue(c1)
        self.ui.inpC2.setValue(c2)
        self.ui.inpPSNR.setValue(float(psnr))
        self.ui.inpAmpThresh.setValue(float(amp_thresh))
        self.ui.inpReCalcFactorLeft.setValue(float(re_calc_factor_left))
        self.ui.inpReCalcFactorRight.setValue(float(re_calc_factor_right))
        self.ui.cbbSegments.setCurrentText(segments_str)
        self.ui.sldMinSimilarity.setValue(int(min_similarity_slider_val))
        self.ui.grpBoxMinSimilarity.setTitle("Minimum similarity (%): " +
                                             str(min_similarity))
        self.ui.sldAmpRate.setValue(int(amp_rate))
        self.ui.grpBoxAmpRate.setTitle("Amplification rate: " + str(amp_rate))

    def __view_image_sample(self):
        manager = DetectorConfig.instance().get_manager()
        left = manager.get_sample_left()
        right = manager.get_sample_right()
        self.__sample_left, self.__sample_right = self.__preprocess_color(
            left, right)
        label_h = self.image1.height()
        img_size = (156, label_h - 30)
        m_left = cv2.resize(self.__sample_left,
                            img_size,
                            interpolation=cv2.INTER_AREA)
        m_right = cv2.resize(self.__sample_right,
                             img_size,
                             interpolation=cv2.INTER_AREA)
        self.image_sample_left.imshow(m_left)
        self.image_sample_right.imshow(m_right)

    def inp_re_calc_left_changed(self):
        value = self.ui.inpReCalcFactorLeft.value()
        self.__current_cfg["sim_cfg"]["re_calc_factor_left"] = value
        return

    def inp_re_calc_right_changed(self):
        value = self.ui.inpReCalcFactorRight.value()
        self.__current_cfg["sim_cfg"]["re_calc_factor_right"] = value
        return

    def inp_asym_amp_thresh_changed(self):
        value = self.ui.inpAmpThresh.value()
        self.__current_cfg["sim_cfg"]["asym_amp_thresh"] = value
        return

    def inp_C1_changed(self):
        value = self.ui.inpC1.value()
        self.__current_cfg["sim_cfg"]["C1"] = value
        return

    def inp_C2_changed(self):
        value = self.ui.inpC2.value()
        self.__current_cfg["sim_cfg"]["C2"] = value
        return

    def inp_PSNR_changed(self):
        value = self.ui.inpPSNR.value()
        self.__current_cfg["sim_cfg"]["psnr_trigger"] = value
        return

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
            trio.run(self.__detect_asym_diff, left, right)
            left = cv2.resize(left, img_size)
            right = cv2.resize(right, img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)

    async def __detect_asym_diff(self, left, right):
        sim_cfg = self.__current_cfg["sim_cfg"]
        min_sim = sim_cfg['min_similarity']
        manager = DetectorConfig.instance().get_manager()
        left_result, right_result = await manager.detect_asym(
            self.__current_cfg, left, right, self.__sample_left,
            self.__sample_right, None)
        is_asym_diff_left, avg_asym_left, avg_amp_left, recalc_left, res_list_l, amp_res_list_l = left_result
        is_asym_diff_right, avg_asym_right, avg_amp_right, recalc_right, res_list_r, amp_res_list_r = right_result

        # calculate calc_factor both side and then keep the highest only
        tmp_re_calc_factor_left = avg_asym_left / avg_amp_left
        tmp_re_calc_factor_right = avg_asym_right / avg_amp_right
        if (tmp_re_calc_factor_left > sim_cfg['re_calc_factor_left']):
            sim_cfg['re_calc_factor_left'] = tmp_re_calc_factor_left
        if (tmp_re_calc_factor_right > sim_cfg['re_calc_factor_right']):
            sim_cfg['re_calc_factor_right'] = tmp_re_calc_factor_right

        # update result to screen
        self.ui.inpReCalcFactorLeft.setValue(sim_cfg["re_calc_factor_left"])
        self.ui.inpReCalcFactorRight.setValue(sim_cfg["re_calc_factor_right"])

        # result display
        cur = datetime.datetime.now()
        cur_date_str = cur.strftime(ISO_DATE_FORMAT)
        left_result_text = "PASSED" if not is_asym_diff_left else "FAILED"
        right_result_text = "PASSED" if not is_asym_diff_right else "FAILED"
        result_text = f"<b>RESULT</b><br/>" + f"<b>Time</b>: {cur_date_str}<br/>"
        result_text += f"<b>Original similarity</b>: Left {avg_asym_left:.2f} - Right {avg_asym_right:.2f}<br/>"
        result_text += f"<b>Final similarity</b>: Left {recalc_left:.2f} - Right {recalc_right:.2f}<br/>"
        result_text += f"<b>Final result</b>: Left {left_result_text} - Right {right_result_text}"
        self.ui.inpResult.setHtml(result_text)

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
        if pair is not None:
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
