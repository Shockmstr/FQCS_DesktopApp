from PySide2.QtWidgets import QApplication
from widgets.main_window import MainWindow
from widgets.login_screen import LoginScreen
import asyncio
import sys
import os
from services.login_service import LoginService
from app_constants import CONFIG_PATH
from app_models.auth_info import AuthInfo
import json
from app_constants import KEY_AUTH_INFO
from services.thread_manager import ThreadManager
from app_models.app_config import AppConfig


class MainApplication():
    def __init__(self):
        self.__login_service = None
        self.auth_info = None
        self.app = None
        self.main_window = None
        self.login_screen = None
        return

    def run(self):
        AppConfig.instance().load_config()
        self.app = QApplication([])
        self.auth_info = AuthInfo()
        self.auth_info.new_token.connect(self.on_logged_in_success)
        self.auth_info.refresh_token.connect(self.on_refresh_token)
        self.auth_info.remove_token.connect(self.on_logged_out)
        self.auth_info.same_token.connect(lambda val: print("Same token"))
        self.__login_service = LoginService(self.auth_info)
        self.__login_service.init_auth_info()
        self.choose_screen()
        return self.app.exec_()

    def on_logged_in_success(self, token):
        print("Logged in")
        self.choose_screen()
        return

    def on_refresh_token(self, token):
        print("Refresh token")
        return

    def on_logged_out(self):
        self.choose_screen()
        return

    def choose_screen(self):
        if not self.auth_info.is_logged_in() and (
                self.login_screen is None
                or not self.login_screen.isActiveWindow()):
            self.login_screen = LoginScreen(self.__login_service)
            self.login_screen.show()
            if self.main_window is not None:
                self.main_window.close()
        elif (self.main_window is None
              or not self.main_window.isActiveWindow()):
            self.main_window = MainWindow(self.__login_service)
            self.main_window.show()
            if self.login_screen is not None:
                self.login_screen.close()


async def main():
    with ThreadManager.instance() as tm:
        status = MainApplication().run()
    ThreadManager.instance().wait()
    sys.exit(status)


if __name__ == "__main__":
    asyncio.run(main())