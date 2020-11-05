from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets.main_window import MainWindow
from widgets.login_screen import LoginScreen
import asyncio
import sys
from services.login_service import LoginService
from app_constants import CONFIG_PATH
from app_models.auth_info import AuthInfo
import json
from app_constants import KEY_AUTH_INFO

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets.main_window import MainWindow
from widgets.login_screen import LoginScreen
import asyncio
import sys
from services.login_service import LoginService
from app_constants import CONFIG_PATH
from app_models.auth_info import AuthInfo
import json
from app_constants import KEY_AUTH_INFO


class MainApplication():
    def __init__(self):
        self.app_config = None
        self.auth_info = None
        self.app = None
        self.login_service = None
        self.main_window = None
        self.login_screen = None
        return

    async def run(self):
        self.app = QApplication([])
        self.app_config = self.load_app_config()
        self.auth_info = AuthInfo()
        self.auth_info.register(KEY_AUTH_INFO, self.on_auth_info_changed)
        self.login_service = LoginService(self.app_config, self.auth_info)
        await self.login_service.init_auth_info()
        self.choose_screen()
        sys.exit(self.app.exec_())

    def on_log_in_success(self, token):
        self.choose_screen()
        return

    def on_log_in_error(self, resp):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        if resp is not None:
            msg.setText("Invalid account or password")
        else:
            msg.setText("Something's wrong")

        msg.setWindowTitle("Login fail")
        return msg.exec_()

    def on_log_out(self):
        self.login_service.log_out()
        self.choose_screen()
        return

    def on_auth_info_changed(self, obj: AuthInfo):
        print("Logged in:", obj.is_logged_in())
        return

    def choose_screen(self):
        if not self.auth_info.is_logged_in():
            self.login_screen = LoginScreen(login_service=self.login_service,
                                            on_success=self.on_log_in_success,
                                            on_error=self.on_log_in_error)
            self.login_screen.show()
            if self.main_window is not None:
                self.main_window.close()
        else:
            self.main_window = MainWindow(self.login_service, self.on_log_out)
            self.main_window.show()
            if self.login_screen is not None:
                self.login_screen.close()

    def load_app_config(self):
        with open(CONFIG_PATH) as fi:
            app_config = json.load(fi)
            return app_config


async def main():
    await MainApplication().run()


if __name__ == "__main__":
    asyncio.run(main())