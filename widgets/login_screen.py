from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from services.login_service import LoginService
from views.login_screen import Ui_LoginScreen
import trio


class LoginScreen(QWidget):
    success = Signal(dict)
    error = Signal(Exception)

    def __init__(self, login_service: LoginService, parent=None):
        QWidget.__init__(self, parent)
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
        is_success, resp = trio.run(self.__login_service.log_in, username,
                                    password)
        if is_success:
            self.success.emit(resp)
        else:
            self.error.emit(resp)
