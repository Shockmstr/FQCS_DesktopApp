from FQCS import detector
from FQCS.manager import FQCSManager
import cv2
import abc


class DetectorConfigAbs(metaclass=abc.ABCMeta):
    current_path: str
    manager: FQCSManager
    current_cfg_name: str

    @abc.abstractmethod
    def get_current_cfg(self):
        pass


class DetectorConfig(DetectorConfigAbs):
    __instance: DetectorConfigAbs = None

    def __init__(self):
        return

    def get_current_cfg(self):
        return self.manager.get_config_by_name(self.current_cfg_name)

    @staticmethod
    def instance() -> DetectorConfigAbs:
        if DetectorConfig.__instance == None:
            instance = DetectorConfig()
            instance.manager = FQCSManager()
            instance.current_cfg_name = None
            DetectorConfig.__instance = instance

        return DetectorConfig.__instance
