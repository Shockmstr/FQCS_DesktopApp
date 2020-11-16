from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QThreadPool, QTimer
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
from app_constants import ISO_DATE_FORMAT
import datetime


class ProgressScreen(QWidget):
    return_home = Signal()
    __result_html_changed = Signal(str)
    __sample_left = None
    __sample_right = None
    __last_side_idx = 0
    __capturing = True

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__camera_timer = QTimer()
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        self.image1 = ImageWidget()
        self.side_result_image = ImageWidget()
        self.left_detected_image = ImageWidget()
        self.right_detected_image = ImageWidget()
        self.left_sample_image = ImageWidget()
        self.right_sample_image = ImageWidget()

        self.imageLayout = self.ui.screen1.parentWidget().layout()
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
        self.ui.screen1.deleteLater()

        self.mainCamLayout = self.ui.sectionMainResult.layout()
        self.mainCamLayout.replaceWidget(self.ui.detected_L,
                                         self.left_detected_image)
        self.mainCamLayout.replaceWidget(self.ui.detected_R,
                                         self.right_detected_image)
        self.mainCamLayout.replaceWidget(self.ui.sample_L,
                                         self.left_sample_image)
        self.mainCamLayout.replaceWidget(self.ui.sample_R,
                                         self.right_sample_image)
        self.ui.detected_L.deleteLater()
        self.ui.detected_R.deleteLater()
        self.ui.sample_L.deleteLater()
        self.ui.sample_R.deleteLater()

        self.sideCamLayout = self.ui.sectionSideResult.layout()
        self.sideCamLayout.replaceWidget(self.ui.lblSideResult,
                                         self.side_result_image)
        self.ui.lblSideResult.deleteLater()

    def showEvent(self, event):
        manager = DetectorConfig.instance().get_manager()
        main_idx, self.__main_cfg = manager.get_main_config()
        self.__capturing = True
        video_cameras = DetectorConfig.instance().get_video_cameras()
        configs = manager.get_configs()
        self.__main_cam = video_cameras[main_idx]
        for i, cfg in enumerate(configs):
            # video_cameras[i].open(cfg["camera_uri"])
            # test only
            video_cameras[i].open(
                r"N:\Workspace\Capstone\FQCS-Research\FQCS.ColorDetection\test1.mp4"
            )

        self.image1.imshow(None)
        self.left_detected_image.imshow(None)
        self.right_detected_image.imshow(None)
        self.side_result_image.imshow(None)
        self.ui.inpResult.setHtml("<b>RESULT</b>")
        self.__set_btn_capture_text()
        self.__view_image_sample()
        self.__load_config()
        self.__camera_timer.start(20)
        return

    def hideEvent(self, event):
        self.__release()

    def closeEvent(self, event):
        self.__release()

    def __release(self):
        self.__camera_timer.stop()
        manager = DetectorConfig.instance().get_manager()
        video_cameras = DetectorConfig.instance().get_video_cameras()
        configs = manager.get_configs()
        for i, cfg in enumerate(configs):
            video_cameras[i].release()

    def validate_show(self):
        manager = DetectorConfig.instance().get_manager()
        _, main_cfg = manager.get_main_config()
        if main_cfg is None: return "No main configuration available"
        has_model = manager.get_model() is not None
        configs = manager.get_configs()
        for cfg in configs:
            if cfg["is_defect_enable"] and not has_model:
                return "Defect detection enabled but no model founded"
        if manager.get_sample_left() is None or manager.get_sample_right(
        ) is None:
            return "Samples not found"
        return None

    # data binding
    def binding(self):
        self.return_home = self.ui.btnReturnHome.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        self.ui.cbbCamera.currentIndexChanged.connect(
            self.cbb_camera_current_index_changed)
        self.ui.cbbDisplayType.currentIndexChanged.connect(
            self.cbb_display_type_index_changed)
        self.__camera_timer.timeout.connect(self.camera_timer_timeout)
        self.__result_html_changed.connect(self.__handle_result_html_changed)

    def btn_capture_clicked(self):
        if self.__camera_timer.isActive():
            self.__capturing = False
            self.__camera_timer.stop()
        else:
            self.__capturing = True
            self.__camera_timer.start(20)
        self.__set_btn_capture_text()

    def cbb_camera_current_index_changed(self):
        cur_idx = self.ui.cbbCamera.currentIndex()
        if cur_idx != self.__last_side_idx:
            self.__last_side_idx = cur_idx
            self.side_result_image.imshow(None)

    def cbb_display_type_index_changed(self):
        self.__last_display_type = self.ui.cbbDisplayType.currentText()

    def __set_btn_capture_text(self):
        self.ui.btnCapture.setText(
            "CAPTURE" if not self.__capturing else "STOP")

    def camera_timer_timeout(self):
        manager = DetectorConfig.instance().get_manager()
        _, image = self.__main_cam.read()
        if image is None:
            # test only
            self.__main_cam.set(cv2.CAP_PROP_POS_FRAMES, 0)
            _, image = self.__main_cam.read()
            # self.image1.imshow(image)
            # return
        frame_width, frame_height = self.__main_cfg[
            "frame_width"], self.__main_cfg["frame_height"]
        image = cv2.resize(image, (frame_width, frame_height))
        trio.run(self.process_image, image)

    def __view_image_sample(self):
        manager = DetectorConfig.instance().get_manager()
        self.__sample_left = manager.get_sample_left()
        self.__sample_right = manager.get_sample_right()
        label_w, label_h = self.left_detected_image.width(
        ), self.left_detected_image.height()
        dim = (label_w, label_h)
        m_left = cv2.resize(self.__sample_left, dim)
        m_right = cv2.resize(self.__sample_right, dim)
        self.left_sample_image.imshow(m_left)
        self.right_sample_image.imshow(m_right)

    async def process_image(self, image):
        label_w = self.image1.width()
        label_h = self.image1.height()
        dim = (label_w, label_h)
        manager = DetectorConfig.instance().get_manager()
        idx, main_cfg = manager.get_main_config()
        if self.__last_display_type == "Original":
            resized_image = cv2.resize(image, dim)
            self.image1.imshow(resized_image)
        boxes, proc = manager.extract_boxes(main_cfg, image)
        final_grouped, sizes, check_group_idx, pair, split_left, split_right, image_detect = manager.detect_groups_and_checked_pair(
            main_cfg, boxes, image)

        if self.__last_display_type == "Detection":
            unit = main_cfg["length_unit"]
            for idx, group in enumerate(final_grouped):
                for b_idx, b in enumerate(group):
                    c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
                    cur_size = sizes[idx][b_idx]
                    lH, lW = cur_size
                    helper.draw_boxes_and_sizes(image, idx, box, lH, lW, unit,
                                                tl, br)
            resized_image = cv2.resize(image, dim)
            self.image1.imshow(resized_image)
        elif self.__last_display_type == "Contours":
            resized_image = cv2.resize(proc, dim)
            self.image1.imshow(resized_image)

        if (pair is not None):
            manager.check_group(check_group_idx, final_grouped)
            left, right = pair
            left, right = left[0], right[0]
            left = cv2.flip(left, 1)
            label_w = self.left_detected_image.width()
            label_h = self.left_detected_image.height()
            dim = (label_w, label_h)
            left_resized, right_resized = cv2.resize(left, dim), cv2.resize(
                right, dim)
            self.left_detected_image.imshow(left_resized)
            self.right_detected_image.imshow(right_resized)
            runnable = WorkerRunnable(self.__process_pair, parent=self)
            runnable.work_error.connect(lambda ex: print(ex))
            QThreadPool.globalInstance().start(runnable)

    async def __process_pair(self):
        # result display
        cur = datetime.datetime.now()
        cur_date_str = cur.strftime(ISO_DATE_FORMAT)
        result_text = f"<b>RESULT</b><br/>" + f"<b>Time</b>: {cur_date_str}<br/>"
        self.__result_html_changed.emit(result_text)
        return

    def __handle_result_html_changed(self, html):
        self.ui.inpResult.setHtml(html)

    def __load_config(self):
        manager = DetectorConfig.instance().get_manager()
        configs = manager.get_configs()
        self.ui.cbbCamera.clear()
        for cfg in configs:
            if not cfg["is_main"]:
                self.ui.cbbCamera.addItem(cfg["name"])
        self.__last_side_idx = 0
        self.ui.cbbCamera.setCurrentIndex(0)
        self.__last_display_type = "Original"
        self.ui.cbbDisplayType.setCurrentIndex(0)
        return