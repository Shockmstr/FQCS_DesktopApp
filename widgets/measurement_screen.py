from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import numpy as np
import cv2 as cv

from views.measurement_screen import Ui_MeasurementScreen

class MeasurementScreen(QWidget):
    def __init__(self, backscreen: (), nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_MeasurementScreen()
        self.ui.setupUi(self)
        self.label_width = 0
        self.label_height = 0
        self.height_value =  0
        self.width_value = 0
        self.binding(backscreen=backscreen, nextscreen=nextscreen)

    # binding
    def binding(self, backscreen:(), nextscreen: ()):
        self.ui.btnBack.clicked.connect(backscreen)
        self.ui.btnNext.clicked.connect(nextscreen)
        self.ui.sldMaximumHeight.valueChanged.connect(self.draw_rectangle_on_image)
        self.ui.sldMaximumWidth.valueChanged.connect(self.draw_rectangle_on_image)
        self.ui.sldDectectPosition.valueChanged.connect(self.draw_position_line_on_image)
        self.ui.sldDetectRange.valueChanged.connect(self.detect_range_change)
        self.ui.inpLeftActualLength.textChanged.connect(self.actual_length_change)
        self.ui.inpAllowDiff.textChanged.connect(self.allow_diff_change)

    def draw_rectangle_on_image(self):
        if self.sender() == self.ui.sldMaximumWidth:
            self.width_value = self.ui.sldMaximumWidth.value()
            self.ui.groupSliderWidth.setTitle("Maximum width(%): " + str(self.width_value))
        if self.sender() == self.ui.sldMaximumHeight:
            self.height_value = self.ui.sldMaximumHeight.value()
            self.ui.groupSliderHeight.setTitle("Maximum height(%): " + str(self.height_value))
            
        self.label_width = self.ui.screen1.width()
        self.label_height = self.ui.screen1.height()

        rectange_width = int(self.label_width * self.width_value / 100)
        rectange_height = int(self.label_height * self.height_value / 100)

        # create and read from a demo "black" image - Green boundary lines 
        img = np.zeros((self.label_height,self.label_width,3), np.uint8)

        # draw Green rectangle image into image
        cv.rectangle(img,(0,0),(rectange_width,rectange_height),(0,255,0),3)
        if img is None:
            sys.exit("Could not read the image")
        
        cv.imshow("Display window", img)

    def draw_position_line_on_image(self):
        detect_position = self.ui.sldDectectPosition.value()
        self.ui.groupSliderPosition.setTitle("Detect position: " + str(detect_position))

        self.label_width = self.ui.screen1.width()
        self.label_height = self.ui.screen1.height()

        width = int(self.label_width * detect_position / 100)

        # create and read from a demo "black" image - Green boundary lines 
        img = np.zeros((self.label_height,self.label_width,3), np.uint8)
        
        cv.line(img, (width,0), (width, self.label_height), (0, 255, 0), 3)
        if img is None:
            sys.exit("Could not read the image")
        
        cv.imshow("Display window", img)

    def calculate_length_per10px(total_px, total_length):
        return total_length / total_px * 10

    def detect_range_change(self):
        # convert 0 - 50 to scale of 0.0 to 0.5 (step 0.01)
        range_value = str(self.ui.sldDetectRange.value() / 100)
        self.ui.groupSliderDetectRange.setTitle("Detect range: " + range_value)

    def actual_length_change(self, text):
        actual_length_value = float(self.ui.inpLeftActualLength.text())

    def allow_diff_change(self, text):
        allow_diff_value = float(self.ui.inpAllowDiff.text())