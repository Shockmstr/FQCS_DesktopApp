from FQCS import detector
import cv2
import abc


class DetectorConfigAbs(Subject, metaclass=abc.ABCMeta):
    camera: cv2.VideoCapture
    config: dict
    current_path: str

    @abc.abstractmethod
    def load_config(self, detector_config=None):
        pass


class DetectorConfig(DetectorConfigAbs):
    __instance: DetectorConfigAbs

    def __init__(self):
        return

    def load_config(self, detector_config=None):
        if detector_config is None:
            self.config = detector.default_detector_config()
            self.current_path = None
        else:
            self.config = detector_config

    @staticmethod
    def instance() -> DetectorConfigAbs:
        if DetectorConfig.__instance == None:
            instance = DetectorConfig()
            instance.load_config()
            DetectorConfig.__instance = instance

        return DetectorConfig.__instance
