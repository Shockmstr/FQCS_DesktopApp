from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.main_window import Ui_MainWindow
from FQCS import detector
from models.detector_config import *
from app.helpers import *
# from widgets.detection_config_screen_layout import DetectionConfigScreen


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.bind_exit_program()
        self.bind_load_config()
        self.bind_save_config()
        # screen 1
        # self.detection_screen = DetectionConfigScreen()
        # self.setCentralWidget(self.detection_screen)
        # event handler

    def exit_program(self):
        self.close()

    # binding
    def bind_exit_program(self):
        self.ui.actionExit.triggered.connect(self.exit_program)

    def bind_load_config(self):
        self.ui.actionLoadCfg.triggered.connect(self.on_load_config)

    def bind_save_config(self):
        self.ui.actionSaveCfg.triggered.connect(self.on_save_config)

    # event handlers
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
