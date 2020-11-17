from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QThreadPool
from app_models.detector_config import DetectorConfig
from app_models.app_config import AppConfig
from app import helpers
from views.error_detect_screen import Ui_ErrorDetectScreen
from FQCS import detector, helper, manager
import os
import imutils
import cv2
from widgets.image_widget import ImageWidget
import imutils
import matplotlib.pyplot as plt
import numpy as np
from qasync import asyncSlot
from services.worker_runnable import WorkerRunnable
import trio


class ErrorDetectScreen(QWidget):
    backscreen: Signal
    nextscreen: Signal
    captured = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ErrorDetectScreen()
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

        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)
        frame_resize_values = [str(32 * i) for i in range(1, 20)]

        self.ui.cbbHeight.clear()
        for value in frame_resize_values:
            self.ui.cbbHeight.addItem(value, userData=int(value))

        self.ui.cbbWidth.clear()
        for value in frame_resize_values:
            self.ui.cbbWidth.addItem(value, userData=int(value))

    def showEvent(self, event):
        _, self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        self.__set_btn_capture_text()
        self.__load_config()

    def __load_config(self):
        err_cfg = self.__current_cfg["err_cfg"]
        img_size = err_cfg["img_size"]
        inp_shape = err_cfg["inp_shape"]
        yolo_iou_threshold = err_cfg["yolo_iou_threshold"]
        yolo_max_boxes = err_cfg["yolo_max_boxes"]
        yolo_score_threshold = err_cfg["yolo_score_threshold"]
        weights = err_cfg["weights"]
        classes = err_cfg["classes"]
        num_classes = err_cfg["num_classes"]
        is_defect_enable = self.__current_cfg["is_defect_enable"]

        width = img_size[0]
        height = img_size[1]

        self.ui.cbbWidth.setCurrentText(str(width))
        self.ui.cbbHeight.setCurrentText(str(height))
        self.ui.chkDefectDetection.setChecked(is_defect_enable)

        self.ui.inpModelChoice.setText(weights)
        self.ui.sldIoUThresh.setValue(int(yolo_iou_threshold * 100))
        self.ui.groupIoUThresh.setTitle(f"IoU threshold: {yolo_iou_threshold}")
        self.ui.sldScoreThresh.setValue(int(yolo_score_threshold * 100))
        self.ui.groupScoreThresh.setTitle(
            f"Score threshold: {yolo_score_threshold}")
        self.ui.inpMaxInstances.setValue(yolo_max_boxes)
        self.ui.inpClasses.setText(", ".join(classes))

    # binding
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnFinish.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        self.ui.inpMaxInstances.textChanged.connect(
            self.inp_max_instances_changed)
        self.ui.sldScoreThresh.valueChanged.connect(
            self.sld_score_thresh_changed)
        self.ui.sldIoUThresh.valueChanged.connect(
            self.sld_iou_threshold_changed)
        self.ui.cbbHeight.currentIndexChanged.connect(
            self.width_height_changed)
        self.ui.cbbWidth.currentIndexChanged.connect(self.width_height_changed)
        self.ui.btnChooseModel.clicked.connect(self.btn_choose_model_clicked)
        self.ui.btnChooseClasses.clicked.connect(
            self.btn_choose_classes_clicked)
        self.ui.chkDefectDetection.stateChanged.connect(
            self.chk_defect_detection_state_changed)
        self.ui.btnReloadModel.clicked.connect(self.btn_reload_model_clicked)
        self.ui.btnChoosePicture.clicked.connect(
            self.btn_choose_picture_clicked)

    def chk_defect_detection_state_changed(self):
        checked = self.ui.chkDefectDetection.isChecked()
        self.__current_cfg["is_defect_enable"] = checked

    # hander
    @asyncSlot()
    async def btn_reload_model_clicked(self):
        await DetectorConfig.instance().get_manager().load_model(
            self.__current_cfg)

    def btn_capture_clicked(self):
        self.captured.emit()
        self.__set_btn_capture_text()

    def __set_btn_capture_text(self):
        timer_active = DetectorConfig.instance().get_timer().isActive()
        self.ui.btnCapture.setText("CAPTURE" if not timer_active else "STOP")
        self.ui.btnChoosePicture.setEnabled(not timer_active)

    def inp_max_instances_changed(self):
        value = self.ui.inpMaxInstances.value()
        if value != self.__current_cfg["err_cfg"]["yolo_max_boxes"]:
            self.__current_cfg["err_cfg"]["yolo_max_boxes"] = value

    def sld_score_thresh_changed(self):
        value = self.ui.sldScoreThresh.value()
        self.ui.groupScoreThresh.setTitle(f"Score threshold: {value/100}")
        self.__current_cfg["err_cfg"]["yolo_score_threshold"] = value / 100

    def sld_iou_threshold_changed(self):
        value = self.ui.sldIoUThresh.value()
        self.ui.groupIoUThresh.setTitle(f"IoU threshold: {value/100}")
        self.__current_cfg["err_cfg"]["yolo_iou_threshold"] = value / 100

    def width_height_changed(self):
        height = self.ui.cbbHeight.currentData()
        width = self.ui.cbbWidth.currentData()
        self.__current_cfg["err_cfg"]["img_size"] = (width, height)
        self.__current_cfg["err_cfg"]["inp_shape"] = (height, width, 3)

    def chk_defect_detection_state_changed(self):
        checked = self.ui.chkDefectDetection.isChecked()
        self.__current_cfg["is_defect_enable"] = checked

    def btn_choose_model_clicked(self):
        url, _ = helpers.file_chooser_open_file(self,
                                                f_filter="Keras model (*.h5)")
        if url.isEmpty(): return
        file_name = url.toLocalFile()
        self.ui.inpModelChoice.setText(file_name)
        self.__current_cfg["err_cfg"]["weights"] = file_name

    @asyncSlot()
    async def btn_choose_picture_clicked(self):
        url, _ = helpers.file_chooser_open_file(
            self, f_filter="Images (*.jpg *.png *.bmp)")
        if url.isEmpty(): return
        file_name = url.toLocalFile()
        images = [cv2.imread(file_name)]
        await self.__detect_error_on_picture(images)

    def btn_choose_classes_clicked(self):
        url, _ = helpers.file_chooser_open_file(self, "Text file (*.txt)")
        if url.isEmpty(): return
        file_name = url.toLocalFile()
        classes = []
        with open(file_name) as txt_file:
            classes = txt_file.readlines()
        self.__current_cfg["err_cfg"]["classes"] = classes
        self.__current_cfg["err_cfg"]["num_classes"] = len(classes)
        self.ui.inpClasses.setText(", ".join(classes))

    def view_cam(self, image):
        # read image in BGR format
        label_w = self.image1.width()
        label_h = self.image1.height()
        dim = (label_w, label_h)
        if image is None:
            self.image1.imshow(image)
            self.image2.imshow(image)
            self.image3.imshow(image)
            return
        orig = cv2.resize(image, dim)
        self.image1.imshow(orig)
        contour = self.__process_image(image)
        contour = cv2.resize(contour, dim)
        self.image2.imshow(contour)

    async def __detect_error(self, images):
        manager = DetectorConfig.instance().get_manager()
        # test only
        file_name = np.random.randint(151, 200)
        if len(images) == 2:
            images[0] = cv2.imread(
                f"./resources/test_data/{file_name}.jpg"
            )

        err_task = manager.detect_errors(self.__current_cfg, images, None)
        boxes, scores, classes, valid_detections = await err_task
        err_cfg = self.__current_cfg["err_cfg"]
        helper.draw_yolo_results(images,
                                 boxes,
                                 scores,
                                 classes,
                                 err_cfg["classes"],
                                 err_cfg["img_size"],
                                 min_score=err_cfg["yolo_score_threshold"])

        label_w = self.image3.width()
        label_h = self.image3.height()
        for idx, img in enumerate(images):
            images[idx] *= 255.
            images[idx] = np.asarray(images[idx], np.uint8)
        final_img = helpers.concat_images(images, label_w, label_h)
        self.image3.imshow(final_img)

    async def __detect_error_on_picture(self, images):
        manager = DetectorConfig.instance().get_manager()
        err_task = manager.detect_errors(self.__current_cfg, images, None)
        boxes, scores, classes, valid_detections = await err_task
        err_cfg = self.__current_cfg["err_cfg"]
        helper.draw_yolo_results(images,
                                 boxes,
                                 scores,
                                 classes,
                                 err_cfg["classes"],
                                 err_cfg["img_size"],
                                 min_score=err_cfg["yolo_score_threshold"])
        label_w = self.image3.width()
        label_h = self.image3.height()
        for idx, img in enumerate(images):
            images[idx] *= 255.
            images[idx] = np.asarray(images[idx], np.uint8)
        final_img = helpers.concat_images(images, label_w, label_h)
        self.image3.imshow(final_img)

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
            return image, [left, right]
        return image, None

    def __process_image(self, image):
        manager = DetectorConfig.instance().get_manager()
        contour, detected_pair = self.__process_pair(image)
        if detected_pair is not None and manager.get_model() is not None:
            runnable = WorkerRunnable(self.__detect_error,
                                      detected_pair,
                                      parent=self)
            runnable.work_error.connect(lambda ex: print(ex))
            QThreadPool.globalInstance().start(runnable)
        return contour