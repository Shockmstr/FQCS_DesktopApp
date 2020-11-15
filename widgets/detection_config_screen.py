from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QColorDialog, QHeaderView, QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox, QAction, QMenu
from PySide2.QtCore import Signal, Qt
import numpy as np
from views.detection_config_screen import Ui_DetectionConfigScreen
from widgets.dialogs.dialog_edit_name import DialogEditName
from widgets.image_widget import ImageWidget
from FQCS import detector, helper
from app_models.detector_config import DetectorConfig
from cv2 import cv2
from app import helpers


class DetectionConfigScreen(QWidget):
    BRIGHTNESS_STEP = 0.1
    CONTRAST_STEP = 5
    THRESHOLD1_STEP = 5
    THRESHOLD2_STEP = 5
    __last_selected_row = -1
    backscreen: Signal
    nextscreen: Signal
    captured = Signal()
    camera_changed = Signal(object)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.__cam_array = helpers.get_all_camera_index()
        self.__current_cfg = None
        self.ui = Ui_DetectionConfigScreen()
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
        self.imageLayout.replaceWidget(self.ui.screen3, self.image3)
        self.ui.screen1.deleteLater()
        self.ui.screen2.deleteLater()
        self.ui.screen3.deleteLater()

        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbCamera.setPlaceholderText("Choose Cam")

        self.ui.cbbCamera.clear()
        for camera in self.__cam_array:
            self.ui.cbbCamera.addItem("Camera " + str(camera), userData=camera)

        frame_resize_values = [
            "160", "240", "320", "400", "480", "560", "640", "720", "800",
            "880", "960", "1040", "1120", "1200", "1280"
        ]

        self.ui.cbbHeight.clear()
        for value in frame_resize_values:
            self.ui.cbbHeight.addItem(value, userData=int(value))

        self.ui.cbbWidth.clear()
        for value in frame_resize_values:
            self.ui.cbbWidth.addItem(value, userData=int(value))

        self.ui.cbbMethod.clear()
        self.ui.cbbMethod.addItem("Edge", userData="edge")
        self.ui.cbbMethod.addItem("Threshold", userData="thresh")
        self.ui.cbbMethod.addItem("Range", userData="range")

        table = self.ui.tblCameraConfig
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__reload_table()

        # create context menu
        self.tblPopMenu = QMenu(self)
        self.tblPopActionEditName = QAction('Edit name', self)
        self.tblPopActionRemove = QAction('Remove', self)
        self.tblPopMenu.addAction(self.tblPopActionEditName)
        self.tblPopMenu.addAction(self.tblPopActionRemove)

    def showEvent(self, event):
        _, self.__current_cfg = DetectorConfig.instance().get_current_cfg()
        if self.__current_cfg is None:
            self.__show_config_section(False)
            return
        self.__set_btn_capture_text()
        self.__load_config()

    def __reload_table(self):
        table = self.ui.tblCameraConfig
        table.clearContents()
        table.setRowCount(0)
        manager = DetectorConfig.instance().get_manager()
        cfgs = manager.get_configs()
        for cfg in cfgs:
            camera_name = cfg["name"]
            is_main = cfg["is_main"]
            if (is_main):
                self.__add_new_row(table, camera_name, "Main Camera")
            else:
                self.__add_new_row(table, camera_name, "")
        table.clearSelection()
        table.itemSelectionChanged.emit()
        self.__last_selected_row = -1
        self.image1.imshow(None)
        self.image2.imshow(None)
        self.image3.imshow(None)

    #BINDING
    def binding(self):
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.ui.btnCapture.clicked.connect(self.btn_capture_clicked)
        DetectorConfig.instance().manager_changed.connect(self.manager_changed)
        self.ui.sldBrightness.valueChanged.connect(
            self.sld_brightness_value_change)
        self.ui.sldContrast.valueChanged.connect(
            self.sld_contrast_value_change)
        self.ui.sldThreshold1.valueChanged.connect(
            self.sld_threshold1_value_change)
        self.ui.sldThreshold2.valueChanged.connect(
            self.sld_threshold2_value_change)
        self.ui.sldBlur.valueChanged.connect(self.sld_blur_value_change)
        self.ui.sldDilate.valueChanged.connect(self.dilate_value_change)
        self.ui.sldErode.valueChanged.connect(self.sld_erode_value_change)
        self.ui.sldBkgThresh.valueChanged.connect(self.sld_bkg_value_change)
        self.ui.sldLightAdj.valueChanged.connect(
            self.sld_light_adj_value_change)
        self.ui.sldLightAdjRange.valueChanged.connect(
            self.sld_light_adj_range_value_change)
        self.ui.cbbCamera.currentIndexChanged.connect(self.cbbCamera_changed)
        self.ui.btnColorFrom.clicked.connect(self.btn_color_from_clicked)
        self.ui.btnColorTo.clicked.connect(self.btn_color_to_clicked)
        self.ui.cbbHeight.currentIndexChanged.connect(self.cbbHeight_changed)
        self.ui.cbbWidth.currentIndexChanged.connect(self.cbbWidth_changed)
        self.ui.cbbMethod.currentIndexChanged.connect(self.cbbMethod_changed)
        self.ui.ckbInvertThresh.stateChanged.connect(
            self.chk_thresh_invert_state_change)
        self.ui.ckbInvertRange.stateChanged.connect(
            self.chk_range_invert_state_change)
        self.ui.tblCameraConfig.itemSelectionChanged.connect(
            self.tbl_camera_item_selection_changed)
        self.ui.tblCameraConfig.customContextMenuRequested.connect(
            self.table_context_menu)
        self.tblPopActionEditName.triggered.connect(
            self.table_action_edit_name_triggered)
        self.tblPopActionRemove.triggered.connect(
            self.table_action_remove_triggered)
        self.ui.btnAdd.clicked.connect(self.btn_add_clicked)

    #HANDLERS
    def btn_capture_clicked(self):
        self.captured.emit()
        self.__set_btn_capture_text()

    def __set_btn_capture_text(self):
        timer_active = DetectorConfig.instance().get_timer().isActive()
        self.ui.btnCapture.setText("CAPTURE" if not timer_active else "STOP")

    def manager_changed(self):
        self.__reload_table()

    def table_context_menu(self, point):
        self.tblPopMenu.exec_(self.ui.tblCameraConfig.mapToGlobal(point))

    def table_action_edit_name_triggered(self):
        table = self.ui.tblCameraConfig
        chosen_row = table.currentRow()
        detector_cfg = DetectorConfig.instance()
        camera_name = table.item(chosen_row, 0).text()
        dialog = DialogEditName(camera_name, parent=self)
        choice = dialog.exec_()
        if choice != QDialog.Accepted:
            return
        new_name = dialog.get_inp_edit_name().strip()
        err_text = detector_cfg.validate_config_name(new_name)
        if err_text is not None:
            helpers.show_message(err_text)
            return
        _, cfg = detector_cfg.get_current_cfg()
        cfg["name"] = new_name
        self.__reload_table()

    def table_action_remove_triggered(self, point):
        table = self.ui.tblCameraConfig
        chosen_row = table.currentRow()
        detector_cfg = DetectorConfig.instance()
        camera_name = table.item(chosen_row, 0).text()
        _, cfg = detector_cfg.get_manager().get_config_by_name(camera_name)
        detector_cfg.remove_config(cfg)
        self.__reload_table()

    #edge detection method
    def chk_thresh_invert_state_change(self):
        if self.ui.ckbInvertThresh.isChecked():
            self.__current_cfg["d_cfg"]["thresh_inv"] = True
        else:
            self.__current_cfg["d_cfg"]["thresh_inv"] = False

    def chk_range_invert_state_change(self):
        if self.ui.ckbInvertRange.isChecked():
            self.__current_cfg["d_cfg"]["color_inv"] = True
        else:
            self.__current_cfg["d_cfg"]["color_inv"] = False

    def sld_brightness_value_change(self):
        value = round(self.ui.sldBrightness.value() * self.BRIGHTNESS_STEP, 1)
        self.__current_cfg["d_cfg"]["alpha"] = value
        self.ui.grpboxSldBrightness.setTitle("Brightness: " + str(value))

    def sld_contrast_value_change(self):
        value = self.ui.sldContrast.value() * self.CONTRAST_STEP
        self.__current_cfg["d_cfg"]["beta"] = value
        self.ui.grbboxSldContrast.setTitle("Contrast: " + str(value))

    def sld_threshold1_value_change(self):
        value = self.ui.sldThreshold1.value() * self.THRESHOLD1_STEP
        self.__current_cfg["d_cfg"]["threshold1"] = value
        self.ui.grbboxSldThreshold.setTitle("Threshold 1: " + str(value))

    def sld_threshold2_value_change(self):
        value = self.ui.sldThreshold2.value() * self.THRESHOLD2_STEP
        self.__current_cfg["d_cfg"]["threshold2"] = value
        self.ui.grbboxSldThreshold2.setTitle("Threshold 2: " + str(value))

    def sld_blur_value_change(self):
        value = self.ui.sldBlur.value()
        self.__current_cfg["d_cfg"]["kernel"] = (2 * value + 1, 2 * value + 1)
        self.ui.grpboxSldBlur.setTitle("Blur: " + str(value))

    def dilate_value_change(self):
        value = self.ui.sldDilate.value()
        self.__current_cfg["d_cfg"]["d_kernel"] = np.ones((value, value))
        self.ui.grbboxSldDilate.setTitle("Dilate: " + str(value))

    def sld_erode_value_change(self):
        value = self.ui.sldErode.value()
        self.__current_cfg["d_cfg"]["e_kernel"] = np.ones((value, value))
        self.ui.grbboxSldErode.setTitle("Erode: " + str(value))

    #threshold detection method
    def sld_bkg_value_change(self):
        value = self.ui.sldBkgThresh.value()
        self.__current_cfg["d_cfg"]["bg_thresh"] = value
        self.ui.grpboxBkgThreshold.setTitle("Background Threshold: " +
                                            str(value))

    def sld_light_adj_value_change(self):
        value = self.ui.sldLightAdj.value()
        self.__current_cfg["d_cfg"]["light_adj_thresh"] = value
        self.ui.grpboxLightAdj.setTitle("Light Adjustment: " + str(value))

    #range detection method
    def sld_light_adj_range_value_change(self):
        value = self.ui.sldLightAdjRange.value()
        self.__current_cfg["d_cfg"]["light_adj_thresh"] = value
        self.ui.grpboxLightAdjRange.setTitle(f"Light Adjustment: {value}")

    def btn_color_from_clicked(self):
        # get initial color
        hsv = self.__current_cfg["d_cfg"]["cr_from"]
        h = 359 if (int(hsv[0] * 2) > 359) else int(hsv[0] * 2)
        s = int(hsv[1])
        v = int(hsv[2])
        init_hsv = QColor.fromHsv(h, s, v, a=255)

        color = QColorDialog.getColor(parent=self, initial=init_hsv)
        if color.isValid():
            hsv = color.getHsv()
            hsv = (hsv[0] / 2, hsv[1], hsv[2])
            self.__current_cfg["d_cfg"]["cr_from"] = hsv
            color_hex = color.name()
            self.ui.btnColorFrom.setStyleSheet("background-color: " +
                                               color_hex)

    def btn_color_to_clicked(self):
        #get initial color
        hsv = self.__current_cfg["d_cfg"]["cr_to"]
        h = 359 if (int(hsv[0] * 2) > 359) else int(hsv[0] * 2)
        s = int(hsv[1])
        v = int(hsv[2])
        init_hsv = QColor.fromHsv(h, s, v, a=255)

        color = QColorDialog.getColor(parent=self, initial=init_hsv)
        if color.isValid():
            hsv = color.getHsv()
            hsv = (hsv[0] / 2, hsv[1], hsv[2])
            self.__current_cfg["d_cfg"]["cr_to"] = hsv
            color_hex = color.name()
            self.ui.btnColorTo.setStyleSheet("background-color: " + color_hex)

    def btn_add_clicked(self):
        detector_cfg = DetectorConfig.instance()
        manager = detector_cfg.get_manager()
        table = self.ui.tblCameraConfig
        camera_name = self.ui.txtNewCamera.text().strip()
        err_text = detector_cfg.validate_config_name(camera_name)
        if err_text is not None:
            helpers.show_message(err_text)
            return
        new_cfg = detector.default_detector_config()
        new_cfg["name"] = camera_name
        detector_cfg.add_config(new_cfg)
        self.__add_new_row(table, camera_name, "")

    def tbl_camera_item_selection_changed(self):
        table = self.ui.tblCameraConfig
        chosen_row = table.currentRow()
        if chosen_row == self.__last_selected_row: return
        self.__last_selected_row = chosen_row
        detector_cfg = DetectorConfig.instance()
        if chosen_row != -1:
            camera_name = table.item(chosen_row, 0).text()
            detector_cfg.set_current_cfg_name(camera_name)
            _, self.__current_cfg = detector_cfg.get_current_cfg()
            self.__show_config_section(True)
            self.__load_config()
        else:
            detector_cfg.set_current_cfg_name(None)
            self.__show_config_section(False)
            self.camera_changed.emit(-1)

    def cbbCamera_changed(self):
        index = self.ui.cbbCamera.currentData()
        self.__current_cfg["camera_uri"] = index
        self.camera_changed.emit(index)

    def cbbMethod_changed(self, index: int):
        method = self.ui.cbbMethod.currentData()
        self.__current_cfg["detect_method"] = method
        self.ui.stackContainerMid.setCurrentIndex(index)

    def cbbHeight_changed(self):
        value = self.ui.cbbHeight.currentData()
        self.__current_cfg["frame_height"] = value

    def cbbWidth_changed(self):
        value = self.ui.cbbWidth.currentData()
        self.__current_cfg["frame_width"] = value

    # view camera
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
        contour, proc = self.__process_contours(image.copy())
        img_resized = cv2.resize(image, dim)
        contour_resized = cv2.resize(contour, dim)
        proc_resized = cv2.resize(proc, dim)
        self.image1.imshow(img_resized)
        self.image2.imshow(contour_resized)
        self.image3.imshow(proc_resized)

    def __process_contours(self, image):
        manager = DetectorConfig.instance().get_manager()
        boxes, proc = manager.extract_boxes(self.__current_cfg, image)
        for b in boxes:
            c, rect, dimA, dimB, box, tl, tr, br, bl, minx, maxx, cenx = b
            helper.draw_boxes(image, box)
        return image, proc

    def __show_config_section(self, shown):
        if shown:
            helpers.show_all_children(self.ui.containerMidRange)
            helpers.show_all_children(self.ui.containerMidEdge)
            helpers.show_all_children(self.ui.containerMidThresh)
            helpers.show_all_children(self.ui.containerLeft)
            self.ui.btnCapture.show()
            self.ui.btnNext.show()
        else:
            helpers.hide_all_children(self.ui.containerMidRange)
            helpers.hide_all_children(self.ui.containerMidEdge)
            helpers.hide_all_children(self.ui.containerMidThresh)
            helpers.hide_all_children(self.ui.containerLeft)
            self.ui.btnCapture.hide()
            self.ui.btnNext.hide()

    #load init configs
    def __load_config(self):
        #edge
        brightness = self.__current_cfg["d_cfg"]["alpha"]
        contrast = self.__current_cfg["d_cfg"]["beta"]
        thresh1 = self.__current_cfg["d_cfg"]["threshold1"]
        thresh2 = self.__current_cfg["d_cfg"]["threshold2"]
        blur = self.__current_cfg["d_cfg"]["kernel"][0]
        dilate = self.__current_cfg["d_cfg"]["d_kernel"].shape[1]
        erode = self.__current_cfg["d_cfg"]["e_kernel"] and self.__current_cfg[
            "d_cfg"]["e_kernel"].shape[1]
        #threshold
        bkg = self.__current_cfg["d_cfg"]["bg_thresh"]
        light_thresh = self.__current_cfg["d_cfg"]["light_adj_thresh"]
        #range
        light_range = self.__current_cfg["d_cfg"]["light_adj_thresh"]
        color_to = self.__current_cfg["d_cfg"]["cr_to"]
        color_from = self.__current_cfg["d_cfg"]["cr_from"]
        #main controls
        method_index = self.ui.cbbMethod.findData(
            self.__current_cfg["detect_method"])
        height_index = self.ui.cbbHeight.findData(
            self.__current_cfg["frame_height"])
        width_index = self.ui.cbbWidth.findData(
            self.__current_cfg["frame_width"])

        self.ui.sldBrightness.setValue(brightness / self.BRIGHTNESS_STEP)
        self.ui.sldContrast.setValue(contrast / self.CONTRAST_STEP)
        self.ui.sldThreshold1.setValue(thresh1 / self.THRESHOLD1_STEP)
        self.ui.sldThreshold2.setValue(thresh2 / self.THRESHOLD2_STEP)
        self.ui.sldBlur.setValue(blur)
        self.ui.sldDilate.setValue(dilate)
        self.ui.sldErode.setValue(erode or 0)

        self.ui.sldBkgThresh.setValue(bkg)
        self.ui.sldLightAdj.setValue(light_thresh)

        self.ui.sldLightAdjRange.setValue(light_range)
        hsv_from = self.__current_cfg["d_cfg"]["cr_from"]
        init_hsv_from = QColor.fromHsv(hsv_from[0] * 2, hsv_from[1],
                                       hsv_from[2], 255)
        self.ui.btnColorFrom.setStyleSheet("background-color: " +
                                           init_hsv_from.name())
        hsv_to = self.__current_cfg["d_cfg"]["cr_to"]
        init_hsv_to = QColor.fromHsv(hsv_from[0] * 2, hsv_from[1], hsv_from[2],
                                     255)
        self.ui.btnColorFrom.setStyleSheet("background-color: " +
                                           init_hsv_to.name())

        self.ui.cbbMethod.setCurrentIndex(method_index)
        self.ui.cbbHeight.setCurrentIndex(height_index)
        self.ui.cbbWidth.setCurrentIndex(width_index)

        camera_uri = self.__current_cfg["camera_uri"]
        if camera_uri is not None and camera_uri < self.ui.cbbCamera.count():
            self.ui.cbbCamera.setCurrentIndex(camera_uri)
            self.camera_changed.emit(camera_uri)
        else:
            self.ui.cbbCamera.setCurrentIndex(-1)

    def __add_new_row(self, table, camera_name, is_main):
        current_row = table.rowCount()
        table.insertRow(current_row)
        name_item = QTableWidgetItem(camera_name)
        is_main_item = QTableWidgetItem(is_main)
        table.setItem(current_row, 0, name_item)
        table.setItem(current_row, 1, is_main_item)
