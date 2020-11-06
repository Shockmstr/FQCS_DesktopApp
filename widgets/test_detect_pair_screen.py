from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from app_models.detector_config import DetectorConfig

import cv2
import os
import imutils
import numpy as np
from FQCS import detector, helper
from widgets.image_widget import ImageWidget
from app import helpers
from views.test_detect_pair_screen import Ui_test_detect_pair_screen


class TestDetectPairScreen(QWidget):
    CAMERA_LOADED = False
    detected_pair = None
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_test_detect_pair_screen()
        self.detector_cfg = DetectorConfig.instance().config
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.binding()

    # binding
    def binding(self):
        self.ui.btnSaveSample.clicked.connect(self.save_sample)
        self.ui.btnRetakeSample.clicked.connect(self.reset_sample)

    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        contour, detected, detected_pair = self.process_image(self.img.copy())
        img_resized = cv2.resize(self.img, self.dim)
        contour_resized = cv2.resize(contour, self.dim)
        self.image1.imshow(img_resized)
        self.image2.imshow(contour_resized)
        if detected is not None and self.detected_pair is None:
            detected_resized = cv2.resize(detected, self.dim)
            self.image3.imshow(detected_resized)
            self.detected_pair = detected_pair

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.image2 = ImageWidget()
            self.image3 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.imageLayout.replaceWidget(self.ui.screen2, self.image2)
            self.imageLayout.replaceWidget(self.ui.screen4, self.image3)
            self.CAMERA_LOADED = True

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

    def save_sample(self):
        if self.detected_pair is not None:
            left, right = self.detected_pair
            folder_path = DetectorConfig.instance().current_path
            if folder_path is None:
                folder_path = helpers.file_chooser_open_directory(self)
                DetectorConfig.instance().current_path = folder_path
            left = cv2.flip(left, 1)
            if not os.path.exists(folder_path + r"/" +
                                  detector.SAMPLE_LEFT_FILE):
                cv2.imwrite(folder_path + r"/" + detector.SAMPLE_LEFT_FILE,
                            left)
                cv2.imwrite(folder_path + r"/" + detector.SAMPLE_RIGHT_FILE,
                            right)
                print(f"save successful at {folder_path}")

    def reset_sample(self):
        self.detected_pair = None
        self.image3.imreset()
