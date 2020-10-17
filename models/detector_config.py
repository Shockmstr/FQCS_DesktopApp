from app.observer import Subject
from FQCS import detector


class DetectorConfig(Subject):
    __instance = None

    @staticmethod 
    def get_instance():
        if DetectorConfig.__instance == None:
            DetectorConfig()
        return DetectorConfig.__instance

    def __init__(self):
        if DetectorConfig.__instance != None:
            raise Exception("DetectorConfig class is a singleton")
        else:
            DetectorConfig.__instance = self
            self.load_config()

    def load_config(self, detector_config = None):
        if detector_config is None:
            self.config = detector.default_detector_config()
        else:
            self.config = detector_config
