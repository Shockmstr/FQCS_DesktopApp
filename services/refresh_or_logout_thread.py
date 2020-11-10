from PySide2.QtCore import QTimer, QThread
from services.login_service import LoginService
from app_models.app_config import AppConfig


class RefreshOrLogoutThread(QThread):
    def __init__(self,
                 login_service: LoginService,
                 is_refresh,
                 timeout,
                 parent=None):
        QThread.__init__(self, parent)
        self.__is_refresh = is_refresh
        self.__timeout = timeout
        self.__login_service = login_service

    def run(self):
        self.__refresh_timer = QTimer()
        callback = self.__refresh_callback if self.__is_refresh else self.__logout_callback
        self.__refresh_timer.timeout.connect(callback)
        self.__refresh_timer.setSingleShot(True)
        self.__refresh_timer.start(self.__timeout)

    def __refresh_callback(self):
        try:
            print("Refresh callback")
            form_data = {}
            form_data['grant_type'] = 'refresh_token'
            form_data['refresh_token'] = token['refresh_token']
            url = "{}/api/users/login".format(
                AppConfig.instance().config['api_url'])
            resp = requests.post(url, data=form_data)
            if (resp.status_code >= 200 and resp.status_code < 300):
                data = resp.json()
                self.__login_service.save_token_json(data)
                trio.run(self.__login_service.check_token)
            else:
                raise Exception("Resp error")
        except:
            print("Error refresh callback")
            self.__login_service.log_out()
        finally:
            self.__refresh_timer.stop()
            self.quit()
        return

    def __logout_callback(self):
        try:
            self.__login_service.log_out()
        except:
            print("Log out error")
        finally:
            self.__refresh_timer.stop()
            self.quit()
        return