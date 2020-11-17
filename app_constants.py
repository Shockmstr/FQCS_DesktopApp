import os

KEY_AUTH_INFO = "auth_info"
TOKEN_PATH = "token.json"
DEV_TOKEN_PATH = "dev_token.json"
CONFIG_PATH = "app_config.json"
ISO_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
FOLDER_DATE_FORMAT = "%Y%m%d"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Project Root

ROLE_DEVICE = "Device"