from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from app_models.detector_config import DetectorConfig

import cv2
import os
import imutils
import numpy as np
from FQCS import detector, helper, manager
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
        self.detector_cfg = DetectorConfig.instance()
        self.manager = manager.FQCSManager()
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
            self.dim = (self.label_w, self.label_h)
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.imageLayout.replaceWidget(self.ui.screen2, self.image2)
            self.imageLayout.replaceWidget(self.ui.screen4, self.image3)
            self.CAMERA_LOADED = True

    def process_image(self, image):
        detected = None
        detector_cfg = self.detector_cfg.config
        d_cfg = detector_cfg["d_cfg"]
        manager = self.manager

        # define sample_area for grouping
        sample_area = None
        sample_left, sample_right = None, None
        sample_left_path = None
        if os.path.exists(sample_left_path or "/a/b"):
            sample_left = cv2.imread(sample_left_path)
            sample_right = cv2.imread(sample_right_path)
            sample_area = sample_left.shape[0] * sample_left.shape[1]

        frame_width, frame_height = detector_cfg["frame_width"], detector_cfg[
            "frame_height"]
        min_width, min_height = detector_cfg["min_width_per"], detector_cfg[
            "min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height
        find_contours_func = detector.get_find_contours_func_by_method(
            detector_cfg["detect_method"])

        # adjust thresh
        if (detector_cfg["detect_method"] == "thresh"):
            adj_thresh = d_cfg["light_adj_thresh"]
            if adj_thresh is not None and adj_thresh > 0:
                adj_bg_thresh = helper.adjust_thresh_by_brightness(
                    image, d_cfg["light_adj_thresh"], d_cfg["bg_thresh"])
            else:
                adj_bg_thresh = d_cfg["bg_thresh"]
            d_cfg["adj_bg_thresh"] = adj_bg_thresh
        elif (detector_cfg["detect_method"] == "range"):
            adj_thresh = d_cfg["light_adj_thresh"]
            if adj_thresh is not None and adj_thresh > 0:
                adj_cr_to = helper.adjust_crange_by_brightness(
                    image, d_cfg["light_adj_thresh"], d_cfg["cr_to"])
                d_cfg["adj_cr_to"] = adj_cr_to
            else:
                d_cfg["adj_cr_to"] = d_cfg["cr_to"]

        boxes, proc = detector.find_contours_and_box(
            image,
            find_contours_func,
            d_cfg,
            min_width=min_width,
            min_height=min_height,
            detect_range=detector_cfg['detect_range'])

        final_grouped, _, _, check_group_idx = manager.group_pairs(
            boxes, sample_area)
        group_count = manager.get_last_group_count()

        pair, split_left, split_right = None, None, None
        check_group = None
        if check_group_idx is not None:
            check_group = final_grouped[check_group_idx]
            image_detect = image.copy()
            pair, image_detect, split_left, split_right, check_group = detector.detect_pair_and_size(
                image_detect,
                find_contours_func,
                d_cfg,
                check_group,
                stop_condition=detector_cfg['stop_condition'])
            final_grouped[check_group_idx] = check_group

        # output
        unit = detector_cfg["length_unit"]
        per_10px = detector_cfg["length_per_10px"]
        sizes = []
        for idx, group in enumerate(final_grouped):
            for b in group:
                c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
                if per_10px:
                    lH, lW = helper.calculate_length(
                        dimA,
                        per_10px), helper.calculate_length(dimB, per_10px)
                    sizes.append((lH, lW))
                else:
                    lH, lW = dimA, dimB
                    sizes.append((lH, lW))
                    unit = "px"
                cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0),
                                 2)
                cv2.putText(image, f"{idx}/ {lW:.1f} {unit}", (tl[0], tl[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 0), 2)
                cv2.putText(image, f"{lH:.1f} {unit}", (br[0], br[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 0), 2)

        if (pair is not None):
            check_group_min_x = manager.get_min_x(check_group)
            manager.check_group(check_group_min_x)
            left, right = pair
            left, right = left[0], right[0]

            max_width = max((left.shape[0], right.shape[0]))
            temp_left = imutils.resize(left, height=max_width)
            temp_right = imutils.resize(right, height=max_width)
            detected = np.concatenate((temp_left, temp_right), axis=1)
            return image, detected, [left, right]

        return image, None, None

    def save_sample(self):
        if self.detected_pair is not None:
            left, right = self.detected_pair
            folder_path = DetectorConfig.instance().current_path
            if folder_path is None:
                folder_path = helpers.file_chooser_open_directory(self)
                DetectorConfig.instance().current_path = folder_path
            left = cv2.flip(left, 1)
            # if not os.path.exists(os.path.join(folder_path,
            #                       detector.SAMPLE_LEFT_FILE):
            cv2.imwrite(os.path.join(folder_path, detector.SAMPLE_LEFT_FILE),
                        left)
            cv2.imwrite(os.path.join(folder_path, detector.SAMPLE_RIGHT_FILE),
                        right)
            print(f"save successful at {folder_path}")

    def reset_sample(self):
        self.detected_pair = None
        self.image3.imreset()
