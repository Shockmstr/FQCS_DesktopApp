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
    CAMERA_LOADED = False
    IMAGE_LOADED = False
    detected_pair = None
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.detector_cfg = DetectorConfig.instance().config
        self.ui = Ui_AsymConfigScreen()
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.load_cfg()
        self.binding()

    # binding
    def binding(self):
        self.ui.sldAmpRate.valueChanged.connect(self.amplification_rate_changed)
        self.ui.sldMinSimilarity.valueChanged.connect(self.min_similarity_changed)

    # handlers
    def amplification_rate_changed(self):
        value = self.ui.sldAmpRate.value()
        self.detector_cfg["sim_cfg"]["asym_amp_rate"] = value
        self.ui.grpBoxAmpRate.setTitle("Amplification rate: " + str(value))

    def min_similarity_changed(self):
        value = round(self.ui.sldMinSimilarity.value() * self.MIN_SIMILARITY_STEP, 2)
        self.detector_cfg["sim_cfg"]["min_similarity"] = value
        self.ui.grpBoxMinSimilarity.setTitle("Minimum similarity (%): " + str(value))

    def load_cfg(self):
        cfg = self.detector_cfg["sim_cfg"]
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
        min_similarity_slider_val = round(min_similarity / self.MIN_SIMILARITY_STEP, 0)
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
        self.ui.grpBoxMinSimilarity.setTitle("Minimum similarity (%): " + str(min_similarity))
        self.ui.sldAmpRate.setValue(int(amp_rate))
        self.ui.grpBoxAmpRate.setTitle("Amplification rate: " + str(amp_rate))

    def view_image_sample(self):
        left_path = '/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/resources/sample_left.jpg'
        # helpers.get_current_sample_image_path(
        #     self) + os.sep + detector.SAMPLE_LEFT_FILE
        right_path = '/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/resources/sample_right.jpg'
        # helpers.get_current_sample_image_path(
        #     self) + os.sep + detector.SAMPLE_RIGHT_FILE
        left = cv2.imread(left_path)
        right = cv2.imread(right_path)
        m_left, m_right = self.preprocess_color(left, right)
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
        contour, detected, detected_pair = self.process_image(self.img.copy())
        contour_resized = cv2.resize(contour, self.dim)
        self.image1.imshow(contour_resized)
        if detected_pair is not None:
            left, right = self.preprocess_color(detected_pair[0], detected_pair[1])
            left = cv2.flip(left, 1)
            trio.run(self.detect_asym_diff, left, right)
            left = cv2.resize(left, img_size)
            right = cv2.resize(right, img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)
            self.detected_pair = detected_pair


    def replace_image_widget(self):
        if not self.CAMERA_LOADED:
            self.image_detect_left = ImageWidget()
            self.image_detect_right = ImageWidget()
            self.image_sample_left = ImageWidget()
            self.image_sample_right = ImageWidget()
            #       
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()

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
            self.IMAGE_LOADED = True

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.CAMERA_LOADED = True


    avg_min = 1
    re_calc_factor_left = 0
    re_calc_factor_right = 0
    async def detect_asym_diff(self, left, right):
        sample_left_path = '/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/resources/sample_left.jpg'
        # helpers.get_current_sample_image_path(
        #     self) + os.sep + detector.SAMPLE_LEFT_FILE
        sample_right_path = '/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/resources/sample_left.jpg'
        # helpers.get_current_sample_image_path(
        #     self) + os.sep + detector.SAMPLE_RIGHT_FILE
        sample_left, sample_right = self.preprocess_color(
            cv2.imread(sample_left_path), cv2.imread(sample_right_path))
        cfg = self.detector_cfg["sim_cfg"]
        min_sim = self.detector_cfg["sim_cfg"]['min_similarity']

        
        is_asym_diff_left, self.avg_asym_left, self.avg_amp_left, recalc_left, res_list_l, amp_res_list_l = (
            await detector.detect_asym_diff(
                left, sample_left, cfg['segments_list'],
                cfg['C1'], cfg['C2'], cfg['psnr_trigger'],
                cfg['asym_amp_thresh'], cfg['asym_amp_rate'],
                cfg['re_calc_factor_left'],
                min_sim))
        is_asym_diff_right, self.avg_asym_right, self.avg_amp_right, recalc_right, res_list_r, amp_res_list_r = (
            await detector.detect_asym_diff(
                right, sample_right, cfg['segments_list'],
                cfg['C1'], cfg['C2'], cfg['psnr_trigger'],
                cfg['asym_amp_thresh'], cfg['asym_amp_rate'],
                cfg['re_calc_factor_right'],
                min_sim))
        # find smaller value between the value of asym left and right 
        self.tmp_min = min(self.avg_asym_left, self.avg_asym_right)
        print("tmpmin - ", self.tmp_min)
        
        # find the smallest ASYM value among all detected shoes
        if (self.tmp_min < self.avg_min): self.avg_min = self.tmp_min
        print("avg_min - ", self.avg_min)
        
        # calculate calc_factor both side and then keep the highest only
        self.tmp_re_calc_factor_left = self.avg_asym_left / self.avg_amp_left
        self.tmp_re_calc_factor_right = self.avg_asym_right / self.avg_amp_right
        if(self.tmp_re_calc_factor_left > self.re_calc_factor_left): self.re_calc_factor_left = self.tmp_re_calc_factor_left
        if(self.tmp_re_calc_factor_right > self.re_calc_factor_right): self.re_calc_factor_right = self.tmp_re_calc_factor_right

        # update configure value
        self.detector_cfg['asym_amp_thresh'] = self.avg_min
        self.detector_cfg['re_calc_factor_left'] = self.re_calc_factor_left
        self.detector_cfg['re_calc_factor_right'] = self.re_calc_factor_right

        # update result to screen
        self.ui.inpAmpThresh.setValue(self.avg_min)
        self.ui.inpReCalcFactorLeft.setValue(self.re_calc_factor_left)
        self.ui.inpReCalcFactorRight.setValue(self.re_calc_factor_right)



    def showEvent(self, event):
        self.replace_image_widget()
        self.view_image_sample()


    def preprocess_color(self, sample_left, sample_right):
        c_cfg = self.detector_cfg['color_cfg']
        #print(c_cfg)
        pre_sample_left = detector.preprocess_for_color_diff(
            sample_left, c_cfg['img_size'], c_cfg['blur_val'],
            c_cfg['alpha_l'], c_cfg['beta_l'], c_cfg['sat_adj'])
        pre_sample_right = detector.preprocess_for_color_diff(
            sample_right, c_cfg['img_size'], c_cfg['blur_val'],
            c_cfg['alpha_r'], c_cfg['beta_r'], c_cfg['sat_adj'])
        return pre_sample_left, pre_sample_right



    def process_image(self, image):
        detected = None

        frame_width, frame_height = self.detector_cfg[
            "frame_width"], self.detector_cfg["frame_height"]
        min_width, min_height = self.detector_cfg[
            "min_width_per"], self.detector_cfg["min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height
        find_contours_func = detector.get_find_contours_func_by_method(
            self.detector_cfg["detect_method"])

        # adjust thresh
        if (self.detector_cfg["detect_method"] == "thresh"):
            adj_bg_thresh = helper.adjust_thresh_by_brightness(
                image, self.detector_cfg["d_cfg"]["light_adj_thresh"],
                self.detector_cfg["d_cfg"]["bg_thresh"])
            self.detector_cfg["d_cfg"]["adj_bg_thresh"] = adj_bg_thresh
        elif (self.detector_cfg["detect_method"] == "range"):
            adj_cr_to = helper.adjust_crange_by_brightness(
                image, self.detector_cfg["d_cfg"]["light_adj_thresh"],
                self.detector_cfg["d_cfg"]["cr_to"])
            self.detector_cfg["d_cfg"]["adj_cr_to"] = adj_cr_to

        boxes, cnts, proc = detector.find_contours_and_box(
            image,
            find_contours_func,
            self.detector_cfg["d_cfg"],
            min_width=min_width,
            min_height=min_height)
        pair, image, split_left, split_right, boxes = detector.detect_pair_and_size(
            image,
            find_contours_func,
            self.detector_cfg["d_cfg"],
            boxes,
            cnts,
            stop_condition=self.detector_cfg['stop_condition'],
            detect_range=self.detector_cfg['detect_range'])

        # output
        unit = self.detector_cfg["length_unit"]
        per_10px = self.detector_cfg["length_per_10px"]
        sizes = []
        for b in boxes:
            rect, lH, lW, box, tl, tr, br, bl = b
            if (per_10px is not None):
                lH, lW = helper.calculate_length(
                    lH, per_10px), helper.calculate_length(lW, per_10px)
            sizes.append((lH, lW))
            cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0), 2)
            cv2.putText(image, f"{lW:.1f} {unit}", (tl[0], tl[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 0), 2)
            cv2.putText(image, f"{lH:.1f} {unit}", (br[0], br[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 0), 2)
        # cv2.imshow("Contours processed", proc)
        if pair is not None:
            left, right = pair
            left, right = left[0], right[0]
            h_diff, w_diff = detector.compare_size(sizes[0], sizes[1],
                                                   self.detector_cfg)

            # if split_left is not None:
            #     detected = np.concatenate((split_left, split_right), axis=1)
            max_width = max((left.shape[0], right.shape[0]))
            temp_left = imutils.resize(left, height=max_width)
            temp_right = imutils.resize(right, height=max_width)
            detected = np.concatenate((temp_left, temp_right), axis=1)
            return image, detected, (left, right)

        return image, None, None

