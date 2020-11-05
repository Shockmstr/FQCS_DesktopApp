from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2
import os
from models.detector_config import DetectorConfig, DetectorConfigSingleton


def file_chooser_open_directory(self):
    dialog = QFileDialog(self)
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    filename = dialog.getExistingDirectory()
    return filename

def file_chooser_open_file(self):
    dialog = QFileDialog(self)
    filename = dialog.getOpenFileName()
    return filename

def get_all_camera_index(self):
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

def get_current_sample_image_path(self):
    currentPath = DetectorConfigSingleton.get_instance().current_path
    if (currentPath == None):
        currentPath = os.getcwd() #default = current working directory
    return currentPath