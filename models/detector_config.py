from app.observer import Subject
from FQCS import detector

KEY_VIDEO = "video"


class DetectorConfig(Subject):
    @staticmethod
    def get_instance(): #-> DetectorConfig:
        if DetectorConfig.__instance == None:
            DetectorConfig()
        return DetectorConfig.__instance

    def __init__(self):
        self.camera = None
        if DetectorConfig.__instance != None:
            raise Exception("DetectorConfig class is a singleton")
        else:
            DetectorConfig.__instance = self
            self.load_config()

    def load_config(self, detector_config=None):
        if detector_config is None:
            self.config = detector.default_detector_config()
        else:
            self.config = detector_config

