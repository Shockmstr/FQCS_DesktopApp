from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from views.progress_screen import Ui_ProgressScreen


class ProgressScreen(QWidget):
    stopped = Signal(bool)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        self.binding()

    # data binding
    def binding(self):
        self.ui.btnStop.clicked.connect(self.btn_stop_clicked)
        return

    def btn_stop_clicked(self, event: bool):
        # another logic
        self.stopped.emit(event)