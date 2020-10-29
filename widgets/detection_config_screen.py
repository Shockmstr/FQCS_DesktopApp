from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import numpy as np
from views.detection_config_screen import Ui_DetectionConfigScreen
from widgets.image_widget import ImageWidget
from FQCS import detector, helper
from models.detector_config import DetectorConfigSingleton, DetectorConfig
from cv2 import cv2
from app.helpers import *


class DetectionConfigScreen(QWidget):
    BRIGHTNESS_STEP = 0.1
    CONTRAST_STEP = 5
    THRESHOLD1_STEP = 5
    THRESHOLD2_STEP = 5
    CAMERA_LOADED = False

    def __init__(self, backscreen: (), nextscreen: (), main_window):
        QWidget.__init__(self)
        self.ui = Ui_DetectionConfigScreen()
        self.detector_cfg = DetectorConfigSingleton.get_instance().config
        # hacks waiting for TODO: add more default props to detector.default_detector_config
        self.detector_cfg["d_cfg"] = dict(detector.default_thresh_config(),
                                          **detector.default_range_config(),
                                          **detector.default_edge_config())
        self.ui.setupUi(self)
        self.init_ui_values()
        self.main_window = main_window
        self.binding(backscreen=backscreen, nextscreen=nextscreen)
        self.load_cfg()

    #init ui values
    def init_ui_values(self):
        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbCamera.setPlaceholderText("Choose Cam")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)
        self.ui.cbbCamera.setCurrentIndex(-1)

        cam_array = get_all_camera_index(self)
        self.ui.cbbCamera.clear()
        for camera in cam_array:
            self.ui.cbbCamera.addItem("Camera " + str(camera), userData=camera)

        frame_resize_values = [
            "160", "240", "320", "400", "480", "660", "720", "800", "880",
            "960", "1040", "1120", "1200", "1280"
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

    #BINDING
    def binding(self, backscreen: (), nextscreen: ()):

        self.ui.sldBrightness.valueChanged.connect(
            self.brightness_value_change)
        self.ui.sldContrast.valueChanged.connect(self.contrast_value_change)
        self.ui.sldThreshold1.valueChanged.connect(
            self.threshold1_value_change)
        self.ui.sldThreshold2.valueChanged.connect(
            self.threshold2_value_change)
        self.ui.sldBlur.valueChanged.connect(self.blur_value_change)
        self.ui.sldDilate.valueChanged.connect(self.dilate_value_change)
        self.ui.sldErode.valueChanged.connect(self.erode_value_change)
        self.ui.sldBkgThresh.valueChanged.connect(self.bkg_value_change)
        self.ui.sldLightAdj.valueChanged.connect(self.light_adj_value_change)
        self.ui.sldLightAdjRange.valueChanged.connect(
            self.light_adj_range_value_change)
        self.ui.cbbCamera.currentIndexChanged.connect(self.cbbCamera_chose)
        self.ui.btnColorFrom.clicked.connect(self.button_color_from_clicked)
        self.ui.btnColorTo.clicked.connect(self.button_color_to_clicked)
        self.ui.cbbHeight.currentIndexChanged.connect(self.cbbHeight_changed)
        self.ui.cbbWidth.currentIndexChanged.connect(self.cbbWidth_changed)
        self.ui.cbbMethod.currentIndexChanged.connect(self.cbbMethod_changed)
        self.ui.btnNext.clicked.connect(nextscreen)
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnCapture.clicked.connect(self.button_capture_clicked)

    #HANDLERS
    #edge detection method
    def brightness_value_change(self):
        value = round(self.ui.sldBrightness.value() * self.BRIGHTNESS_STEP, 1)
        self.detector_cfg["d_cfg"]["alpha"] = value
        self.ui.grpboxSldBrightness.setTitle("Brightness: " + str(value))

    def contrast_value_change(self):
        value = self.ui.sldContrast.value() * self.CONTRAST_STEP
        self.detector_cfg["d_cfg"]["beta"] = value
        self.ui.grbboxSldContrast.setTitle("Contrast: " + str(value))

    def threshold1_value_change(self):
        value = self.ui.sldThreshold1.value() * self.THRESHOLD1_STEP
        self.detector_cfg["d_cfg"]["threshold1"] = value
        self.ui.grbboxSldThreshold.setTitle("Threshold 1: " + str(value))

    def threshold2_value_change(self):
        value = self.ui.sldThreshold2.value() * self.THRESHOLD2_STEP
        self.detector_cfg["d_cfg"]["threshold2"] = value
        self.ui.grbboxSldThreshold2.setTitle("Threshold 2: " + str(value))

    def blur_value_change(self):
        value = self.ui.sldBlur.value()
        self.detector_cfg["d_cfg"]["kernel"] = (2 * value + 1, 2 * value + 1)
        self.ui.grpboxSldBlur.setTitle("Blur: " + str(value))

    def dilate_value_change(self):
        value = self.ui.sldDilate.value()
        self.detector_cfg["d_cfg"]["d_kernel"] = np.ones((value, value))
        self.ui.grbboxSldDilate.setTitle("Dilate: " + str(value))

    def erode_value_change(self):
        value = self.ui.sldErode.value()
        self.detector_cfg["d_cfg"]["e_kernel"] = np.ones((value, value))
        self.ui.grbboxSldErode.setTitle("Erode: " + str(value))

    #threshold detection method
    def bkg_value_change(self):
        value = self.ui.sldBkgThresh.value()
        self.detector_cfg["d_cfg"]["bg_thresh"] = value
        self.ui.grpboxBkgThreshold.setTitle("Background Threshold: " +
                                            str(value))

    def light_adj_value_change(self):
        value = self.ui.sldLightAdj.value()
        self.detector_cfg["d_cfg"]["light_adj_thresh"] = value
        self.ui.grpboxLightAdj.setTitle("Light Adjustment: " + str(value))

    #range detection method
    def light_adj_range_value_change(self):
        value = self.ui.sldLightAdjRange.value()
        self.detector_cfg["d_cfg"]["light_adj_thresh"] = value
        self.ui.grpboxLightAdjRange.setTitle(f"Light Adjustment: {value}")

    def button_color_from_clicked(self):
        hsv = self.detector_cfg["d_cfg"]["cr_from"]
        init_hsv = QColor.fromHsv(hsv[0] * 2, hsv[1], hsv[2], 255)
        color = QColorDialog.getColor(parent=self, initial=init_hsv)
        if color.isValid():
            hsv = color.getHsv()
            hsv = (hsv[0] / 2, hsv[1], hsv[2])
            self.detector_cfg["d_cfg"]["cr_from"] = hsv
            color_hex = color.name()
            self.ui.btnColorFrom.setStyleSheet("background-color: " +
                                               color_hex)

    def button_color_to_clicked(self):
        hsv = self.detector_cfg["d_cfg"]["cr_to"]
        init_hsv = QColor.fromHsv(hsv[0] * 2, hsv[1], hsv[2], 255)
        color = QColorDialog.getColor(parent=self, initial=init_hsv)
        if color.isValid():
            hsv = color.getHsv()
            hsv = (hsv[0] / 2, hsv[1], hsv[2])
            self.detector_cfg["d_cfg"]["cr_to"] = hsv
            color_hex = color.name()
            self.ui.btnColorTo.setStyleSheet("background-color: " + color_hex)

    #main controls
    def cbbCamera_chose(self):
        # self.replace_camera_widget()
        index = self.ui.cbbCamera.currentData()
        self.main_window.video_camera.open(index)

    def cbbMethod_changed(self, index: int):
        method = self.ui.cbbMethod.currentData()
        # hacks waiting for TODO: add more props to default d_cfg
        method_cfg = {
            "edge": detector.default_edge_config(),
            "thresh": detector.default_thresh_config(),
            "range": detector.default_range_config()
        }
        self.detector_cfg["detect_method"] = method
        self.detector_cfg["d_cfg"] = method_cfg.get(method)
        self.ui.stackContainerMid.setCurrentIndex(index)

    def cbbHeight_changed(self):
        value = self.ui.cbbHeight.currentData()
        self.detector_cfg["frame_height"] = value

    def cbbWidth_changed(self):
        value = self.ui.cbbWidth.currentData()
        self.detector_cfg["frame_width"] = value

    def button_capture_clicked(self):
        self.camera.release()

    # view camera
    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        contour, proc = self.process_contours(self.img.copy())
        img_resized = cv2.resize(self.img, self.dim)
        contour_resized = cv2.resize(contour, self.dim)
        proc_resized = cv2.resize(proc, self.dim)
        self.image1.imshow(img_resized)
        self.image2.imshow(contour_resized)
        self.image3.imshow(proc_resized)

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
            self.imageLayout.replaceWidget(self.ui.screen3, self.image3)
            self.CAMERA_LOADED = True

    def process_contours(self, image):
        frame_width, frame_height = self.detector_cfg[
            "frame_width"], self.detector_cfg["frame_height"]
        min_width, min_height = self.detector_cfg[
            "min_width_per"], self.detector_cfg["min_height_per"]
        min_width, min_height = frame_width * min_width, frame_height * min_height
        find_contours_func = detector.get_find_contours_func_by_method(
            self.detector_cfg["detect_method"])

        # adjust thresh
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
        return image, proc

    #load init configs
    def load_cfg(self):
        #edge
        brightness = self.detector_cfg["d_cfg"]["alpha"]
        contrast = self.detector_cfg["d_cfg"]["beta"]
        thresh1 = self.detector_cfg["d_cfg"]["threshold1"]
        thresh2 = self.detector_cfg["d_cfg"]["threshold2"]
        blur = self.detector_cfg["d_cfg"]["kernel"][0]
        dilate = self.detector_cfg["d_cfg"]["d_kernel"].shape[1]
        erode = self.detector_cfg["d_cfg"]["e_kernel"] and self.detector_cfg["d_cfg"]["e_kernel"].shape[1]
        #threshold
        bkg = self.detector_cfg["d_cfg"]["bg_thresh"]
        light_thresh = self.detector_cfg["d_cfg"]["light_adj_thresh"]
        #range
        light_range = self.detector_cfg["d_cfg"]["light_adj_thresh"]
        color_to = self.detector_cfg["d_cfg"]["cr_to"]
        color_from = self.detector_cfg["d_cfg"]["cr_from"]
        #main controls
        method = self.detector_cfg["detect_method"]
        height = self.detector_cfg["frame_height"]
        width = self.detector_cfg["frame_height"]

        self.ui.sldBrightness.setValue(brightness)
        self.ui.sldContrast.setValue(contrast)
        self.ui.sldThreshold1.setValue(thresh1)
        self.ui.sldThreshold2.setValue(thresh2)
        self.ui.sldBlur.setValue(blur)
        self.ui.sldDilate.setValue(dilate)
        self.ui.sldErode.setValue(erode or 0)

        self.ui.sldBkgThresh.setValue(bkg)
        self.ui.sldLightAdj.setValue(light_thresh)

        self.ui.sldLightAdjRange.setValue(light_range)
        hsv_from = self.detector_cfg["d_cfg"]["cr_from"]
        init_hsv_from = QColor.fromHsv(hsv_from[0] * 2, hsv_from[1],
                                       hsv_from[2], 255)
        self.ui.btnColorFrom.setStyleSheet("background-color: " +
                                           init_hsv_from.name())
        hsv_to = self.detector_cfg["d_cfg"]["cr_to"]
        init_hsv_to = QColor.fromHsv(hsv_from[0] * 2, hsv_from[1], hsv_from[2],
                                     255)
        self.ui.btnColorFrom.setStyleSheet("background-color: " +
                                           init_hsv_to.name())
        
        method_index = self.ui.cbbMethod.findData(method)
        self.ui.cbbMethod.setCurrentIndex(method_index)
        height_index = self.ui.cbbHeight.findData(height)
        self.ui.cbbHeight.setCurrentIndex(height_index)
        width_index = self.ui.cbbWidth.findData(width)
        self.ui.cbbWidth.setCurrentIndex(width_index)


