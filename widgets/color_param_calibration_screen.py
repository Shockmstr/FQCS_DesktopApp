from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer, Signal, Qt
from widgets.image_widget import ImageWidget
from app_models.detector_config import DetectorConfig
import cv2
from FQCS import detector, helper
import numpy as np
from views.color_param_calibration_screen import Ui_ColorParamCalibScreen


class ColorParamCalibrationScreen(QWidget):
    CAMERA_LOADED = False
    IMAGE_LOADED = False
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.detector_cfg = DetectorConfig.instance().config
        self.ui = Ui_ColorParamCalibScreen()
        self.ui.setupUi(self)
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.load_default_config()
        self.binding()

    # binding
    def binding(self):
        self.ui.cbbCamera.setPlaceholderText("Choose Cam")
        self.ui.cbbCamera.setCurrentIndex(-1)

        # create a timer
        self.timer = QTimer()
        # set timer timeout call back function

        self.timer.timeout.connect(self.view_cam)
        self.ui.cbbCamera.currentIndexChanged.connect(self.cbbCamera_chose)
        self.ui.inpSuppThreshold.textChanged.connect(self.sup_thresh_change)
        self.ui.sldAllowDiff.valueChanged.connect(self.allow_diff_change)
        self.ui.sldAmpRate.valueChanged.connect(self.amp_rate_change)
        self.ui.ampThreshBlue.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshGreen.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshRed.textChanged.connect(self.amp_threshold_change)

        self.ui.btnCapture.clicked.connect(self.find_amp_threshold)

    def amp_threshold_change(self):
        amp_thresh_green_value = float(self.ui.ampThreshGreen.text())
        amp_thresh_red_value = float(self.ui.ampThreshRed.text())
        amp_thresh_blue_value = float(self.ui.ampThreshBlue.text())
        self.detector_cfg["color_cfg"]["amplify_thresh"] = (
            amp_thresh_red_value, amp_thresh_green_value,
            amp_thresh_blue_value)

    def amp_rate_change(self):
        value = self.ui.sldAmpRate.value()
        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " + str(value))
        self.detector_cfg["color_cfg"]["amplify_rate"] = value

    def sup_thresh_change(self):
        value = self.ui.inpSuppThreshold.value()
        self.detector_cfg["color_cfg"]["supp_thresh"] = value

    def allow_diff_change(self):
        value = self.ui.sldAllowDiff.value() / 100
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference (%): " +
                                         str(value))
        self.detector_cfg["color_cfg"]["max_diff"] = value

    def cbbCamera_chose(self):
        self.replace_camera_widget()
        index = self.ui.cbbCamera.currentData()
        self.control_timer(index)

    def load_default_config(self):
        #print(self.detector_cfg)
        # amp_thresh_red_value = self.detector_cfg["color_cfg"]["amplify_thresh"][0]
        # amp_thresh_green_value = self.detector_cfg["color_cfg"]["amplify_thresh"][1]
        # amp_thresh_blue_value = self.detector_cfg["color_cfg"]["amplify_thresh"][2]
        amplify_rate = self.detector_cfg["color_cfg"]["amplify_rate"]
        supp_thresh = self.detector_cfg["color_cfg"]["supp_thresh"]
        max_diff = self.detector_cfg["color_cfg"]["max_diff"]

        self.ui.sldAllowDiff.setValue(max_diff * 100)
        self.ui.sldAmpRate.setValue(amplify_rate)
        self.ui.inpSuppThreshold.setValue(supp_thresh)
        self.ui.ampThreshBlue.setValue(0)  # self-created value
        self.ui.ampThreshGreen.setValue(0)  # self-created value
        self.ui.ampThreshRed.setValue(0)  # self-created value

        self.ui.grpSldAllowDiff.setTitle("Amplification Rate: " +
                                         str(max_diff))
        self.ui.grpSldAmpRate.setTitle("Allowed Difference (%): " +
                                       str(amplify_rate))

    def view_image_sample(self):
        left = cv2.imread("sample_left.jpg")
        right = cv2.imread("sample_right.jpg")
        m_left, m_right = self.preprocess_color(left, right)
        img_size = (128, self.label_h - 50)
        m_left = cv2.resize(m_left, img_size, interpolation=cv2.INTER_AREA)
        m_right = cv2.resize(m_right, img_size, interpolation=cv2.INTER_AREA)
        self.image_sample_left.imshow(m_left)
        self.image_sample_right.imshow(m_right)

    def view_image_detect(self, image_left, image_right):
        print(image_left, " + ", image_right)
        left = cv2.imread(image_left)
        right = cv2.imread(image_right)
        m_left, m_right = self.preprocess_color(left, right)
        img_size = (128, self.label_h - 50)
        m_left = cv2.resize(m_left, img_size, interpolation=cv2.INTER_AREA)
        m_right = cv2.resize(m_right, img_size, interpolation=cv2.INTER_AREA)
        self.image_detect_left.imshow(m_left)
        self.image_detect_right.imshow(m_right)
        return m_left, m_right

    def view_cam(self, image):
        # read image in BGR format
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        self.img = cv2.resize(self.img, self.dim)
        self.image1.imshow(self.img)

    def replace_image_widget(self):
        if not self.IMAGE_LOADED:
            self.image_detect_left = ImageWidget()
            self.image_detect_right = ImageWidget()
            self.image_sample_left = ImageWidget()
            self.image_sample_right = ImageWidget()
            self.label_w = self.ui.screen2.width()
            self.label_h = self.ui.screen2.height()

            self.screen2_layout = self.ui.screen2.layout()
            self.screen2_layout.replaceWidget(self.ui.screen2Left,
                                              self.image_detect_left)
            self.screen2_layout.replaceWidget(self.ui.screen2Right,
                                              self.image_detect_right)

            self.screen3_layout = self.ui.screen3.layout()
            self.screen3_layout.replaceWidget(self.ui.screen3Left,
                                              self.image_sample_left)
            self.screen3_layout.replaceWidget(self.ui.screen3Right,
                                              self.image_sample_right)

            self.image_detect_left.ui.lblImage.setAlignment(Qt.AlignCenter)
            self.image_detect_right.ui.lblImage.setAlignment(Qt.AlignCenter)
            self.image_sample_left.ui.lblImage.setAlignment(Qt.AlignCenter)
            self.image_sample_right.ui.lblImage.setAlignment(Qt.AlignCenter)
            self.IMAGE_LOADED = True

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)
            self.CAMERA_LOADED = True

    index = 1
    hist_bgr_list = []

    def find_amp_threshold(self):
        # index = 1
        # while(index < 3):
        image_left = ("app\example_img\d_left_" + str(self.index) + ".jpg")
        image_right = ("app\example_img\d_right_" + str(self.index) + ".jpg")
        img_left, img_right = self.view_image_detect(image_left, image_right)
        #print(index)
        self.index += 1
        self.hist_bgr_list.append(helper.get_hist_bgr(img_left))
        self.hist_bgr_list.append(helper.get_hist_bgr(img_right))
        if (self.index == 4):
            self.index = 1
            max_blue = 0
            max_green = 0
            max_red = 0
            for hist in self.hist_bgr_list:
                blue = np.max(hist[0])
                print("hist blue:", hist[0].reshape(1, -1))
                green = np.max(hist[1])
                print("hist green:", hist[1].reshape(1, -1))
                red = np.max(hist[2])
                print("hist red:", hist[2].reshape(1, -1))
                if (blue > max_blue): max_blue = blue
                if (green > max_green): max_green = green
                if (red > max_red): max_red = red
            amp_thresh = (int(max_red), int(max_green), int(max_blue))
            self.ui.ampThreshRed.setValue(amp_thresh[0])
            self.ui.ampThreshGreen.setValue(amp_thresh[1])
            self.ui.ampThreshBlue.setValue(amp_thresh[2])
            self.detector_cfg["color_cfg"]["amplify_thresh"] = amp_thresh
            self.hist_bgr_list.clear()

    def showEvent(self, event):
        self.replace_image_widget()
        self.view_image_sample()
        # temporary place here ---
        #self.find_amp_threshold()

    #image process function
    async def detect_color_different(self):
        left_task, right_task = detector.detect_color_difference(
            pre_left, pre_right, pre_sample_left, pre_sample_right,
            c_cfg['amplify_thresh'], c_cfg['supp_thresh'],
            c_cfg['amplify_rate'], c_cfg['max_diff'])

        left_results = await left_task
        right_results = await right_task

    def preprocess_color(self, sample_left, sample_right):
        c_cfg = self.detector_cfg['color_cfg']
        #print(c_cfg)
        pre_sample_left = detector.preprocess_for_color_diff(
            sample_left, c_cfg['img_size'], c_cfg['blur_val'],
            c_cfg['alpha_l'], c_cfg['beta_l'], c_cfg['sat_adj'])
        pre_sample_right = detector.preprocess_for_color_diff(
            sample_right, c_cfg['img_size'], c_cfg['blur_val'],
            c_cfg['alpha_r'], c_cfg['beta_r'], c_cfg['sat_adj'])
        return pre_sample_left, pre_sample_right
