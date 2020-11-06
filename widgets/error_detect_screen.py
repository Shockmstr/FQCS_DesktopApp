from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from app_models.detector_config import DetectorConfig
from app import helpers
from views.error_detect_screen import Ui_ErrorDetectScreen
from FQCS import detector, helper
from FQCS.tf2_yolov4.anchors import YOLOV4_ANCHORS
from FQCS.tf2_yolov4.model import YOLOv4
import csv
import os
import cv2
import imutils
import matplotlib.pyplot as plt
from FQCS.tf2_yolov4 import helper as tf_helper
import numpy as np
import asyncio
import trio


class ErrorDetectScreen(QWidget):
    CAMERA_LOADED = False
    SAVED = False
    backscreen: Signal
    nextscreen: Signal
    initing = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ErrorDetectScreen()
        self.detector_cfg = DetectorConfig.instance().config
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnFinish.clicked
        self.init_ui_values()
        self.binding()
        self.load_cfg()
        # trio.run(self.load_yolov4_model)

    def load_cfg(self):
        img_size = self.detector_cfg["err_cfg"]["img_size"]
        inp_shape = self.detector_cfg["err_cfg"]["inp_shape"]
        yolo_iou_threshold = self.detector_cfg["err_cfg"]["yolo_iou_threshold"]
        yolo_max_boxes = self.detector_cfg["err_cfg"]["yolo_max_boxes"]
        yolo_score_threshold = self.detector_cfg["err_cfg"][
            "yolo_score_threshold"]
        weights = self.detector_cfg["err_cfg"]["weights"]
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
        self.ui.inpClasses.setText(str(classes))

    def init_ui_values(self):
        self.height_value = 0
        self.width_value = 0
        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)

        frame_resize_values = [
            "160", "240", "320", "480", "560", "640", "720", "800", "960",
            "1024", "1216", "1280"
        ]
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

    def choose_model_clicked(self):
        file_name, _ = helpers.file_chooser_open_file(self)
        self.ui.inpModelChoice.setText(file_name.split(r"/")[-1])
        self.detector_cfg["err_cfg"]["weights"] = file_name

    def choose_classes_clicked(self):
        class_list = []
        file_name = QFileDialog.getOpenFileName(self, 'open file')
        with open(str(file_name[0]), newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                class_list.extend(row)

            print(class_list)
        self.detector_cfg["err_cfg"]["classes"] = class_list
        self.detector_cfg["err_cffg"]["num_classes"] = len(class_list)
        print(self.detector_cfg["err_cfg"]["classes"])
        print(self.detector_cfg["err_cfg"]["num_classes"])

        # get file name
        _, tail = os.path.split(file_name[0])

        self.ui.inpClasses.setText(str(tail))

    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        orig = cv2.resize(self.img, self.dim)
        self.image1.imshow(orig)
        trio.run(self.process_image, orig)

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

    def load_yolov4_model(self):
        print("Loaded yolo")
        trio.run(self.__load_yolov4_model)

    async def __load_yolov4_model(self):
        if not os.path.exists(r"F:\Capstone\project\FQCS_DesktopApp\yolo4.h5"):
            return
        #TODO: set absolute path for weights in cfg
        self.detector_cfg["err_cfg"][
            "weights"] = r"F:\Capstone\project\FQCS_DesktopApp\yolo4.h5"

        model = detector.get_yolov4_model(
            inp_shape=self.detector_cfg["err_cfg"]["inp_shape"],
            num_classes=self.detector_cfg["err_cfg"]["num_classes"],
            training=False,
            yolo_max_boxes=self.detector_cfg["err_cfg"]["yolo_max_boxes"],
            yolo_iou_threshold=self.detector_cfg["err_cfg"]
            ["yolo_iou_threshold"],
            weights=self.detector_cfg["err_cfg"]["weights"],
            yolo_score_threshold=self.detector_cfg["err_cfg"]
            ["yolo_score_threshold"])

        self.model = await model

    async def show_error(self, images):
        if self.model is None: return

        CLASSES = self.detector_cfg["err_cfg"]["classes"]
        err_task = detector.detect_errors(
            self.model, images, self.detector_cfg["err_cfg"]["img_size"])

        boxes, scores, classes, valid_detections = await err_task

        images = helper_tf.draw_results(
            images,
            boxes,
            scores,
            classes,
            CLASSES,
            self.detector_cfg["err_cfg"]["img_size"],
            min_score=self.detector_cfg["err_cfg"]["yolo_score_threshold"])

        images[0] *= 255.
        images[1] *= 255.
        images[0] = np.asarray(images[0], np.uint8)
        images[0] = np.asarray(images[0], np.uint8)

        self.image3.imshow(images[0])

    async def process_pair(self, image):
        detected = None
        frame_width, frame_height = self.detector_cfg[
            "frame_width"], self.detector_cfg["frame_height"]
        min_width, min_height = self.detector_cfg[
            "min_width_per"], self.detector_cfg["min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height
        find_contours_func = detector.get_find_contours_func_by_method(
            self.detector_cfg["detect_method"])

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

            max_width = max((left.shape[0], right.shape[0]))
            temp_left = imutils.resize(left, height=max_width)
            temp_right = imutils.resize(right, height=max_width)
            detected = np.concatenate((temp_left, temp_right), axis=1)

            # if pair is detected, detected is not None
            return image, detected, (left, right)
        # if no pair detected, return None
        return image, None, None

    async def process_image(self, image):
        contour, _, detected_pair = await self.process_pair(image)
        contour = cv2.resize(contour, self.dim)
        self.image2.imshow(contour)
        if detected_pair is not None:
            await self.show_error(detected_pair)
