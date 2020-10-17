from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


def file_chooser_open_directory(self):
    dialog = QFileDialog(self)
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    filename = dialog.getExistingDirectory()
    print(filename)
    return filename
