from app_constants import KEY_AUTH_INFO
from PySide2.QtCore import QObject, Signal


class AuthInfo(QObject):
    new_token = Signal(dict)
    refresh_token = Signal(dict)
    remove_token = Signal(dict)
    same_token = Signal(dict)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.__token_info = None
        return

    def get_token_info(self):
        return self.__token_info

    def set_token_info(self, val: dict):
        old_token = self.__token_info
        self.__token_info = val
        if val == old_token:
            self.same_token.emit(val)
        elif val is None:
            if old_token is not None:
                self.remove_token.emit(old_token)
        else:
            if old_token is not None:
                self.refresh_token.emit(val)
            else: self.new_token.emit(val)

    def is_logged_in(self):
        return self.__token_info is not None