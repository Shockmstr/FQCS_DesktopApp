from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2


def file_chooser_open_directory(self):
    dialog = QFileDialog(self)
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    filename = dialog.getExistingDirectory()
    print(filename)
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