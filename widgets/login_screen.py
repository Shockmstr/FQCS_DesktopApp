from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Signal
from services.identity_service import IdentityService
from views.login_screen import Ui_LoginScreen
from app import helpers


class LoginScreen(QWidget):
    def __init__(self, identity_service: IdentityService, parent=None):
        QWidget.__init__(self, parent)
        self.__identity_service = identity_service
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.binding()

    def showEvent(self, event):
        return

    # binding
    def binding(self):
        self.ui.btnLogin.clicked.connect(self.btn_login_clicked)
        return

    # handler
    def btn_login_clicked(self):
        username = self.ui.inpAcc.text()
        password = self.ui.inpPass.text()
        is_success, resp = self.__identity_service.log_in(username, password)
        if is_success and self.__identity_service.is_device_account(resp):
            self.__identity_service.save_token_json(resp)
            self.__identity_service.check_token()
        else:
            if is_success is not None:
                helpers.show_message("Invalid account or password")
            else:
                helpers.show_message("Something's wrong")
