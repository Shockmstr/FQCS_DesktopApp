from PySide2.QtWidgets import QApplication
from widgets.main_window import MainWindow
from widgets.login_screen import LoginScreen
import asyncio
import sys
import os
from services.identity_service import IdentityService
from app_constants import CONFIG_PATH
from app_models.auth_info import AuthInfo
import json
from app_constants import KEY_AUTH_INFO
from services.thread_manager import ThreadManager
from app_models.app_config import AppConfig
from qasync import QEventLoop


class MainApplication():
    def __init__(self):
        self.__identity_service = None
        self.auth_info = None
        self.app = None
        self.main_window = None
        self.login_screen = None
        return

    def run(self, loop):
        AppConfig.instance().load_config()
        self.auth_info = AuthInfo()
        self.__identity_service = IdentityService(self.auth_info)
        self.__identity_service.init_auth_info()
        self.auth_info.new_token.connect(self.on_logged_in_success)
        self.auth_info.refresh_token.connect(self.on_refresh_token)
        self.auth_info.remove_token.connect(self.on_logged_out)
        self.auth_info.same_token.connect(lambda val: print("Same token"))
        self.choose_screen()
        self.__identity_service.check_token()
        return loop.run_forever()

    def on_logged_in_success(self, token):
        print("Logged in")
        self.choose_screen()
        return

    def on_refresh_token(self, token):
        print("Refresh token")
        return

    def on_logged_out(self, old_token):
        print("Logged out")
        self.choose_screen()
        return

    def choose_screen(self):
        if not self.auth_info.is_logged_in() and (
                self.login_screen is None
                or not self.login_screen.isActiveWindow()):
            self.login_screen = LoginScreen(self.__identity_service)
            self.login_screen.showFullScreen()
            if self.main_window is not None:
                self.main_window.close()
        elif (self.main_window is None
              or not self.main_window.isActiveWindow()):
            self.main_window = MainWindow(self.__identity_service)
            self.main_window.showFullScreen()
            if self.login_screen is not None:
                self.login_screen.close()


if __name__ == "__main__":
    with ThreadManager.instance() as tm:
        app = QApplication([])
        loop = QEventLoop(app)
        asyncio.set_event_loop(loop)
        with loop:
            status = MainApplication().run(loop)
    ThreadManager.instance().wait()
    sys.exit(status)
