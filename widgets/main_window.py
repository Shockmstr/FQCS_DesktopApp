from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.main_window import Ui_MainWindow
from FQCS import detector
from models.detector_config import *
from app.helpers import *
import cv2
from widgets.measurement_screen import MeasurementScreen
from widgets.home_screen import HomeScreen
from widgets.test_detect_pair_screen import TestDetectPairScreen
from widgets.color_preprocess_config_screen import ColorPreprocessConfigScreen
from widgets.detection_config_screen import DetectionConfigScreen
from widgets.color_param_calibration_screen import ColorParamCalibrationScreen
from widgets.error_detect_screen import ErrorDetectScreen
from widgets.progress_screen import ProgressScreen


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()
        self.detector_cfg = DetectorConfigSingleton.get_instance()
        self.video_camera = cv2.VideoCapture()
        self.timer = QTimer()
        self.process_cam = None
        self.binding()

        # screen 0
        self.home_screen = HomeScreen(configScreen=self.change_detection_screen, progressScreen=self.change_progress_screen, on_exit=self.exit_program)

        # screen 1
        self.detection_screen = DetectionConfigScreen(
            backscreen=self.change_home_screen,
            nextscreen=self.change_measurement_screen,
            main_window = self)

        # screen 2
        self.measurement_screen = MeasurementScreen(
            backscreen=self.change_detection_screen,
            nextscreen=self.change_detect_pair_screen,
            main_window = self)

        # screen 3
        self.test_detect_pair_screen = TestDetectPairScreen(
            backscreen=self.change_measurement_screen,
            nextscreen=self.change_color_preprocess_config_screen)

        # screen 4
        self.color_preprocess_config_screen = ColorPreprocessConfigScreen(
            backscreen=self.change_detect_pair_screen,
            nextscreen=self.change_color_param_calib_screen)

        # screen 5
        self.color_param_calib_screen = ColorParamCalibrationScreen(
            backscreen=self.change_color_preprocess_config_screen,
            nextscreen=self.change_error_detect_screen)

        # screen 6
        self.error_detect_screen = ErrorDetectScreen(
            backscreen=self.change_color_param_calib_screen,
            nextscreen=self.change_progress_screen)

        # screen 7
        self.progress_screen = ProgressScreen(homeScreen = self.change_home_screen)

        # add to Stacked Widget
        self.ui.centralStackWidget.addWidget(self.home_screen)
        self.ui.centralStackWidget.addWidget(self.detection_screen)
        self.ui.centralStackWidget.addWidget(self.measurement_screen)
        self.ui.centralStackWidget.addWidget(self.test_detect_pair_screen)
        self.ui.centralStackWidget.addWidget(
            self.color_preprocess_config_screen)
        self.ui.centralStackWidget.addWidget(self.color_param_calib_screen)
        self.ui.centralStackWidget.addWidget(self.error_detect_screen)
        self.ui.centralStackWidget.addWidget(self.progress_screen)

    # binding
    def binding(self):
        self.ui.actionExit.triggered.connect(self.exit_program)
        self.ui.actionLoadCfg.triggered.connect(self.on_load_config)
        self.ui.actionSaveCfg.triggered.connect(self.on_save_config)
        self.timer.timeout.connect(self.show_cam)
        self.ui.centralStackWidget.currentChanged.connect(self.widget_change)

    def show_cam(self):
        if (self.video_camera.isOpened() and self.process_cam is not None):
            _, image = self.video_camera.read()
            self.process_cam(image)

    # start/stop timer
    def control_timer(self, active):
        # if timer is stopped
        if active:
            if (not self.timer.isActive()):
                # start timer
                self.timer.start(20)
        # if timer is started
        else:
            self.timer.stop()

    # event handler
    def exit_program(self):
        self.close()

    def change_home_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.home_screen)

    def change_detection_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.detection_screen)

    def change_measurement_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.measurement_screen)

    def change_detect_pair_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(
            self.test_detect_pair_screen)

    def change_color_preprocess_config_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(
            self.color_preprocess_config_screen)

    def change_color_param_calib_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(
            self.color_param_calib_screen)

    def change_error_detect_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.error_detect_screen)

    def change_progress_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.progress_screen)

    def widget_change(self):
        currentWidget = self.ui.centralStackWidget.currentWidget()
        if (currentWidget == self.detection_screen):
            self.process_cam = self.detection_screen.view_cam
            self.control_timer(True)
        elif (currentWidget == self.measurement_screen):
            self.process_cam = self.measurement_screen.view_cam
            self.control_timer(True)    
        elif (currentWidget == self.color_param_calib_screen):
            self.process_cam = self.color_param_calib_screen.view_cam 
            self.control_timer(True)
        elif (currentWidget == self.test_detect_pair_screen):
            self.process_cam = self.test_detect_pair_screen.view_cam
            self.control_timer(True)
        elif (currentWidget == self.error_detect_screen):
            self.process_cam = self.error_detect_screen.view_cam
            self.control_timer(True)
        else:
            self.control_timer(False)

    def capture(self):
        self.control_timer(False)

    def on_load_config(self):
        file_path = file_chooser_open_directory(self)
        if file_path is not None:
            temp_cfg = detector.load_json_cfg(file_path)
            self.detector_cfg.load_config(temp_cfg)
            self.detector_cfg.current_path = file_path
        else:
            print("Error loading config")

    def on_save_config(self):
        configs = self.detector_cfg.config
        if configs is not None:
            file_path = file_chooser_open_directory(self)
            if (file_path):
                detector.save_json_cfg(configs, file_path)
                self.detector_cfg.current_path = file_path
        else:
            print("No config provided")
