from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Signal, QTimer
from views.main_window import Ui_MainWindow
from FQCS import detector
from FQCS.manager import FQCSManager
from app_models.detector_config import DetectorConfig
from app import helpers
import cv2
from widgets.measurement_screen import MeasurementScreen
from widgets.home_screen import HomeScreen
from widgets.test_detect_pair_screen import TestDetectPairScreen
from widgets.color_preprocess_config_screen import ColorPreprocessConfigScreen
from widgets.detection_config_screen import DetectionConfigScreen
from widgets.color_param_calibration_screen import ColorParamCalibrationScreen
from widgets.error_detect_screen import ErrorDetectScreen
from widgets.progress_screen import ProgressScreen
from widgets.asym_config_screen import AsymConfigScreen
from services.identity_service import IdentityService
from qasync import QEventLoop, asyncSlot
import asyncio


class MainWindow(QMainWindow):
    def __init__(self, identity_service: IdentityService):
        QMainWindow.__init__(self)
        self.__identity_service = identity_service
        self.__camera_timer = QTimer()
        self.__process_cam = None
        self.__video_camera = None
        self.__detector_cfg = DetectorConfig.instance()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.build()
        self.binding()

    def build(self):
        # screen 0
        self.home_screen = HomeScreen(self.__identity_service, self)
        # screen 1
        self.detection_screen = DetectionConfigScreen(self)
        # screen 2
        self.measurement_screen = MeasurementScreen(self)
        # screen 3
        self.test_detect_pair_screen = TestDetectPairScreen(self)
        # screen 4
        self.color_preprocess_config_screen = ColorPreprocessConfigScreen(self)
        # screen 5
        self.color_param_calib_screen = ColorParamCalibrationScreen(self)
        # screen 6
        self.error_detect_screen = ErrorDetectScreen(self)
        # screen 7
        self.progress_screen = ProgressScreen(self)
        # screen 8
        self.asym_config_screen = AsymConfigScreen(self)

        # add to Stacked Widget
        self.ui.centralStackWidget.addWidget(self.home_screen)
        self.ui.centralStackWidget.addWidget(self.detection_screen)
        self.ui.centralStackWidget.addWidget(self.measurement_screen)
        self.ui.centralStackWidget.addWidget(self.test_detect_pair_screen)
        self.ui.centralStackWidget.addWidget(self.asym_config_screen)
        self.ui.centralStackWidget.addWidget(
            self.color_preprocess_config_screen)
        self.ui.centralStackWidget.addWidget(self.color_param_calib_screen)
        self.ui.centralStackWidget.addWidget(self.error_detect_screen)
        self.ui.centralStackWidget.addWidget(self.progress_screen)

    def showEvent(self, event):
        return

    # binding
    def binding(self):
        self.ui.actionExit.triggered.connect(self.action_exit_triggered)
        self.ui.actionLoadCfg.triggered.connect(
            self.action_load_config_triggered)
        self.ui.actionSaveCfg.triggered.connect(self.action_save_triggered)
        self.__camera_timer.timeout.connect(self.camera_timer_timeout)
        self.ui.centralStackWidget.currentChanged.connect(
            self.current_stack_widget_changed)

        self.home_screen.action_edit.connect(self.change_detection_screen)
        self.home_screen.action_start.connect(self.change_progress_screen)
        self.home_screen.action_exit.connect(self.action_exit_triggered)

        self.detection_screen.backscreen.connect(self.change_home_screen)
        self.detection_screen.nextscreen.connect(
            self.change_measurement_screen)
        self.detection_screen.captured.connect(self.start_capture)
        self.detection_screen.camera_changed.connect(self.camera_changed)

        self.measurement_screen.backscreen.connect(
            self.change_detection_screen)
        self.measurement_screen.nextscreen.connect(
            self.skipable_change_detect_pair_screen)

        self.test_detect_pair_screen.backscreen.connect(
            self.change_measurement_screen)
        self.test_detect_pair_screen.nextscreen.connect(
            self.change_asym_config_screen)

        self.asym_config_screen.backscreen.connect(
            self.change_detect_pair_screen)
        self.asym_config_screen.nextscreen.connect(
            self.change_color_preprocess_config_screen)

        self.color_preprocess_config_screen.backscreen.connect(
            self.change_asym_config_screen)
        self.color_preprocess_config_screen.nextscreen.connect(
            self.change_color_param_calib_screen)

        self.color_param_calib_screen.backscreen.connect(
            self.change_color_preprocess_config_screen)
        self.color_param_calib_screen.nextscreen.connect(
            self.change_error_detect_screen)

        self.error_detect_screen.backscreen.connect(
            self.skipable_color_param_calib_screen)
        self.error_detect_screen.nextscreen.connect(
            self.change_progress_screen)

        self.progress_screen.return_home.connect(self.change_home_screen)
        self.progress_screen.captured.connect(self.start_capture)
        self.progress_screen.stopped.connect(self.stop_capture)
        return

    def closeEvent(self, event):
        video_cameras = self.__detector_cfg.get_video_cameras()
        for vid in video_cameras:
            vid.release()
        DetectorConfig.instance().reset()

    def camera_timer_timeout(self):
        if (self.__video_camera is not None and self.__video_camera.isOpened()
                and self.__process_cam is not None):
            _, image = self.__video_camera.read()
            self.__process_cam(image)

    # event handler
    def camera_changed(self, index):
        if self.__video_camera is not None:
            self.__video_camera.release()
        self.__video_camera = self.__detector_cfg.get_current_camera()
        if self.__video_camera is None: return
        if index is not None and index > -1:
            self.__video_camera.open(index)
        else:
            self.__video_camera.release()

    def action_exit_triggered(self):
        self.close()

    def skipable_change_detect_pair_screen(self):
        idx, cfg = self.__detector_cfg.get_current_cfg()
        continue_screen = cfg["is_main"]
        if continue_screen:
            self.ui.centralStackWidget.setCurrentWidget(
                self.test_detect_pair_screen)
        else:
            # skip to screen 6 if only side camera is selected
            self.ui.centralStackWidget.setCurrentWidget(
                self.error_detect_screen)

    def skipable_color_param_calib_screen(self):
        idx, cfg = self.__detector_cfg.get_current_cfg()
        continue_screen = cfg["is_main"]
        if continue_screen:
            self.ui.centralStackWidget.setCurrentWidget(
                self.color_param_calib_screen)
        else:
            # skip to screen 6 if only side camera is selected
            self.ui.centralStackWidget.setCurrentWidget(
                self.measurement_screen)

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

    def change_asym_config_screen(self):
        self.ui.centralStackWidget.setCurrentWidget(self.asym_config_screen)

    def current_stack_widget_changed(self):
        currentWidget = self.ui.centralStackWidget.currentWidget()
        if (currentWidget == self.detection_screen):
            self.__process_cam = self.detection_screen.view_cam
            self.start_capture()
        elif (currentWidget == self.measurement_screen):
            self.__process_cam = self.measurement_screen.view_cam
            self.start_capture()
        elif (currentWidget == self.color_preprocess_config_screen):
            self.__process_cam = None
            self.stop_capture()
            self.color_preprocess_config_screen.view_image()
        elif (currentWidget == self.color_param_calib_screen):
            self.__process_cam = self.color_param_calib_screen.view_cam
            self.start_capture()
        elif (currentWidget == self.test_detect_pair_screen):
            self.__process_cam = self.test_detect_pair_screen.view_cam
            self.start_capture()
        elif (currentWidget == self.error_detect_screen):
            self.__process_cam = self.error_detect_screen.view_cam
            self.start_capture()
        elif (currentWidget == self.progress_screen):
            self.__process_cam = self.progress_screen.view_cam
            self.start_capture()
        elif (currentWidget == self.asym_config_screen):
            self.__process_cam = self.asym_config_screen.view_cam
            self.start_capture()
        else:
            self.stop_capture()

    def stop_capture(self):
        self.__camera_timer.stop()

    def start_capture(self):
        if (not self.__camera_timer.isActive()):
            # start timer
            self.__camera_timer.start(20)

    @asyncSlot()
    async def action_load_config_triggered(self):
        file_path = helpers.file_chooser_open_directory(self)
        if file_path is not None:
            manager = FQCSManager(config_folder=file_path)
            manager.load_sample_images()
            configs = manager.get_configs()
            for cfg in configs:
                if cfg["is_main"] == True:
                    self.__detector_cfg.set_current_cfg_name(cfg["name"])
                    await manager.load_model(cfg)
                    break
            self.__detector_cfg.set_manager(manager)
            self.__detector_cfg.set_current_path(file_path)
        else:
            print("Error loading config")

    def action_save_triggered(self):
        manager = self.__detector_cfg.get_manager()
        configs = manager.get_configs()
        if configs is not None:
            file_path = helpers.file_chooser_open_directory(self)
            if (file_path):
                manager.save_config(file_path)
                self.__detector_cfg.set_current_path(file_path)
        else:
            print("No config provided")
