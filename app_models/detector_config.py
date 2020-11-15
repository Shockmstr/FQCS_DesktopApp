from PySide2.QtCore import Signal, QObject
from FQCS import detector
from FQCS.manager import FQCSManager
import cv2
import abc


class DetectorConfigAbs():
    current_path_changed: Signal
    manager_changed: Signal
    current_cfg_name_changed: Signal

    def add_config(self, new_cfg):
        pass

    def remove_config(self, cfg):
        pass

    def get_video_cameras(self):
        pass

    def get_current_camera(self):
        pass

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
    __video_cameras = []

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        return

    def get_video_cameras(self):
        return self.__video_cameras.copy()

    def get_current_camera(self):
        idx, cfg = self.get_current_cfg()
        if idx is not None:
            return self.__video_cameras[idx]
        return None

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
        idx, cfg = self.__manager.get_config_by_name(self.__current_cfg_name)
        return idx, cfg

    def add_config(self, new_cfg):
        vid = cv2.VideoCapture()
        camera_uri = new_cfg["camera_uri"]
        if camera_uri is not None and camera_uri != -1:
            vid.open(camera_uri)
        self.__video_cameras.append(vid)
        self.__manager.add_config(new_cfg)

    def remove_config(self, cfg):
        idx, cfg = self.__manager.get_config_by_name(cfg["name"])
        self.__video_cameras[idx].release()
        self.__video_cameras.remove(self.__video_cameras[idx])
        self.__manager.remove_config(cfg)

    def reset(self):
        self.__manager = FQCSManager()
        self.__current_cfg_name = None
        self.__current_path = None

    @staticmethod
    def instance() -> DetectorConfigAbs:
        if DetectorConfig.__instance == None:
            instance = DetectorConfig()
            instance.reset()
            DetectorConfig.__instance = instance

        return DetectorConfig.__instance
