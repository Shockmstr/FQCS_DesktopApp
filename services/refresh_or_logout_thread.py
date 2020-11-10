from PySide2.QtCore import QTimer, QThread
from app_models.app_config import AppConfig
from FQCS import fqcs_api


class RefreshOrLogoutThread(QThread):
    def __init__(self, login_service, token, is_refresh, timeout, parent=None):
        QThread.__init__(self, parent)
        self.__token = token
        self.__is_refresh = is_refresh
        self.__timeout = timeout
        self.__login_service = login_service

    def run(self):
        print("Start thread")
        self.__refresh_timer = QTimer()
        callback = self.__refresh_callback if self.__is_refresh else self.__logout_callback
        self.__refresh_timer.timeout.connect(callback)
        self.__refresh_timer.setSingleShot(True)
        self.__refresh_timer.start(self.__timeout)
        self.exec_()
        self.__stop_timer()
        print("End thread")

    def __refresh_callback(self):
        try:
            print("Refresh callback")
            api_url = AppConfig.instance().config['api_url']
            rf_token = self.__token['refresh_token']
            (status, resp) = fqcs_api.refresh_token(api_url, rf_token)
            if (status == True):
                self.__login_service.save_token_json(resp)
                trio.run(self.__login_service.check_token)
            else:
                raise Exception("Resp error")
        except:
            print("Error refresh callback")
            self.__login_service.log_out()
        finally:
            self.__stop_timer()
            self.quit()
        return

    def __logout_callback(self):
        try:
            self.__login_service.log_out()
        except:
            print("Log out error")
        finally:
            self.__stop_timer()
            self.quit()
        return

    def __stop_timer(self):
        self.__refresh_timer.stop()
