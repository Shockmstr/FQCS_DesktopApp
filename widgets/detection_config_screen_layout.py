from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.detection_config_screen_layout import Ui_DetectionConfigScreen
from widgets.image_widget import ImageWidget
from cv2 import cv2
from app.helpers import *


class DetectionConfigScreen(QWidget):
    def __init__(self, nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_DetectionConfigScreen()
        self.ui.setupUi(self)
        self.binding(nextscreen=nextscreen)

    # binding
    def binding(self, nextscreen: ()):
        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbHeight.setPlaceholderText("Choose Cam")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)
        self.ui.cbbCamera.setCurrentIndex(-1)

        cam_array = get_all_camera_index(self)
        self.ui.cbbCamera.clear()
        for camera in cam_array:
            self.ui.cbbCamera.addItem("Camera " + str(camera), userData=camera)

        self.ui.cbbHeight.clear()
        self.ui.cbbHeight.addItem("900")
        self.ui.cbbHeight.addItem("1024")
        self.ui.cbbHeight.addItem("1158")

        self.ui.cbbWidth.clear()
        self.ui.cbbWidth.addItem("900")
        self.ui.cbbWidth.addItem("1024")
        self.ui.cbbWidth.addItem("1158")

        self.ui.cbbMethod.clear()
        self.ui.cbbMethod.addItem("Edge")
        self.ui.cbbMethod.addItem("Threshold")
        self.ui.cbbMethod.addItem("Range")

               
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        
        self.timer.timeout.connect(self.view_cam)

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

        self.ui.cbbMethod.activated[int].connect(
            self.ui.stackContainerMid.setCurrentIndex)
        self.bind_next_screen(nextscreen=nextscreen)

    #handler
    def brightness_value_change(self):
        value = self.ui.sldBrightness.value()
        self.ui.grpboxSldBrightness.setTitle("Brightness: " + str(value))

    def contrast_value_change(self):
        value = self.ui.sldContrast.value()
        self.ui.grbboxSldContrast.setTitle("Contrast: " + str(value))

    def threshold1_value_change(self):
        value = self.ui.sldThreshold1.value()
        self.ui.grbboxSldThreshold.setTitle("Threshold 1: " + str(value))

    def threshold2_value_change(self):
        value = self.ui.sldThreshold2.value()
        self.ui.grbboxSldThreshold2.setTitle("Threshold 2: " + str(value))

    def blur_value_change(self):
        value = self.ui.sldBlur.value()
        self.ui.grpboxSldBlur.setTitle("Blur: " + str(value))

    def dilate_value_change(self):
        value = self.ui.sldDilate.value()
        self.ui.grbboxSldDilate.setTitle("Dilate: " + str(value))

    def erode_value_change(self):
        value = self.ui.sldErode.value()
        self.ui.grbboxSldErode.setTitle("Erode: " + str(value))

    def bkg_value_change(self):
        value = self.ui.sldBkgThresh.value()
        self.ui.grpboxBkgThreshold.setTitle("Background Threshold: " +
                                            str(value))

    def light_adj_value_change(self):
        value = self.ui.sldLightAdj.value()
        self.ui.grpboxLightAdj.setTitle("Light Adjustment: " + str(value))

    def light_adj_range_value_change(self):
        value = self.ui.sldLightAdjRange.value()
        self.ui.grpboxLightAdjRange.setTitle("Light Adjustment: " + str(value))

    def bind_next_screen(self, nextscreen: ()):
        self.ui.btnNext.clicked.connect(nextscreen)   

    def cbbCamera_chose(self):
        index = self.ui.cbbCamera.currentData()
        self.control_timer(index)

    # view camera
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
    
    def showEvent(self, event: QShowEvent): #showEvent chay khi nao? Need tim hieu here/ co the thay the bang j nua dc ko?
        self.image1 = ImageWidget()
        self.label_w = self.ui.screen1.width()
        self.label_h = self.ui.screen1.height()
        self.imageLayout = self.ui.screen1.parentWidget().layout()     
        self.imageLayout.replaceWidget(self.ui.screen1, self.image1)      
        
