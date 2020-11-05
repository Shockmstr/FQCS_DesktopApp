from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from services.login_service import LoginService
from views.login_screen import Ui_LoginScreen
import trio


class LoginScreen(QWidget):
    def __init__(self, login_service: LoginService, on_success, on_error):
        QWidget.__init__(self)
        self.__on_success = on_success
        self.__on_error = on_error
        self.__login_service = login_service
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.binding()
        self.showFullScreen()

    # data binding
    def binding(self):
        self.ui.btnLogin.clicked.connect(self.log_in)
        return

    def log_in(self):
        username = self.ui.inpAcc.text()
        password = self.ui.inpPass.text()
        trio.run(self.__login_service.log_in, username, password,
                 self.__on_success, self.__on_error)
