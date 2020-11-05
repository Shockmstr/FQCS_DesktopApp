from app.observer import Subject
from FQCS import detector
import cv2


class DetectorConfig(Subject):
    def __init__(self):
        super().__init__()
        self.camera: cv2.VideoCapture
        self.load_config()

    def load_config(self, detector_config=None):
        if detector_config is None:
            self.config = detector.default_detector_config()
            self.current_path = None
        else:
            self.config = detector_config


class DetectorConfigSingleton():
    __instance: DetectorConfig = None

    @staticmethod
    def get_instance():  #-> DetectorConfig:
        if DetectorConfigSingleton.__instance == None:
            DetectorConfigSingleton.__instance = DetectorConfig()
        return DetectorConfigSingleton.__instance
