from FQCS import detector
from FQCS.manager import FQCSManager
import cv2
import abc


class DetectorConfigAbs(metaclass=abc.ABCMeta):
    camera: cv2.VideoCapture
    current_path: str
    manager: FQCSManager


class DetectorConfig(DetectorConfigAbs):
    __instance: DetectorConfigAbs = None

    def __init__(self):
        return

    @staticmethod
    def instance() -> DetectorConfigAbs:
        if DetectorConfig.__instance == None:
            instance = DetectorConfig()
            instance.manager = FQCSManager()
            DetectorConfig.__instance = instance

        return DetectorConfig.__instance
