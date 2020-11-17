from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QThreadPool, QTimer
import trio
from app_models.detector_config import DetectorConfig
from app_models.app_config import AppConfig
from app_models.auth_info import AuthInfo
from app import helpers
from FQCS import helper
import os
from FQCS import detector, fqcs_constants, fqcs_api
from views.progress_screen import Ui_ProgressScreen
from widgets.image_widget import ImageWidget
from cv2 import cv2
import numpy as np
from services.worker_runnable import WorkerRunnable
from app_constants import ISO_DATE_FORMAT, FOLDER_DATE_FORMAT, Videos
import datetime
import uuid


class ProgressScreen(QWidget):
    return_home = Signal()
    __result_html_changed = Signal(str)
    __sample_left = None
    __sample_right = None
    __capturing = True

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__camera_timer = QTimer()
        self.__storage_path = AppConfig.instance().config["storage_path"]
        self.__api_url = AppConfig.instance().config["api_url"]
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
            video_cameras[i].open(Videos.instance().next())

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
            self.__main_cam.open(Videos.instance().next())
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
            self.__last_detect_time = datetime.datetime.now()
            runnable = WorkerRunnable(self.__process_pair,
                                      self.__last_detect_time,
                                      check_group_idx,
                                      final_grouped,
                                      sizes,
                                      pair,
                                      parent=self)
            runnable.work_error.connect(lambda ex: print(ex))
            QThreadPool.globalInstance().start(runnable)

    async def __process_pair(self, cur: datetime.datetime, check_group_idx,
                             final_grouped, sizes, pair):
        manager = DetectorConfig.instance().get_manager()
        manager.check_group(check_group_idx, final_grouped)
        check_size = sizes[check_group_idx]
        h_diff, w_diff = manager.compare_size(self.__main_cfg, check_size)

        # output
        left, right = pair
        left, right = left[0], right[0]
        left = cv2.flip(left, 1)
        pre_left, pre_right, pre_sample_left, pre_sample_right = manager.preprocess_images(
            self.__main_cfg, left, right)
        images = [left, right]
        side_images = []
        # Similarity compare
        sim_cfg = self.__main_cfg["sim_cfg"]
        left_result, right_result = await manager.detect_asym(
            self.__main_cfg, pre_left, pre_right, pre_sample_left,
            pre_sample_right, None)
        is_asym_diff_left, avg_asym_left, avg_amp_left, recalc_left, res_list_l, amp_res_list_l = left_result
        is_asym_diff_right, avg_asym_right, avg_amp_right, recalc_right, res_list_r, amp_res_list_r = right_result
        has_asym = is_asym_diff_left or is_asym_diff_right
        has_color_checked, has_error_checked = False, False
        result_dict = {}
        async with trio.open_nursery() as nursery:
            if has_asym:
                if self.__main_cfg["is_color_enable"]:
                    has_color_checked = True
                    nursery.start_soon(manager.compare_colors, self.__main_cfg,
                                       pre_left, pre_right, pre_sample_left,
                                       pre_sample_right, True,
                                       (result_dict, "color_results"))

                if self.__main_cfg["is_defect_enable"]:
                    has_error_checked = True
                    nursery.start_soon(manager.detect_errors, self.__main_cfg,
                                       images, (result_dict, "err_results"))

            video_cameras = DetectorConfig.instance().get_video_cameras()
            configs = manager.get_configs()
            for idx, cfg in enumerate(configs):
                if cfg["is_main"] == True: continue
                cfg_name = cfg["name"]
                nursery.start_soon(self.__activate_side_cam, cfg,
                                   video_cameras[idx], manager,
                                   (result_dict, f"side_result_{cfg_name}"))

        side_results = []
        for key in result_dict.keys():
            if key.startswith("side_result_"):
                result = result_dict[key]
                if result is not None:
                    side_results.append(result)

        # result display
        defect_types = set()
        size_result = "<span style='color:green'>PASSED</span>"
        left_asym_result = "<span style='color:green'>PASSED</span>"
        right_asym_result = "<span style='color:green'>PASSED</span>"
        if h_diff or w_diff:
            size_result = "<span style='color:red'>FAILED: Different size</span>"
            defect_types.add(fqcs_constants.SIZE_MISMATCH)
        if is_asym_diff_left:
            left_asym_result = "<span style='color:red'>FAILED: Different from sample</span>"
            defect_types.add(fqcs_constants.SAMPLE_MISMATCH)
        if is_asym_diff_right:
            right_asym_result = "<span style='color:red'>FAILED: Different from sample</span>"
            defect_types.add(fqcs_constants.SAMPLE_MISMATCH)
        # output
        defect_result = "<span style='color:green'>NOT ANY</span>"
        defects = {}
        err_cfg = self.__main_cfg["err_cfg"]
        min_score = err_cfg["yolo_score_threshold"]
        classes_labels = err_cfg["classes"]
        if has_error_checked:
            boxes, scores, classes, valid_detections = result_dict[
                "err_results"]
            helper.draw_yolo_results(images,
                                     boxes,
                                     scores,
                                     classes,
                                     classes_labels,
                                     err_cfg["img_size"],
                                     min_score=min_score)
            self.__parse_defects_detection_result(images, scores, classes,
                                                  classes_labels, min_score,
                                                  defects)
            if cur == self.__last_detect_time:
                label_w = self.left_detected_image.width()
                label_h = self.left_detected_image.height()
                dim = (label_w, label_h)
                left_img = cv2.resize(images[0], dim)
                right_img = cv2.resize(images[1], dim)
                self.left_detected_image.imshow(left_img)
                self.right_detected_image.imshow(right_img)

        label_w = self.side_result_image.width()
        label_h = self.side_result_image.height()
        for res in side_results:
            side_images, side_boxes, side_scores, side_classes, side_valid_detections = res
            self.__parse_defects_detection_result(side_images, side_scores,
                                                  side_classes, classes_labels,
                                                  min_score, defects)
            if cur == self.__last_detect_time:
                final_img = helpers.concat_images(side_images, label_w,
                                                  label_h)
                self.side_result_image.imshow(final_img)

        defect_result_text = []
        for key in defects.keys():
            defect_types.add(key)
            d_count = defects[key]
            defect_result_text.append(f"{key}: {d_count}")
        if len(defects) > 0:
            defect_result_text = ", ".join(defect_result_text)
            defect_result_text = f"<span style='color:red'>{defect_result_text}</span>"
            defect_result = defect_result_text

        # output
        if has_color_checked:
            left_color_result = "<span style='color:green'>PASSED</span>"
            right_color_result = "<span style='color:green'>PASSED</span>"
            left_c_results = result_dict["color_results"][0]
            right_c_results = result_dict["color_results"][1]
            if left_c_results[3]:
                left_color_result = "<span style='color:red'>FAILED: Different color</span>"
                defect_types.add(fqcs_constants.COLOR_MISMATCH)
            if right_c_results[3]:
                right_color_result = "<span style='color:red'>FAILED: Different color</span>"
                defect_types.add(fqcs_constants.COLOR_MISMATCH)

        cur_date_str = cur.strftime(ISO_DATE_FORMAT)
        result_text = f"<b>RESULT</b><br/>" + f"<b>Time</b>: {cur_date_str}<br/><hr/>"
        result_text += f"<b>Size</b>: {size_result}<br/><hr/>"
        result_text += f"<b>Similarity of left</b>: {left_asym_result}<br/>"
        result_text += f"<b>Similarity of right</b>: {right_asym_result}<br/><hr/>"
        if has_color_checked:
            result_text += f"<b>Color of left</b>: {left_color_result}<br/>"
            result_text += f"<b>Color of right</b>: {right_color_result}<br/><hr/>"
        result_text += f"<b>Defects</b>: {defect_result}<br/>"
        # test only
        result_text += f"{defect_types}"

        if cur == self.__last_detect_time:
            self.__result_html_changed.emit(result_text)

        # save images
        folder = cur.strftime(FOLDER_DATE_FORMAT)
        os.makedirs(os.path.join(self.__storage_path, folder), exist_ok=True)
        all_imgs = []
        all_imgs.extend(images)
        all_imgs.extend(side_images)
        images = []
        for img in all_imgs:
            img_name = str(uuid.uuid4()) + ".jpg"
            rel_path = os.path.join(folder, img_name)
            abs_path = os.path.join(self.__storage_path, rel_path)
            cv2.imwrite(abs_path, img)
            images.append(rel_path)

        # send to api
        access_token = AuthInfo.instance().get_token_info()["access_token"]
        headers = fqcs_api.get_common_headers(auth_token=access_token)
        is_success, resp = fqcs_api.submit_event(self.__api_url, defect_types,
                                                 images[0], images[1],
                                                 images[2:], headers)
        print(is_success, resp)
        return

    async def __activate_side_cam(self, cfg, cam, manager, result_info):
        # _, image = cam.read()
        # test only
        _, image = self.__main_cam.read()

        frame_width, frame_height = cfg["frame_width"], cfg["frame_height"]
        resized_image = cv2.resize(image, (frame_width, frame_height))
        boxes, proc = manager.extract_boxes(cfg, resized_image)
        image_detect = resized_image.copy()
        pair, image_detect, boxes = manager.detect_pair_side_cam(
            cfg, boxes, image_detect)
        result = None
        if (pair is not None and len(pair) > 0):
            images = [item[0] for item in pair]
            boxes, scores, classes, valid_detections = await manager.detect_errors(
                cfg, images, None)
            err_cfg = cfg["err_cfg"]
            helper.draw_yolo_results(images,
                                     boxes,
                                     scores,
                                     classes,
                                     err_cfg["classes"],
                                     err_cfg["img_size"],
                                     min_score=err_cfg["yolo_score_threshold"])
            result = (images, boxes, scores, classes, valid_detections)
        return helper.return_result(result, result_info)

    def __parse_defects_detection_result(self, images, scores, classes,
                                         classes_labels, min_score, defects):
        for i in range(len(images)):
            images[i] *= 255.
            images[i] = np.asarray(images[i], dtype=np.uint8)
            iscores = scores[i]
            iclasses = classes[i].astype(int)
            for score, cl in zip(iscores.tolist(), iclasses.tolist()):
                if score > min_score:
                    defect = classes_labels[cl]
                    if defect not in defects:
                        defects[defect] = 0
                    defects[defect] += 1

    def __handle_result_html_changed(self, html):
        self.ui.inpResult.setHtml(html)

    def __load_config(self):
        manager = DetectorConfig.instance().get_manager()
        configs = manager.get_configs()
        self.__last_display_type = "Original"
        self.ui.cbbDisplayType.setCurrentIndex(0)
        return