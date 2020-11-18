import os

KEY_AUTH_INFO = "auth_info"
TOKEN_PATH = "token.json"
DEV_TOKEN_PATH = "dev_token.json"
CONFIG_PATH = "app_config.json"
ISO_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
FOLDER_DATE_FORMAT = "%Y%m%d"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Project Root

ROLE_DEVICE = "Device"


# test only
class Videos():
    __instance = None

    def __init__(self):
        self.__clips = [
            "./data/videos/sam1.avi",
            "./data/videos/sam2.avi",
            "./data/videos/stain1.avi",
            "./data/videos/sam3.avi",
            "./data/videos/stain3.avi",
            "./data/videos/sam4.avi",
            "./data/videos/stain4.avi",
            "./data/videos/sam5.avi",
            "./data/videos/stain2.avi",
            "./data/videos/stain5.avi",
        ]
        self.__last_idx = 0

    def next(self):
        vid = self.__clips[self.__last_idx]
        if self.__last_idx + 1 == len(self.__clips):
            self.__last_idx = 0
        else:
            self.__last_idx += 1
        return vid

    @staticmethod
    def instance():
        if Videos.__instance == None:
            instance = Videos()
            Videos.__instance = instance
        return Videos.__instance
