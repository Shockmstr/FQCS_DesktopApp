from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QThreadPool
from app_models.detector_config import DetectorConfig
from app_models.app_config import AppConfig
from app import helpers
from views.error_detect_screen import Ui_ErrorDetectScreen
from FQCS import detector, helper, manager
from FQCS.tf2_yolov4.anchors import YOLOV4_ANCHORS
from FQCS.tf2_yolov4.model import YOLOv4
import csv
import os
import imutils
import cv2
from widgets.image_widget import ImageWidget
import imutils
import matplotlib.pyplot as plt
import numpy as np
from qasync import asyncSlot
from services.worker_runnable import WorkerRunnable


class ErrorDetectScreen(QWidget):
    CAMERA_LOADED = False
    SAVED = False
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ErrorDetectScreen()
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        self.app_cfg = AppConfig.instance().config
        self.manager = manager.FQCSManager()
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnFinish.clicked
        self.init_ui_values()
        self.binding()
        self.load_cfg()
        if not self.CAMERA_LOADED:
            self.ui.containerConfig.setEnabled(False)

    def load_cfg(self):
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        if self.detector_cfg is None: return
        img_size = self.detector_cfg["err_cfg"]["img_size"]
        inp_shape = self.detector_cfg["err_cfg"]["inp_shape"]
        yolo_iou_threshold = self.detector_cfg["err_cfg"]["yolo_iou_threshold"] / 10
        yolo_max_boxes = self.detector_cfg["err_cfg"]["yolo_max_boxes"]
        yolo_score_threshold = self.detector_cfg["err_cfg"][
            "yolo_score_threshold"]
        weights = self.detector_cfg["err_cfg"]["weights"].split("/")[-1].split("\\")[-1]
        classes = self.detector_cfg["err_cfg"]["classes"]
        num_classes = self.detector_cfg["err_cfg"]["num_classes"]

        width = self.detector_cfg["err_cfg"]["img_size"][1]
        height = self.detector_cfg["err_cfg"]["img_size"][0]

        width_index = self.ui.cbbWidth.findData(width)
        self.ui.cbbWidth.setCurrentIndex(width_index)
        height_index = self.ui.cbbHeight.findData(height)
        self.ui.cbbHeight.setCurrentIndex(height_index)

        self.ui.inpModelChoice.setText(weights)
        self.ui.inpIouThreshold.setValue(yolo_iou_threshold * 10)
        self.ui.inpMaxInstances.setValue(yolo_max_boxes)
        self.ui.inpMinimumScore.setValue(yolo_score_threshold * 10)
        self.ui.inpClasses.setText(", ".join(classes))

    def init_ui_values(self):
        self.height_value = 0
        self.width_value = 0
        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)

        frame_resize_values = [str(32 * i) for i in range(1, 20, 2)]

        self.ui.cbbHeight.clear()
        for value in frame_resize_values:
            self.ui.cbbHeight.addItem(value, userData=int(value))

        self.ui.cbbWidth.clear()
        for value in frame_resize_values:
            self.ui.cbbWidth.addItem(value, userData=int(value))

    # binding
    def binding(self):
        self.ui.inpMaxInstances.textChanged.connect(self.max_instances_change)
        self.ui.inpMinimumScore.textChanged.connect(self.min_score_change)
        self.ui.inpIouThreshold.textChanged.connect(self.iou_threshold_change)
        self.ui.cbbHeight.currentIndexChanged.connect(self.image_resize)
        self.ui.cbbWidth.currentIndexChanged.connect(self.image_resize)
        self.ui.btnChooseModel.clicked.connect(self.choose_model_clicked)
        self.ui.btnChooseClasses.clicked.connect(self.choose_classes_clicked)
        self.ui.chkDefectDetection.stateChanged.connect(self.defect_detection_state_change)

    def defect_detection_state_change(self):
        if self.ui.chkDefectDetection.isChecked():
            self.detector_cfg["is_defect_enable"] = True
        else:
            self.detector_cfg["is_defect_enable"] = False

    # hander
    def min_score_change(self):
        value = self.ui.inpMinimumScore.value()
        self.detector_cfg["err_cfg"]["yolo_score_threshold"] = value / 10

    def max_instances_change(self):
        value = self.ui.inpMaxInstances.value()
        self.detector_cfg["err_cfg"]["yolo_max_boxes"] = value

    def iou_threshold_change(self):
        value = self.ui.inpIouThreshold.value()
        self.detector_cfg["err_cfg"]["yolo_iou_threshold"] = value / 10

    def image_resize(self):
        if self.sender() == self.ui.cbbHeight:
            self.height_value = self.ui.cbbHeight.currentData()
        if self.sender() == self.ui.cbbWidth:
            self.width_value = self.ui.cbbWidth.currentData()

        print(self.height_value, self.width_value)
        self.detector_cfg["err_cfg"]["img_size"] = (self.width_value,
                                                    self.height_value)
        self.detector_cfg["err_cfg"]["inp_shape"] = (self.height_value,
                                                     self.width_value, 3)

    @asyncSlot()
    async def choose_model_clicked(self):
        file_name, _ = helpers.file_chooser_open_file(self)
        if file_name is not None:
            self.ui.inpModelChoice.setText(file_name.split("/")[-1].split("\\")[-1])
            self.detector_cfg["err_cfg"]["weights"] = file_name
            await DetectorConfig.instance().manager.load_model(self.detector_cfg)

    def choose_classes_clicked(self):
        file_name, _= helpers.file_chooser_open_file(self)
        if file_name is not None:
            class_list = []
            with open(file_name, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter='\n')
                for row in spamreader:
                    class_list.extend(row)
            self.detector_cfg["err_cfg"]["classes"] = class_list
            self.detector_cfg["err_cfg"]["num_classes"] = len(class_list)
            self.ui.inpClasses.setText(", ".join(class_list))

    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        orig = cv2.resize(self.img, self.dim)
        self.image1.imshow(orig)
        self.process_image(self.img)

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
            self.ui.containerConfig.setEnabled(True)

    async def show_error(self, images):
        manager = DetectorConfig.instance().manager
        err_task = manager.detect_errors(self.detector_cfg, images, None)
        boxes, scores, classes, valid_detections = await err_task
        err_cfg = self.detector_cfg["err_cfg"]
        helper.draw_yolo_results(images,
                                 boxes,
                                 scores,
                                 classes,
                                 err_cfg["classes"],
                                 err_cfg["img_size"],
                                 min_score=err_cfg["yolo_score_threshold"])
        images[0] *= 255.
        images[1] *= 255.

        left = np.asarray(images[0], np.uint8)
        right = np.asarray(images[1], np.uint8)
        max_width = max((left.shape[0], right.shape[0]))
        temp_left = imutils.resize(left, height=max_width)
        temp_right = imutils.resize(right, height=max_width)
        detected = np.concatenate((temp_left, temp_right), axis=1)
        detected = cv2.resize(detected, self.dim)
        self.image3.imshow(detected)

    def __process_pair(self, image):
        manager = DetectorConfig.instance().manager
        boxes, proc = manager.extract_boxes(self.detector_cfg, image)
        final_grouped, sizes, check_group_idx, pair, split_left, split_right, image_detect = manager.detect_groups_and_checked_pair(
            self.detector_cfg, boxes, image)
        unit = self.detector_cfg["length_unit"]
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
            return image, [left, right]
        return image, None

    def process_image(self, image):
        manager = DetectorConfig.instance().manager
        contour, detected_pair = self.__process_pair(image)
        contour = cv2.resize(contour, self.dim)
        self.image2.imshow(contour)
        if detected_pair is not None and manager.get_model() is not None:
            runnable = WorkerRunnable(self.show_error,
                                      detected_pair,
                                      parent=self)
            runnable.work_error.connect(lambda ex: print(ex))
            QThreadPool.globalInstance().start(runnable)