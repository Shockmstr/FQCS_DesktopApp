import abc
from app_constants import CONFIG_PATH
import json

class AppConfigAbs(metaclass=abc.ABCMeta):
    config: dict

    @abc.abstractmethod
    def load_config(self):
        pass


class AppConfig(AppConfigAbs):
    __instance: AppConfigAbs = None

    def __init__(self):
        return

    def load_config(self):
        with open(CONFIG_PATH) as fi:
            self.config = json.load(fi)

    @staticmethod
    def instance() -> AppConfigAbs:
        if AppConfig.__instance == None:
            instance = AppConfig()
            AppConfig.__instance = instance

        return AppConfig.__instance
