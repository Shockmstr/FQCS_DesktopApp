from PySide2.QtCore import Signal, QObject, QTimer
from FQCS import detector
from FQCS.manager import FQCSManager
import cv2
import abc


class DetectorConfigAbs():
    manager_changed: Signal

    def get_timer(self):
        pass

    def release_cameras(self):
        pass

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

    def reset(self):
        pass

    def validate_config_name(self, camera_name):
        pass

    def get_last_camera_uri(self):
        pass

    def set_last_camera_uri(self, val):
        pass


class DetectorConfig(QObject, DetectorConfigAbs):
    manager_changed = Signal()

    __instance: DetectorConfigAbs = None
    __current_path: str = None
    __manager: FQCSManager = None
    __current_cfg_name: str = None
    __video_cameras = []
    __camera_timer: QTimer
    __last_camera_uri = None

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.__camera_timer = QTimer(self)
        return

    def set_last_camera_uri(self, val):
        self.__last_camera_uri = val

    def get_last_camera_uri(self):
        return self.__last_camera_uri

    def get_timer(self):
        return self.__camera_timer

    def release_cameras(self):
        for vid in self.__video_cameras:
            vid.release()

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

    def get_manager(self):
        return self.__manager

    def set_manager(self, val):
        self.__manager = val
        for cfg in self.__manager.get_configs():
            self.__add_camera(cfg)

    def get_current_cfg_name(self):
        return self.__current_cfg_name

    def set_current_cfg_name(self, val):
        self.__current_cfg_name = val

    def get_current_cfg(self):
        idx, cfg = self.__manager.get_config_by_name(self.__current_cfg_name)
        return idx, cfg

    def __add_camera(self, cfg):
        vid = cv2.VideoCapture()
        self.__video_cameras.append(vid)

    def add_config(self, new_cfg):
        self.__add_camera(new_cfg)
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
        self.release_cameras()
        self.__video_cameras = []
        self.__last_camera_uri = None

    def validate_config_name(self, camera_name):
        err_text = None
        if camera_name is None or camera_name == "":
            err_text = "Invalid name"
        else:
            idx, existed_cfg = self.__manager.get_config_by_name(camera_name)
            if existed_cfg is not None:
                err_text = "Name existed"
        return err_text

    @staticmethod
    def instance() -> DetectorConfigAbs:
        if DetectorConfig.__instance == None:
            instance = DetectorConfig()
            instance.reset()
            DetectorConfig.__instance = instance

        return DetectorConfig.__instance
