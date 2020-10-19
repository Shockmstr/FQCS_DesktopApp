from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.main_window import Ui_MainWindow
from FQCS import detector
from models.detector_config import *
from app.helpers import *
from widgets.measurement_screen import MeasurementScreen
from widgets.test_detect_pair_screen import TestDetectPairScreen
from widgets.color_preprocess_config_screen import ColorPreprocessConfigScreen
from widgets.detection_config_screen_layout import DetectionConfigScreen
from widgets.color_param_calibration_screen import ColorParamCalibrationScreen
from widgets.error_detect_screen import ErrorDetectScreen
from widgets.progress_screen import ProgressScreen


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.showFullScreen()
        self.bind_exit_program()

        self.bind_load_config()
        self.bind_save_config()

        # screen 1
        self.detection_screen = DetectionConfigScreen(
            nextscreen=self.change_measurement_screen)

        # screen 2
        self.measurement_screen = MeasurementScreen(
            backscreen=self.change_detection_screen,
            nextscreen=self.change_detect_pair_screen)

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
        self.progress_screen = ProgressScreen()

        # add to Stacked Widget
        self.ui.centralStackWidget.addWidget(self.detection_screen)
        self.ui.centralStackWidget.addWidget(self.measurement_screen)
        self.ui.centralStackWidget.addWidget(self.test_detect_pair_screen)
        self.ui.centralStackWidget.addWidget(
            self.color_preprocess_config_screen)
        self.ui.centralStackWidget.addWidget(self.color_param_calib_screen)
        self.ui.centralStackWidget.addWidget(self.error_detect_screen)
        self.ui.centralStackWidget.addWidget(self.progress_screen)

    # binding

    def bind_exit_program(self):
        self.ui.actionExit.triggered.connect(self.exit_program)

    def bind_load_config(self):
        self.ui.actionLoadCfg.triggered.connect(self.on_load_config)

    def bind_save_config(self):
        self.ui.actionSaveCfg.triggered.connect(self.on_save_config)

    # event handler

    def exit_program(self):
        self.close()

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
        self.ui.centralStackWidget.setCurrentWidget(
            self.error_detect_screen)

    def change_progress_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(
            self.progress_screen)

    def on_load_config(self):
        file_path = file_chooser_open_directory(self)
        if (file_path is not None):
            temp_cfg = detector.load_json_cfg(file_path)
            print(temp_cfg)
            DetectorConfig.getInstance().load_config(temp_cfg)
        else:
            print("Error loading config")

    def on_save_config(self):
        configs = DetectorConfig.getInstance().config
        print(configs)
        if configs is not None:
            configs["min_area"] = 1
            file_path = file_chooser_open_directory(self)
            if (file_path):
                detector.save_json_cfg(configs, file_path)
        else:
            print("No config provided")
