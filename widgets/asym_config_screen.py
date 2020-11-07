from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from views.asym_config_screen import Ui_AsymConfigScreen
from app_models.detector_config import DetectorConfig
from widgets.image_widget import ImageWidget
from FQCS import detector, helper
import imutils
import cv2
import numpy as np


class AsymConfigScreen(QWidget):
    MIN_SIMILARITY_STEP = 0.01
    CAMERA_LOADED = False
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_AsymConfigScreen()
        self.ui.setupUi(self)
        self.detector_cfg = DetectorConfig.instance().config
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.binding()
        self.load_cfg()
        
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

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.image2 = ImageWidget()            
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1) 
            self.imageLayout.replaceWidget(self.ui.screen2, self.image1)   
            self.CAMERA_LOADED = True

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

    # def process_ssim(self, image):
    #     detected = None

    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        self.img = cv2.resize(self.img, self.dim)
        img_size = (128, self.label_h - 50)
        contour, detected, detected_pair = self.process_image(self.img.copy())
        contour_resized = cv2.resize(contour, self.dim)
        self.image1.imshow(contour_resized)
        self.image1.imshow(contour_resized)
        if detected is not None and self.detected_pair is None:
            left = cv2.resize(detected_pair[0], img_size)
            right = cv2.resize(detected_pair[1], img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)
            self.detected_pair = detected_pair

    def process_image(self, image):
        detected = None 

        uri = "/Users/bitumhoang/Desktop/capstone/FQCS-Research/FQCS.ColorDetection/FQCS_detector/test.mp4"
        cap = cv2.VideoCapture(uri)
        frame_width, frame_height = self.detector_cfg[
            "frame_width"], self.detector_cfg["frame_height"]
        min_width, min_height = self.detector_cfg[
            "min_width_per"], self.detector_cfg["min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height
        find_contours_func = detector.get_find_contours_func_by_method(
            self.detector_cfg["detect_method"])

        found = False
        while(cap.isOpened()):   
            _, image = cap.read()
            image = cv2.resize(image, (frame_width, frame_height))

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
        
            

            