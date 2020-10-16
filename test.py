from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets.main_window import MainWindow
import sys

def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
    
main()