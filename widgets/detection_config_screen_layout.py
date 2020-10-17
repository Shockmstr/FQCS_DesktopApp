from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.detection_config_screen_layout import Ui_DetectionConfigScreen

class DetectionConfigScreen(QWidget):
    def __init__(self, nextscreen: ()):
        QWidget.__init__(self)
        self.ui = Ui_DetectionConfigScreen()
        self.ui.setupUi(self)
        self.binding(nextscreen=nextscreen)
    
    # binding
    def binding(self, nextscreen: ()):
        self.ui.sldBrightness.valueChanged.connect(self.brightness_value_change)
        self.ui.sldContrast.valueChanged.connect(self.contrast_value_change)
        self.ui.sldThreshold1.valueChanged.connect(self.threshold1_value_change)
        self.ui.sldThreshold2.valueChanged.connect(self.threshold2_value_change)
        self.ui.sldBlur.valueChanged.connect(self.blur_value_change)
        self.ui.sldDilate.valueChanged.connect(self.dilate_value_change)
        self.ui.sldErode.valueChanged.connect(self.erode_value_change)
        self.ui.sldBkgThresh.valueChanged.connect(self.bkg_value_change)
        self.ui.sldLightAdj.valueChanged.connect(self.light_adj_value_change)
        self.ui.sldLightAdjRange.valueChanged.connect(self.light_adj_range_value_change)

        self.ui.cbbWidth.setPlaceholderText("Width")
        self.ui.cbbHeight.setPlaceholderText("Height")
        self.ui.cbbWidth.setCurrentIndex(-1)
        self.ui.cbbHeight.setCurrentIndex(-1)

        self.ui.cbbCamera.clear()
        self.ui.cbbCamera.addItem("Camera 1")
        self.ui.cbbCamera.addItem("Camera 2")
        self.ui.cbbCamera.addItem("Camera 3")

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

        self.ui.cbbMethod.activated[int].connect(self.ui.stackContainerMid.setCurrentIndex)

        self.ui.btnNext.clicked.connect(nextscreen)

    # handler
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
        self.ui.grpboxBkgThreshold.setTitle("Background Threshold: " + str(value))

    def light_adj_value_change(self):
        value = self.ui.sldLightAdj.value()
        self.ui.grpboxLightAdj.setTitle("Light Adjustment: " + str(value))

    def light_adj_range_value_change(self):
        value = self.ui.sldLightAdjRange.value()
        self.ui.grpboxLightAdjRange.setTitle("Light Adjustment: " + str(value))
        
    def slider_value_change(self, slider: QSlider , grpboxSlider: QGroupBox):
        value = slider.value()
        title = grpboxSlider.title().split(":")[0] # get the first name before : to eliminate duplicate
        grpboxSlider.setTitle(title + ": " + str(value))