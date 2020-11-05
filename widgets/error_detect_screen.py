from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from app_models.detector_config import DetectorConfig
from app import helpers
from views.error_detect_screen import Ui_ErrorDetectScreen
from FQCS import detector
from FQCS.tf2_yolov4.anchors import YOLOV4_ANCHORS
from FQCS.tf2_yolov4.model import YOLOv4
from FQCS.tf2_yolov4.convert_darknet_weights import convert_darknet_weights

import csv
import os
import asyncio
import trio


class ErrorDetectScreen(QWidget):
    backscreen: Signal
    nextscreen: Signal

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
            "160", "240", "256", "480", "660", "720", "800", "960", "1024",
            "1216", "1280"
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
        self.ui.btnCapture.clicked.connect(self.trigger_yolo_process)

    def trigger_yolo_process(self):
        if self.sender() == self.ui.btnCapture:
            trio.run(self.load_yolov4_model)

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
        self.detector_cfg["err_cfg"]["num_classes"] = len(class_list)
        print(self.detector_cfg["err_cfg"]["classes"])
        print(self.detector_cfg["err_cfg"]["num_classes"])

        # get file name
        _, tail = os.path.split(file_name[0])

        self.ui.inpClasses.setText(str(tail))

    async def load_yolov4_model(self):
        if not os.path.exists("./yolov4.h5"):
            convert_darknet_weights("./yolov4-custom_best.weights",
                                    "./yolo4.h5", (416, 416, 3),
                                    1,
                                    weights=None)
            return

        img_size = self.detector_cfg["err_cfg"]["img_size"]
        inp_shape = self.detector_cfg["err_cfg"]["inp_shape"]
        yolo_iou_threshold = self.detector_cfg["err_cfg"]["yolo_iou_threshold"]
        yolo_max_boxes = self.detector_cfg["err_cfg"]["yolo_max_boxes"]
        yolo_score_threshold = self.detector_cfg["err_cfg"][
            "yolo_score_threshold"]
        weights = self.detector_cfg["err_cfg"]["weights"]
        classes = self.detector_cfg["err_cfg"]["classes"]
        num_classes = self.detector_cfg["err_cfg"]["num_classes"]
        training = False

        model = asyncio.create_task(
            detector.get_yolov4_model(
                inp_shape=self.detector_cfg["err_cfg"]["inp_shape"],
                num_classes=self.detector_cfg["err_cfg"]["num_classes"],
                training=False,
                yolo_max_boxes=self.detector_cfg["err_cfg"]["yolo_max_boxes"],
                yolo_iou_threshold=self.detector_cfg["err_cfg"]
                ["yolo_iou_threshold"],
                weights=self.detector_cfg["err_cfg"]["weights"],
                yolo_score_threshold=self.detector_cfg["err_cfg"]
                ["yolo_score_threshold"]))
        CLASSES = self.detector_cfg["err_cfg"]["classes"]

        import matplotlib.pyplot as plt
        from FQCS.tf2_yolov4 import helper
        import numpy as np

        model = await model
        while True:
            img1 = cv2.imread(
                "/Users/bitumhoang/Downloads/dirty_sorted/dirty_sorted/" +
                str(np.random.randint(151, 324)) + ".jpg")
            img2 = cv2.imread(
                "/Users/bitumhoang/Downloads/dirty_sorted/dirty_sorted/" +
                str(np.random.randint(151, 324)) + ".jpg")
            images = [img1, img2]

            err_task = asyncio.create_task(
                detector.detect_errors(
                    model, images, self.detector_cfg["err_cfg"]["img_size"]))

            boxes, scores, classes, valid_detections = await err_task

            print(boxes)
            helper.draw_results(
                images,
                boxes,
                scores,
                classes,
                CLASSES,
                self.detector_cfg["err_cfg"]["img_size"],
                min_score=self.detector_cfg["err_cfg"]["yolo_score_threshold"])
            cv2.imshow("Prediction", images[0])
            cv2.waitKey()
            cv2.imshow("Prediction", images[1])
            if (cv2.waitKey() == 27):
                break
