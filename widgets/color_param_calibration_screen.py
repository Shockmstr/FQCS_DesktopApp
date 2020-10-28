from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from app.helpers import * 
from widgets.image_widget import ImageWidget
from cv2 import cv2
from views.color_param_calibration_screen import Ui_ColorParamCalibScreen


class ColorParamCalibrationScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_ColorParamCalibScreen()
        self.ui.setupUi(self)
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen: (), nextscreen: ()):
        self.ui.cbbCamera.setPlaceholderText("Choose Cam")
        self.ui.cbbCamera.setCurrentIndex(-1)
        cam_array = get_all_camera_index(self)       
        self.ui.cbbCamera.clear()
        for camera in cam_array:
            self.ui.cbbCamera.addItem("Camera " + str(camera), userData=camera)

        # create a timer
        self.timer = QTimer()
        # set timer timeout call back function

        self.timer.timeout.connect(self.view_cam)
        self.ui.cbbCamera.currentIndexChanged.connect(self.cbbCamera_chose)
        self.ui.sldSupThresh.valueChanged.connect(self.sup_thresh_change)
        self.ui.sldAllowDiff.valueChanged.connect(self.allow_diff_change)
        self.ui.sldAmpRate.valueChanged.connect(self.amp_rate_change)
        self.ui.ampThreshBlue.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshGreen.textChanged.connect(self.amp_threshold_change)
        self.ui.ampThreshRed.textChanged.connect(self.amp_threshold_change)

        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnNext.clicked.connect(nextscreen)

    def amp_threshold_change(self):
        amp_thresh_green_value = float(self.ui.ampThreshGreen.text())
        amp_thresh_red_value = float(self.ui.ampThreshRed.text())
        amp_thresh_blue_value = float(self.ui.ampThreshBlue.text())
        
    def amp_rate_change(self):
        amp_rate_value = self.ui.sldAmpRate.value()
        self.ui.grpSldAmpRate.setTitle("Amplification Rate: " + str(amp_rate_value))
        
    def sup_thresh_change(self):
        sup_thresh_value = self.ui.sldSupThresh.value()
        self.ui.grpSldSupThresh.setTitle("Supress Threshold: " + str(sup_thresh_value))
    
    def allow_diff_change(self):
        allow_diff_value = self.ui.sldAllowDiff.value()
        self.ui.grpSldAllowDiff.setTitle("Allowed Difference: " + str(allow_diff_value))

    def cbbCamera_chose(self):
        self.replace_camera_widget()
        index = self.ui.cbbCamera.currentData()
        self.control_timer(index) 

    def view_cam(self):
        # read image in BGR format       
        _, self.img = self.cap.read()
        self.dim = (self.label_w, self.label_h)
        self.img = cv2.resize(self.img, self.dim)
        self.image1.imshow(self.img)

    # start/stop timer
    def control_timer(self, index: int):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(index)
            # start timer
            self.timer.start(20)
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()

    def replace_camera_widget(self):
        self.image1 = ImageWidget()
        self.label_w = self.ui.screen1.width()
        self.label_h = self.ui.screen1.height()
        self.imageLayout = self.ui.screen1.parentWidget().layout()
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)