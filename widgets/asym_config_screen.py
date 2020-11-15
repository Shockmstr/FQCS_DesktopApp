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


class AsymConfigScreen(QWidget):
    MIN_SIMILARITY_STEP = 0.01
    __detected_pair = None
    __avg_min = 1
    __re_calc_factor_left = 0
    __re_calc_factor_right = 0
    backscreen: Signal
    nextscreen: Signal

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
        self.ui.sldAmpRate.valueChanged.connect(
            self.sld_amplification_rate_changed)
        self.ui.sldMinSimilarity.valueChanged.connect(
            self.sld_min_similarity_changed)

    # handlers
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
        self.__view_image_sample()
        self.__load_config()

    def __load_config(self):
        cfg = self.__current_cfg["sim_cfg"]
        c1 = cfg["C1"]
        c2 = cfg["C2"]
        psnr = cfg["psnr_trigger"]
        amp_thresh = cfg["asym_amp_thresh"]
        amp_rate = cfg["asym_amp_rate"]
        min_similarity = cfg["min_similarity"]
        re_calc_factor_left = cfg["re_calc_factor_left"]
        re_calc_factor_right = cfg["re_calc_factor_right"]
        segments_list = cfg["segments_list"]
        #---------------------------------------#
        min_similarity_slider_val = round(
            min_similarity / self.MIN_SIMILARITY_STEP, 0)
        if (amp_thresh is None): amp_thresh = 0
        #---------------------------------------#
        self.ui.inpC1.setValue(c1)
        self.ui.inpC2.setValue(c2)
        self.ui.inpPSNR.setValue(int(psnr))
        self.ui.inpAmpThresh.setValue(int(amp_thresh))
        self.ui.inpReCalcFactorLeft.setValue(int(re_calc_factor_left))
        self.ui.inpReCalcFactorRight.setValue(int(re_calc_factor_right))
        self.ui.inpSegments.setText(segments_list.__str__())
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
            left = cv2.flip(left, 1)
            trio.run(self.__detect_asym_diff, left, right)
            left = cv2.resize(left, img_size)
            right = cv2.resize(right, img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)
            self.__detected_pair = detected_pair

    async def __detect_asym_diff(self, left, right):
        cfg = self.__current_cfg["sim_cfg"]
        min_sim = self.__current_cfg["sim_cfg"]['min_similarity']
        manager = DetectorConfig.instance().get_manager()
        left_result, right_result = await manager.detect_asym(
            self.__current_cfg, left, right, self.__sample_left,
            self.__sample_right, None)
        is_asym_diff_left, avg_asym_left, avg_amp_left, recalc_left, res_list_l, amp_res_list_l = left_result
        is_asym_diff_right, avg_asym_right, avg_amp_right, recalc_right, res_list_r, amp_res_list_r = right_result
        # find smaller value between the value of asym left and right
        tmp_min = min(avg_asym_left, avg_asym_right)
        print("tmpmin - ", tmp_min)

        # find the smallest ASYM value among all detected shoes
        if (tmp_min < self.__avg_min): self.__avg_min = tmp_min
        print("avg_min - ", self.__avg_min)

        # calculate calc_factor both side and then keep the highest only
        tmp_re_calc_factor_left = avg_asym_left / avg_amp_left
        tmp_re_calc_factor_right = avg_asym_right / avg_amp_right
        if (tmp_re_calc_factor_left > self.__re_calc_factor_left):
            self.__re_calc_factor_left = tmp_re_calc_factor_left
        if (tmp_re_calc_factor_right > self.__re_calc_factor_right):
            self.__re_calc_factor_right = tmp_re_calc_factor_right

        # update configure value
        self.__current_cfg['asym_amp_thresh'] = self.__avg_min
        self.__current_cfg['re_calc_factor_left'] = self.__re_calc_factor_left
        self.__current_cfg[
            're_calc_factor_right'] = self.__re_calc_factor_right

        # update result to screen
        self.ui.inpAmpThresh.setValue(self.__avg_min)
        self.ui.inpReCalcFactorLeft.setValue(self.__re_calc_factor_left)
        self.ui.inpReCalcFactorRight.setValue(self.__re_calc_factor_right)

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
            max_width = max((left.shape[0], right.shape[0]))
            temp_left = imutils.resize(left, height=max_width)
            temp_right = imutils.resize(right, height=max_width)
            detected = np.concatenate((temp_left, temp_right), axis=1)
            return image, detected, [left, right]
        return image, None, None
