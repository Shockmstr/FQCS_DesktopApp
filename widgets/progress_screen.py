from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
import trio
from app_models.detector_config import DetectorConfig
from FQCS import helper
from FQCS.tf2_yolov4 import helper as y_helper
import os
from FQCS import detector

from views.progress_screen import Ui_ProgressScreen
from widgets.image_widget import ImageWidget
from cv2 import cv2
import numpy as np


class ProgressScreen(QWidget):
    CAMERA_LOADED = False
    finished = Signal(bool)
    stopped = Signal()
    captured = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ProgressScreen()
        self.detector_cfg = DetectorConfig.instance().config
        self.ui.setupUi(self)
        self.binding()

    # data binding
    def binding(self):
        self.ui.btnCapture.clicked.connect(self.cam_control)
        self.ui.btnStop.clicked.connect(self.btn_finished_clicked)

    def cam_control(self):
        if self.CAMERA_LOADED == True:
            self.ui.btnCapture.setText("STOP")
            self.captured.emit()
            self.CAMERA_LOADED = False
        elif self.CAMERA_LOADED == False:
            self.ui.btnCapture.setText("CAPTURE")
            self.stopped.emit()
            self.CAMERA_LOADED = True

    def view_cam(self, image):
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        img_resized = cv2.resize(self.img, self.dim)
        self.image1.imshow(img_resized)

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.ui.btnCapture.setText("STOP")
            self.CAMERA_LOADED = True

    async def final_process(self):
        sample_left_path = "/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/sample_left.jpg"
        sample_right_path = "/Users/bitumhoang/Desktop/capstone/FQCS_DesktopApp/sample_right.jpg"

        err_cfg = self.detector_cfg["err_cfg"]
        model = detector.get_yolov4_model(
            inp_shape=err_cfg["inp_shape"],
            num_classes=err_cfg["num_classes"],
            training=False,
            yolo_max_boxes=err_cfg["yolo_max_boxes"],
            yolo_iou_threshold=err_cfg["yolo_iou_threshold"],
            weights=err_cfg["weights"],
            yolo_score_threshold=err_cfg["yolo_score_threshold"])

        uri = "/Users/bitumhoang/Desktop/capstone/FQCS-Research/FQCS.ColorDetection/FQCS_detector/test.mp4"
        cap = cv2.VideoCapture(uri)
        frame_width, frame_height = self.detector_cfg[
            "frame_width"], self.detector_cfg["frame_height"]
        min_width, min_height = self.detector_cfg[
            "min_width_per"], self.detector_cfg["min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height
        # cap.set(cv2.CAP_PROP_POS_FRAMES, 1100)

        sample_left, sample_right = None, None
        if os.path.exists(sample_left_path):
            sample_left = cv2.imread(sample_left_path)
            sample_right = cv2.imread(sample_right_path)

        model = await model
        try:
            # activate
            await detector.detect_errors(model,
                                         [np.zeros(err_cfg["inp_shape"])],
                                         err_cfg["img_size"])
        finally:
            print("Activated")

        found = False
        while not found:
            _, image = cap.read()
            image = cv2.resize(image, (frame_width, frame_height))

            # output
            cv2.imshow("Original", image)

            find_contours_func = detector.get_find_contours_func_by_method(
                self.detector_cfg["detect_method"])
            d_cfg = self.detector_cfg['d_cfg']

            # adjust thresh
            if (self.detector_cfg["detect_method"] == "thresh"):
                adj_bg_thresh = helper.adjust_thresh_by_brightness(
                    image, d_cfg["light_adj_thresh"], d_cfg["bg_thresh"])
                d_cfg["adj_bg_thresh"] = adj_bg_thresh
            elif (self.detector_cfg["detect_method"] == "range"):
                adj_cr_to = helper.adjust_crange_by_brightness(
                    image, d_cfg["light_adj_thresh"], d_cfg["cr_to"])
                d_cfg["adj_cr_to"] = adj_cr_to

            boxes, cnts, proc = detector.find_contours_and_box(
                image,
                find_contours_func,
                d_cfg,
                min_width=min_width,
                min_height=min_height)
            pair, image, split_left, split_right, boxes = detector.detect_pair_and_size(
                image,
                find_contours_func,
                d_cfg,
                boxes,
                cnts,
                stop_condition=self.detector_cfg['stop_condition'],
                detect_range=self.detector_cfg['detect_range'])

            # output
            unit = self.detector_cfg["length_unit"]
            per_10px = self.detector_cfg["length_per_10px"]
            sizes = []
            for b in boxes:
                rect, dimA, dimB, box, tl, tr, br, bl = b
                lH, lW = helper.calculate_length(
                    dimA, per_10px), helper.calculate_length(dimB, per_10px)
                sizes.append((lH, lW))
                cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0),
                                 2)
                cv2.putText(image, f"{lW:.1f} {unit}", (tl[0], tl[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 0), 2)
                cv2.putText(image, f"{lH:.1f} {unit}", (br[0], br[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 0), 2)
            cv2.imshow("Processed", image)
            cv2.imshow("Contours processed", proc)
            # cv2.waitKey(1)
            cv2.waitKey(0)

            if (pair is not None):
                found = True
                left, right = pair
                left, right = left[0], right[0]
                h_diff, w_diff = detector.compare_size(sizes[0], sizes[1],
                                                       self.detector_cfg)

                if split_left is not None:
                    # output
                    plt.imshow(split_left)
                    plt.show()
                    plt.imshow(split_right)
                    plt.show()

                # output
                fig, axs = plt.subplots(1, 2)
                axs[0].imshow(left)
                axs[0].set_title("Left detect")
                axs[1].imshow(right)
                axs[1].set_title("Right detect")
                if h_diff or w_diff:
                    plt.title("Right detect: Different size")
                plt.show()

                left = cv2.flip(left, 1)
                if not os.path.exists(sample_left_path):
                    cv2.imwrite(sample_left_path, left)
                    cv2.imwrite(sample_right_path, right)
                else:
                    images = [left, right]
                    err_task = detector.detect_errors(model, images,
                                                      err_cfg["img_size"])

                    # start
                    c_cfg = self.detector_cfg['color_cfg']
                    pre_sample_left = detector.preprocess_for_color_diff(
                        sample_left, c_cfg['img_size'], c_cfg['blur_val'],
                        c_cfg['alpha_l'], c_cfg['beta_l'], c_cfg['sat_adj'])
                    pre_sample_right = detector.preprocess_for_color_diff(
                        sample_right, c_cfg['img_size'], c_cfg['blur_val'],
                        c_cfg['alpha_r'], c_cfg['beta_r'], c_cfg['sat_adj'])
                    pre_left = detector.preprocess_for_color_diff(
                        left, c_cfg['img_size'], c_cfg['blur_val'],
                        c_cfg['alpha_l'], c_cfg['beta_l'], c_cfg['sat_adj'])
                    pre_right = detector.preprocess_for_color_diff(
                        right, c_cfg['img_size'], c_cfg['blur_val'],
                        c_cfg['alpha_r'], c_cfg['beta_r'], c_cfg['sat_adj'])

                    left_task, right_task = detector.detect_color_difference(
                        pre_left, pre_right, pre_sample_left, pre_sample_right,
                        c_cfg['amplify_thresh'], c_cfg['supp_thresh'],
                        c_cfg['amplify_rate'], c_cfg['max_diff'])

                    left_results = await left_task
                    right_results = await right_task
                    boxes, scores, classes, valid_detections = await err_task

                    # output
                    fig, axs = plt.subplots(1, 2)
                    axs[0].imshow(left)
                    axs[0].set_title("Left detect")
                    axs[1].imshow(sample_left)
                    axs[1].set_title("Left sample")
                    plt.show()
                    fig, axs = plt.subplots(1, 2)
                    axs[0].imshow(right)
                    axs[0].set_title("Right detect")
                    axs[1].imshow(sample_right)
                    axs[1].set_title("Right sample")
                    plt.show()

                    # output
                    fig, axs = plt.subplots(1, 2)
                    axs[0].imshow(pre_left)
                    axs[1].imshow(pre_sample_left)
                    plt.show()
                    fig, axs = plt.subplots(1, 2)
                    axs[0].imshow(pre_right)
                    axs[1].imshow(pre_sample_right)
                    plt.show()

                    # output
                    y_helper.draw_results(
                        images,
                        boxes,
                        scores,
                        classes,
                        err_cfg["classes"],
                        err_cfg["img_size"],
                        min_score=err_cfg["yolo_score_threshold"])

                    print("Left", left_results[1], left_results[2])
                    print("Right", right_results[1], right_results[2])
                    fig, axs = plt.subplots(1, 3)
                    if (left_results[3]):
                        plt.title("Different left")
                    axs[0].imshow(left)
                    axs[1].imshow(sample_left)
                    axs[2].imshow(images[0])
                    plt.show()
                    fig, axs = plt.subplots(1, 3)
                    if (right_results[3]):
                        plt.title("Different right")
                    axs[0].imshow(right)
                    axs[1].imshow(sample_right)
                    axs[2].imshow(images[1])
                    plt.show()

    def btn_finished_clicked(self, event: bool):
        if self.sender() == self.ui.btnStop:
            trio.run(self.final_process)
        self.finished.emit(event)
