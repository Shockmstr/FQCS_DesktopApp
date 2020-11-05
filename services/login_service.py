import os
from app_models.auth_info import AuthInfo
from app_constants import TOKEN_PATH, ISO_DATE_FORMAT
import requests
import datetime
import asyncio
from app.fukin_thread import FukinThread
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import trio
import json


class LoginService:
    def __init__(self, app_config, auth_info: AuthInfo):
        self.__app_config = app_config
        self.__auth_info = auth_info
        self.rf_thread = None
        self.lo_thread = None

    async def init_auth_info(self):
        if os.path.exists(TOKEN_PATH):
            with open(TOKEN_PATH) as fi:
                token = json.load(fi)
                self.__auth_info.set_token_info(token)
        await self.check_token()
        return

    async def check_token(self):
        token = self.__auth_info.get_token_info()
        if (token is not None and 'expires_utc' in token):
            cur_exp_str = token['expires_utc']
            cur = datetime.datetime.utcnow()
            exp = datetime.datetime.strptime(cur_exp_str, ISO_DATE_FORMAT)
            min_diff_delta = exp - cur
            min_diff = min_diff_delta.total_seconds() / 60
            min_diff = 0 if min_diff < 0 else min_diff
            min_ref_diff = min_diff - 5
            min_ref_diff = 0 if min_ref_diff < 0 else min_ref_diff
            print('Refresh token in', min_ref_diff, 'mins')

            if ('refresh_token' in token):

                def refresh_callback():
                    try:
                        print("Refresh callback")
                        form_data = {}
                        form_data['grant_type'] = 'refresh_token'
                        form_data['refresh_token'] = token['refresh_token']
                        url = "{}/api/users/login".format(
                            self.__app_config['api_url'])
                        resp = requests.post(url, data=form_data)
                        if (resp.status_code >= 200
                                and resp.status_code < 300):
                            data = resp.json()
                            self.save_token_json(data)
                            trio.run(self.check_token)
                        else:
                            self.log_out()
                    except:
                        print("Error refresh callback")
                    finally:
                        self.rf_thread.quit()
                    return

                def start_timer():
                    refresh_timer = QTimer()
                    self.rf_thread.refresh_timer = refresh_timer
                    refresh_timer.timeout.connect(refresh_callback)
                    refresh_timer.setSingleShot(True)
                    refresh_timer.start(min_ref_diff * 60 * 1000)

                self.__cancel_threads()
                self.rf_thread = FukinThread(start_timer)
                self.rf_thread.start()
            else:

                def logout_callback():
                    try:
                        self.log_out()
                    except:
                        print("Log out error")
                    finally:
                        self.lo_thread.quit()
                    return

                def start_timer():
                    logout_timer = QTimer()
                    self.lo_thread.logout_timer = logout_timer
                    logout_timer.timeout.connect(logout_callback)
                    logout_timer.setSingleShot(True)
                    logout_timer.start(min_diff * 60 * 1000)

                self.__cancel_threads()
                self.lo_thread = FukinThread(start_timer)
                self.lo_thread.start()

        return

    async def log_in(self, username, password, success=None, error=None):
        try:
            form_data = {}
            form_data['username'] = username
            form_data['password'] = password
            url = "{}/api/users/login".format(self.__app_config['api_url'])
            resp = requests.post(url, data=form_data)
            if (resp.status_code >= 200 and resp.status_code < 300):
                data = resp.json()
                self.save_token_json(data)
                await self.check_token()
                if success is not None:
                    if asyncio.iscoroutinefunction(success):
                        await success(data)
                    else:
                        success(data)
            else:
                if error is not None:
                    if asyncio.iscoroutinefunction(error): await error(resp)
                    else: error(resp)
        except Exception as ex:
            print(ex)
            if error is not None:
                if asyncio.iscoroutinefunction(error): await error(None)
                else: error(None)
        return

    def save_token_json(self, token):
        self.__auth_info.set_token_info(token)
        with open(TOKEN_PATH, 'w') as fo:
            json.dump(token, fo, indent=2)

    def log_out(self):
        self.__cancel_threads()
        if not self.__auth_info.is_logged_in(): return
        if os.path.exists(TOKEN_PATH):
            os.remove(TOKEN_PATH)
        self.__auth_info.set_token_info(None)
        return

    def __cancel_threads(self):
        if self.rf_thread is not None:
            self.rf_thread.quit()
        if self.lo_thread is not None:
            self.lo_thread.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__cancel_threads()
        return