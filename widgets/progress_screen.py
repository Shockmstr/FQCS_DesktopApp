from PySide2.QtGui import QMouseEvent
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from views.progress_screen import Ui_ProgressScreen


class ProgressScreen(QWidget):
    stopped = Signal(QMouseEvent)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ProgressScreen()
        self.ui.setupUi(self)
        self.binding()

    # data binding
    def binding(self):
        self.ui.btnStop.clicked.connect(self.btn_stop_clicked)
        return

    def btn_stop_clicked(self, event: QMouseEvent):
        # another logic
        self.stopped.emit(event)