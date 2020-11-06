from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from views.asym_config_screen import Ui_AsymConfigScreen
from app_models.detector_config import DetectorConfig
from widgets.image_widget import ImageWidget
import cv2


class AsymConfigScreen(QWidget):
    MIN_SIMILARITY_STEP = 0.01
    CAMERA_LOADED = False
    backscreen: Signal
    nextscreen: Signal

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_AsymConfigScreen()
        self.ui.setupUi(self)
        self.detector_cfg = DetectorConfig.instance() .config
        self.backscreen = self.ui.btnBack.clicked
        self.nextscreen = self.ui.btnNext.clicked
        self.binding()
        self.load_cfg()
        
    # binding
    def binding(self):
        self.ui.sldAmpRate.valueChanged.connect(self.amplification_rate_changed)
        self.ui.sldMinSimilarity.valueChanged.connect(self.min_similarity_changed)

    # handlers
    def amplification_rate_changed(self):
        value = self.ui.sldAmpRate.value()
        self.detector_cfg["sim_cfg"]["asym_amp_rate"] = value
        self.ui.grpBoxAmpRate.setTitle("Amplification rate: " + str(value))

    def min_similarity_changed(self):
        value = round(self.ui.sldMinSimilarity.value() * self.MIN_SIMILARITY_STEP, 2)
        self.detector_cfg["sim_cfg"]["min_similarity"] = value
        self.ui.grpBoxMinSimilarity.setTitle("Minimum similarity (%): " + str(value))

    def replace_camera_widget(self):
        if not self.CAMERA_LOADED:
            self.image1 = ImageWidget()            
            self.label_w = self.ui.screen1.width()
            self.label_h = self.ui.screen1.height()
            self.imageLayout = self.ui.screen1.parentWidget().layout()
            self.imageLayout.replaceWidget(self.ui.screen1, self.image1)       
            self.CAMERA_LOADED = True

    def view_cam(self, image):
        # read image in BGR format       
        self.replace_camera_widget()
        self.img = image
        self.dim = (self.label_w, self.label_h)
        self.img = cv2.resize(self.img, self.dim)
        self.image1.imshow(self.img)

    def load_cfg(self):
        cfg = self.detector_cfg["sim_cfg"]
        c1 = cfg["C1"]
        c2 = cfg["C2"]
        psnr = cfg["psnr_trigger"]
        amp_thresh = cfg["asym_amp_thresh"]
        amp_rate = cfg["asym_amp_rate"]
        min_similarity = cfg["min_similarity"]
        re_calc_factor_left = cfg["re_calc_factor_left"]
        re_calc_factor_right = cfg["re_calc_factor_right"]
        segments_list = cfg["segments_list"]
        #---------------------------------------#
        min_similarity_slider_val = round(min_similarity / self.MIN_SIMILARITY_STEP, 0)
        if (amp_thresh is None): amp_thresh = 0
        #---------------------------------------#
        self.ui.inpC1.setValue(c1)
        self.ui.inpC2.setValue(c2)
        self.ui.inpPSNR.setValue(int(psnr))
        self.ui.inpAmpThresh.setValue(int(amp_thresh))
        self.ui.inpReCalcFactorLeft.setValue(int(re_calc_factor_left))
        self.ui.inpReCalcFactorRight.setValue(int(re_calc_factor_right))
        self.ui.inpSegments.setText(segments_list.__str__())
        self.ui.sldMinSimilarity.setValue(int(min_similarity_slider_val))
        self.ui.grpBoxMinSimilarity.setTitle("Minimum similarity (%): " + str(min_similarity))
        self.ui.sldAmpRate.setValue(int(amp_rate))
        self.ui.grpBoxAmpRate.setTitle("Amplification rate: " + str(amp_rate))



        

