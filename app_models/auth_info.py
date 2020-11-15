from app_constants import KEY_AUTH_INFO
from PySide2.QtCore import QObject, Signal


class AuthInfo(QObject):
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