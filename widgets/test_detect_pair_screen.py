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
    __detected_pair = None
    backscreen: Signal
    nextscreen: Signal
    captured = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_test_detect_pair_screen()
        self.__current_cfg = None
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        self.image1 = ImageWidget()
        self.image2 = ImageWidget()
        self.image3 = ImageWidget()
        self.imageLayout = self.ui.screen1.parentWidget().layout()
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
        self.imageLayout.replaceWidget(self.ui.screen2, self.image2)
        self.imageLayout.replaceWidget(self.ui.screen4, self.image3)
        self.ui.screen1.deleteLater()
        self.ui.screen2.deleteLater()
        self.ui.screen4.deleteLater()

    def showEvent(self, event):
        _, self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        self.__detected_pair = None
        self.image3.imshow(None)
        manager = DetectorConfig.instance().get_manager()
        left = manager.get_sample_left()
        right = manager.get_sample_right()
        if left is not None:
            label_w = self.image1.width()
            label_h = self.image1.height()
            images = [left, right]
            self.__detected_pair = images
            final_img = helpers.concat_images(images, label_w, label_h)
            self.image3.imshow(final_img)
        self.__set_btn_next_enabled()
        self.__set_btn_capture_text()
        self.__load_config()

    # binding
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        self.ui.btnSaveSample.clicked.connect(self.btn_save_sample_clicked)
        self.ui.btnRetakeSample.clicked.connect(self.btn_retake_sample_clicked)

    def btn_capture_clicked(self):
        self.captured.emit()
        self.__set_btn_capture_text()

    def __set_btn_capture_text(self):
        timer_active = DetectorConfig.instance().get_timer().isActive()
        self.ui.btnCapture.setText("CAPTURE" if not timer_active else "STOP")

    def __set_btn_next_enabled(self):
        manager = DetectorConfig.instance().get_manager()
        left = manager.get_sample_left()
        has_sample = left is not None
        self.ui.btnNext.setEnabled(has_sample)

    def view_cam(self, image):
        # read image in BGR format
        label_w = self.image1.width()
        label_h = self.image1.height()
        dim = (label_w, label_h)
        if image is None:
            self.image1.imshow(image)
            self.image2.imshow(image)
            # self.image3.imshow(image)
            return
        contour, detected, detected_pair = self.__process_pair(image.copy())
        img_resized = cv2.resize(image, dim)
        contour_resized = cv2.resize(contour, dim)
        self.image1.imshow(img_resized)
        self.image2.imshow(contour_resized)
        if detected is not None and self.__detected_pair is None:
            self.image3.imshow(detected)
            self.__detected_pair = detected_pair

    def __load_config(self):
        return

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
            label_w = self.image3.width()
            label_h = self.image3.height()
            images = [left, right]
            final_img = helpers.concat_images(images, label_w, label_h)
            return image, final_img, images
        return image, None, None

    def btn_save_sample_clicked(self):
        if self.__detected_pair is not None:
            left, right = self.__detected_pair
            folder_path = DetectorConfig.instance().get_current_path()
            if folder_path is None:
                helpers.show_message("You must save configuration first")
                return
            cv2.imwrite(os.path.join(folder_path, detector.SAMPLE_LEFT_FILE),
                        left)
            cv2.imwrite(os.path.join(folder_path, detector.SAMPLE_RIGHT_FILE),
                        right)
            DetectorConfig.instance().get_manager().load_sample_images()
            helpers.show_message("Save successfully")
            self.__set_btn_next_enabled()

    def btn_retake_sample_clicked(self):
        self.__detected_pair = None
        manager = DetectorConfig.instance().get_manager()
        manager.reset_samples()
        self.__set_btn_next_enabled()
        self.image3.imshow(None)
