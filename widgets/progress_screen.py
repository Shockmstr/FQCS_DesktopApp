from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QThreadPool
import trio
from app_models.detector_config import DetectorConfig
from FQCS import helper
import os
from FQCS import detector
from views.progress_screen import Ui_ProgressScreen
from widgets.image_widget import ImageWidget
from cv2 import cv2
import numpy as np
from services.worker_runnable import WorkerRunnable



class ProgressScreen(QWidget):
    CAMERA_LOADED = False
    stopped = Signal()
    captured = Signal()
    returned_home = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ProgressScreen()
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui.setupUi(self)
        self.binding()
        self.returned_home = self.ui.btnReturnHome.clicked
        self.load_cfg()
        if not self.CAMERA_LOADED:
            self.ui.containerConfig.setEnabled(False)


    # data binding
    def binding(self):
        self.ui.btnCapture.clicked.connect(self.cam_control)

    def cam_control(self):
        if self.CAMERA_LOADED == True:
            self.ui.btnCapture.setText("CAPTURE")
            self.stopped.emit()
            self.CAMERA_LOADED = False
        elif self.CAMERA_LOADED == False:
            self.ui.btnCapture.setText("STOP")
            self.captured.emit()
            self.CAMERA_LOADED = True

    def view_cam(self, image):
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        img_resized = cv2.resize(self.img, self.dim)
        self.image1.imshow(img_resized)
        trio.run(self.process_image, self.img)

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
            self.ui.btnCapture.setText("STOP")
            self.CAMERA_LOADED = True
            self.ui.containerConfig.setEnabled(True)

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
            max_width = max((left.shape[0], right.shape[0]))
            return image, [left, right], (check_group_idx, sizes), ()

        return image, None, None, None

    async def process_image(self, image):
        manager = DetectorConfig.instance().manager
        main_cfg = manager.get_main_config()
        contour, detected_pair, size_params, sim_params = self.__process_pair(image)

        if detected_pair is not None:
            left, right = detected_pair
            has_color_checked, has_error_checked = False, False

            # size compare
            check_group_idx, sizes = size_params
            check_size = sizes[check_group_idx]
            h_diff, w_diff = manager.compare_size(main_cfg, check_size)
            if h_diff or w_diff:
                pass

            # similarity compare
            if os.path.exists(manager.get_sample_left()):
                sim_cfg = main_cfg["sim_cfg"]
                pre_left, pre_right, pre_sample_left, pre_sample_right = manager.preprocess_images(
                    main_cfg, left, right)
                images = [left, right]
                left_asym_task, right_asym_task = manager.detect_asym(
                    main_cfg, pre_left, pre_right, pre_sample_left,
                    pre_sample_right)
                is_asym_diff_left, avg_asym_left, avg_amp_left, recalc_left, res_list_l, amp_res_list_l = await left_asym_task
                is_asym_diff_right, avg_asym_right, avg_amp_right, recalc_right, res_list_r, amp_res_list_r = await right_asym_task
                has_asym = is_asym_diff_left or is_asym_diff_right
                if has_asym:
                    if main_cfg["is_color_enable"]:
                        has_color_checked = True
                        left_color_task, right_color_task = manager.compare_colors(
                            main_cfg, pre_left, pre_right, pre_sample_left,
                            pre_sample_right)
                        left_color_results = await left_color_task
                        right_color_results = await right_color_task
                    if main_cfg["is_defect_enable"]:
                        has_error_checked = True
                        err_task = manager.detect_errors(main_cfg, images)
                        boxes, scores, classes, valid_detections = await err_task

            # error detect
            if manager.get_model() is not None:
                runnable = WorkerRunnable(self.show_error,
                                        detected_pair,
                                        parent=self)
                runnable.work_error.connect(lambda ex: print(ex))
                QThreadPool.globalInstance().start(runnable)


            

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
        images[0] = np.asarray(images[0], np.uint8)
        images[0] = np.asarray(images[0], np.uint8)
        self.image3.imshow(images[0])

    def load_cfg(self):
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        if self.detector_cfg is None: return