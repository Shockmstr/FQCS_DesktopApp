from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer, Signal, Qt
from widgets.image_widget import ImageWidget
from app_models.detector_config import DetectorConfig
import cv2
from FQCS import detector, helper
from app import helpers
import numpy as np
import os
import imutils
from views.color_param_calibration_screen import Ui_ColorParamCalibScreen


class ColorParamCalibrationScreen(QWidget):
    CAMERA_LOADED = False
    IMAGE_LOADED = False
    detected_pair = None
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.detector_cfg = DetectorConfig.instance().config
        self.ui = Ui_ColorParamCalibScreen()
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.load_default_config()
        self.binding()

    # binding
    def binding(self):
        self.ui.cbbCamera.setPlaceholderText("Choose Cam")
        self.ui.cbbCamera.setCurrentIndex(-1)
        self.ui.cbbCamera.currentIndexChanged.connect(self.cbbCamera_chose)
        self.ui.inpSuppThreshold.textChanged.connect(self.sup_thresh_change)
        self.ui.sldAllowDiff.valueChanged.connect(self.allow_diff_change)
        self.ui.sldAmpRate.valueChanged.connect(self.amp_rate_change)
        self.ui.ampThreshBlue.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshGreen.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshRed.textChanged.connect(self.amp_threshold_change)

    def amp_threshold_change(self):
        amp_thresh_green_value = float(self.ui.ampThreshGreen.text())
        amp_thresh_red_value = float(self.ui.ampThreshRed.text())
        amp_thresh_blue_value = float(self.ui.ampThreshBlue.text())
        self.detector_cfg["color_cfg"]["amplify_thresh"] = (
            amp_thresh_red_value, amp_thresh_green_value,
            amp_thresh_blue_value)

    def amp_rate_change(self):
        value = self.ui.sldAmpRate.value()
        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " + str(value))
        self.detector_cfg["color_cfg"]["amplify_rate"] = value

    def sup_thresh_change(self):
        value = self.ui.inpSuppThreshold.value()
        self.detector_cfg["color_cfg"]["supp_thresh"] = value

    def allow_diff_change(self):
        value = self.ui.sldAllowDiff.value() / 100
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference (%): " +
                                         str(value))
        self.detector_cfg["color_cfg"]["max_diff"] = value

    def cbbCamera_chose(self):
        self.replace_camera_widget()
        index = self.ui.cbbCamera.currentData()
        

    def load_default_config(self):
        #print(self.detector_cfg)
        # amp_thresh_red_value = self.detector_cfg["color_cfg"]["amplify_thresh"][0]
        # amp_thresh_green_value = self.detector_cfg["color_cfg"]["amplify_thresh"][1]
        # amp_thresh_blue_value = self.detector_cfg["color_cfg"]["amplify_thresh"][2]
        amplify_rate = self.detector_cfg["color_cfg"]["amplify_rate"]
        supp_thresh = self.detector_cfg["color_cfg"]["supp_thresh"]
        max_diff = self.detector_cfg["color_cfg"]["max_diff"]

        self.ui.sldAllowDiff.setValue(max_diff * 100)
        self.ui.sldAmpRate.setValue(amplify_rate)
        self.ui.inpSuppThreshold.setValue(supp_thresh)
        self.ui.ampThreshBlue.setValue(0)  # self-created value
        self.ui.ampThreshGreen.setValue(0)  # self-created value
        self.ui.ampThreshRed.setValue(0)  # self-created value

        self.ui.grpSldAllowDiff.setTitle("Amplification Rate: " +
                                         str(max_diff))
        self.ui.grpSldAmpRate.setTitle("Allowed Difference (%): " +
                                       str(amplify_rate))

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
            self.find_amp_threshold(left, right)
            left = cv2.resize(left, img_size)
            right = cv2.resize(right, img_size)
            self.image_detect_left.imshow(left)
            self.image_detect_right.imshow(right)       
            self.detected_pair = detected_pair

    def replace_image_widget(self):
        if not self.IMAGE_LOADED:
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
            self.IMAGE_LOADED = True

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.CAMERA_LOADED = True

    index = 1
    hist_bgr_list = []

    def find_amp_threshold(self, img_left, img_right):
        sample_left_path = '/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/resources/sample_left.jpg'
        helpers.get_current_sample_image_path(
            self) + os.sep + detector.SAMPLE_LEFT_FILE
        sample_right_path = '/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/resources/sample_left.jpg'
        helpers.get_current_sample_image_path(
            self) + os.sep + detector.SAMPLE_RIGHT_FILE
        sample_left, sample_right = self.preprocess_color(
            cv2.imread(sample_left_path), cv2.imread(sample_right_path))
        self.hist_bgr_list.append(
                np.abs(
                    np.subtract(helper.get_hist_bgr(img_left),
                                helper.get_hist_bgr(sample_left))))
        self.hist_bgr_list.append(
                np.abs(
                    np.subtract(helper.get_hist_bgr(img_left),
                                helper.get_hist_bgr(sample_left))))

        max_blue = 0
        max_green = 0
        max_red = 0
        for hist in self.hist_bgr_list:
            blue = np.max(hist[0])
            #print("hist blue:", hist[0].reshape(1,-1))
            green = np.max(hist[1])
            #print("hist green:", hist[1].reshape(1,-1))
            red = np.max(hist[2])
            #print("hist red:", hist[2].reshape(1,-1))
            if (blue > max_blue): max_blue = blue
            if (green > max_green): max_green = green
            if (red > max_red): max_red = red
        amp_thresh = (int(max_red), int(max_green), int(max_blue))
        self.ui.ampThreshRed.setValue(amp_thresh[0])
        self.ui.ampThreshGreen.setValue(amp_thresh[1])
        self.ui.ampThreshBlue.setValue(amp_thresh[2])
        self.detector_cfg["color_cfg"]["amplify_thresh"] = amp_thresh
        self.hist_bgr_list.clear()

    def showEvent(self, event):
        self.replace_image_widget()
        self.view_image_sample()
        
    #image process function

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