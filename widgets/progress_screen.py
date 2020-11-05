from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from views.progress_screen import Ui_ProgressScreen
from widgets.image_widget import ImageWidget
from cv2 import cv2


class ProgressScreen(QWidget):
    CAMERA_LOADED = False
    def __init__(self, homeScreen: (), main_window):
        QWidget.__init__(self)
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.binding(homeScreen = homeScreen)
        
    # data binding
    def binding(self, homeScreen: ()):
        self.ui.btnStop.clicked.connect(homeScreen)
        self.ui.btnCapture.clicked.connect(self.cam_control)

    def cam_control(self):
        if self.CAMERA_LOADED == True:
            self.ui.btnCapture.setText("STOP")
            self.main_window.stop()
            self.CAMERA_LOADED = False
        elif self.CAMERA_LOADED == False:
            self.ui.btnCapture.setText("CAPTURE")
            self.main_window.capture()
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
        # else:
        #     self.ui.btnCapture.setText("CAPTURE")
