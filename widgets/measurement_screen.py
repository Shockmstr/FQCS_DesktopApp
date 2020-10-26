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
        self.ui.sldMininumHeight.valueChanged.connect(self.draw_rectangle_on_image)
        self.ui.sldMininumWidth.valueChanged.connect(self.draw_rectangle_on_image)
        self.ui.sldDectectPosition.valueChanged.connect(self.detect_position_change)

    def draw_rectangle_on_image(self):
        if self.sender() == self.ui.sldMininumWidth:
            self.width_value = self.ui.sldMininumWidth.value()
            self.ui.groupSliderWidth.setTitle("Mininum width(%): " + str(self.width_value))
        if self.sender() == self.ui.sldMininumHeight:
            self.height_value = self.ui.sldMininumHeight.value()
            self.ui.groupSliderHeight.setTitle("Mininum height(&): " + str(self.height_value))
            
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
