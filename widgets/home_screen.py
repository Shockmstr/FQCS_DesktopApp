from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from views.home_screen import Ui_HomeScreen
from services.identity_service import IdentityService
from app_models.detector_config import DetectorConfig
from app_models.app_config import AppConfig


class HomeScreen(QWidget):
    action_edit: Signal
    action_start: Signal
    action_exit: Signal

    def __init__(self, identity_service: IdentityService, parent=None):
        QWidget.__init__(self, parent)
        self.__identity_service = identity_service
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)
        self.binding()

    def showEvent(self, event):
        self.__set_current_config_path()
        app_cfg = AppConfig.instance()
        api_url = app_cfg.config["api_url"]
        storage_path = app_cfg.config["storage_path"]
        self.ui.lblLocalServer.setText(f"**Local server**: {api_url}")
        self.ui.lblLocalStorage.setText(f"**Local storage**: {storage_path}")
        return

    def __set_current_config_path(self):
        current_path = DetectorConfig.instance().get_current_path()
        self.ui.lblConfigLocation.setText(
            f"**Current config location**: {current_path}")

    def manager_changed(self):
        self.__set_current_config_path()

    # data binding
    def binding(self):
        self.action_edit = self.ui.btnEditConfig.clicked
        self.action_start = self.ui.btnStart.clicked
        self.action_exit = self.ui.btnExit.clicked
        self.ui.btnLogout.clicked.connect(self.btn_log_out)
        DetectorConfig.instance().manager_changed.connect(self.manager_changed)
        return

    def btn_log_out(self, event: bool):
        self.__identity_service.log_out()
