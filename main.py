from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets.main_window import MainWindow
from widgets.login_screen import LoginScreen
import asyncio
import sys

def main():
    app = QApplication([])
    # main_window = MainWindow()
    # main_window.show()
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()