from app_constants import KEY_AUTH_INFO
from PySide2.QtCore import QObject, Signal


class AuthInfoAbs():
    token_info_changed: Signal

    def get_token_info(self):
        pass

    def set_token_info(self, val: dict):
        pass

    def is_logged_in(self):
        pass


class AuthInfo(QObject):
    __instance: AuthInfoAbs = None
    token_info_changed = Signal(dict)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.__token_info = None
        return

    def get_token_info(self):
        return self.__token_info

    def set_token_info(self, val: dict):
        self.__token_info = val
        self.token_info_changed.emit(val)

    def is_logged_in(self):
        return self.__token_info is not None

    @staticmethod
    def instance() -> AuthInfoAbs:
        if AuthInfo.__instance == None:
            instance = AuthInfo()
            AuthInfo.__instance = instance
        return AuthInfo.__instance
