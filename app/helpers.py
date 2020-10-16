from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


def file_chooser_open(self):
    filename, filter = QFileDialog.getOpenFileName()
    return filename


def file_chooser_save(self):
    filename, filter = QFileDialog.getSaveFileName()
    return filename
