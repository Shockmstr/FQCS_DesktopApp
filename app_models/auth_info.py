from app.observer import Subject
from app_constants import KEY_AUTH_INFO


class AuthInfo(Subject):
    def __init__(self):
        super().__init__()
        self.__token_info = None
        return

    def get_token_info(self):
        return self.__token_info

    def set_token_info(self, val):
        self.__token_info = val
        self.notify(KEY_AUTH_INFO)

    def is_logged_in(self):
        return self.__token_info is not None