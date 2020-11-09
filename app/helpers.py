from PySide2.QtWidgets import QFileDialog
import cv2
import os
from app_models.detector_config import DetectorConfig
from app_constants import ROOT_DIR
import trio
import asyncio


def sync_func(func, args):
    if asyncio.iscoroutinefunction(func):
        if (len(args) > 0):
            return trio.run(func, *args)
        else:
            return trio.run(func)
    else:
        if (len(args) > 0):
            return func(*args)
        else:
            return func()


def file_chooser_open_directory(parent):
    dialog = QFileDialog(parent)
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    filename = dialog.getExistingDirectory()
    return filename


def file_chooser_open_file(parent):
    dialog = QFileDialog(parent)
    filename = dialog.getOpenFileName()
    return filename


def get_all_camera_index(num=10):
    # checks the first 10 indexes.
    index = 0
    arr = []
    while num > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        num -= 1
    return arr

def get_current_sample_image_path(self):
    currentPath = DetectorConfig.instance().current_path
    if (currentPath == None):
        currentPath = os.sep.join([ROOT_DIR, "resources"])  #default = current working directory/resouces
    return currentPath
