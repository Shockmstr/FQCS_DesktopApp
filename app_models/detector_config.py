from PySide2.QtCore import Signal, QObject
from FQCS import detector
from FQCS.manager import FQCSManager
import cv2
import abc


class DetectorConfigAbs():
    current_path_changed: Signal
    manager_changed: Signal
    current_cfg_name_changed: Signal

    def get_current_path(self):
        pass

    def set_current_path(self, val):
        pass

    def get_manager(self) -> FQCSManager:
        pass

    def set_manager(self, val):
        pass

    def get_current_cfg_name(self):
        pass

    def set_current_cfg_name(self, val):
        pass

    def get_current_cfg(self):
        pass


class DetectorConfig(QObject, DetectorConfigAbs):
    current_path_changed = Signal(str)
    manager_changed = Signal(FQCSManager)
    current_cfg_name_changed = Signal(str)

    __instance: DetectorConfigAbs = None
    __current_path: str = None
    __manager: FQCSManager = None
    __current_cfg_name: str = None

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        return

    def get_current_path(self):
        return self.__current_path

    def set_current_path(self, val):
        self.__current_path = val
        self.current_path_changed.emit(val)

    def get_manager(self):
        return self.__manager

    def set_manager(self, val):
        self.__manager = val
        self.manager_changed.emit(val)

    def get_current_cfg_name(self):
        return self.__current_cfg_name

    def set_current_cfg_name(self, val):
        self.__current_cfg_name = val
        self.current_cfg_name_changed.emit(val)

    def get_current_cfg(self):
        return self.__manager.get_config_by_name(self.__current_cfg_name)

    @staticmethod
    def instance() -> DetectorConfigAbs:
        if DetectorConfig.__instance == None:
            instance = DetectorConfig()
            instance.__manager = FQCSManager()
            instance.__current_cfg_name = None
            DetectorConfig.__instance = instance

        return DetectorConfig.__instance
