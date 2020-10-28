from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from views.image_widget import Ui_ImageWidget


class ImageWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_ImageWidget()
        self.ui.setupUi(self)

    def imshow(self, image):
        length = image.shape[2] if len(image.shape) > 2 else 1
        imformat = QImage.Format_Grayscale8 if length == 1 else QImage.Format_RGB888 
        image = QImage(image.data, image.shape[1], image.shape[0], length * image.shape[1],
                             imformat).rgbSwapped() # 1: width, 0:height, 2:channel
        self.ui.lblImage.setPixmap(QPixmap.fromImage(image))

