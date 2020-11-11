from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal
from services.identity_service import IdentityService
from views.login_screen import Ui_LoginScreen


class LoginScreen(QWidget):
    success = Signal(dict)
    error = Signal(Exception)

    def __init__(self, identity_service: IdentityService, parent=None):
        QWidget.__init__(self, parent)
        self.__identity_service = identity_service
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.binding()

    # data binding
    def binding(self):
        self.ui.btnLogin.clicked.connect(self.log_in)
        return

    def log_in(self):
        username = self.ui.inpAcc.text()
        password = self.ui.inpPass.text()
        is_success, resp = self.__identity_service.log_in(username, password)
        if is_success and self.__identity_service.is_device_account(resp):
            self.__identity_service.save_token_json(resp)
            self.__identity_service.check_token()
            self.success.emit(resp)
        else:
            choice = self.on_logged_in_error(is_success)
            self.error.emit(resp)

    def on_logged_in_error(self, is_success):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        if is_success is not None:
            msg.setText("Invalid account or password")
        else:
            msg.setText("Something's wrong")

        msg.setWindowTitle("Login fail")
        return msg.exec_()