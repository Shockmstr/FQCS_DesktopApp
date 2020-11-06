from PySide2.QtWidgets import QWidget, QMessageBox
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
            choice = self.on_logged_in_error(resp)
            self.error.emit(resp)

    def on_logged_in_error(self, resp):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        if resp is not None:
            msg.setText("Invalid account or password")
        else:
            msg.setText("Something's wrong")

        msg.setWindowTitle("Login fail")
        return msg.exec_()