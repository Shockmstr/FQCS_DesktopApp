from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
import trio
from app_models.detector_config import DetectorConfig
from FQCS import helper
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
        self.detector_cfg = DetectorConfig.instance().get_current_cfg()
        self.ui.setupUi(self)
        self.binding()
        if not self.CAMERA_LOADED:
            self.ui.containerConfig.setEnabled(False)


    # data binding
    def binding(self):
        self.ui.btnCapture.clicked.connect(self.cam_control)

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
