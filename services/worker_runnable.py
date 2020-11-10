from PySide2.QtCore import QTimer, QRunnable, Signal, QObject
from app_models.app_config import AppConfig
from app import helpers


class WorkerRunnable(QRunnable, QObject):
    work_finished = Signal(object)
    work_error = Signal(Exception)

    def __init__(self, func, *args, parent=None):
        QRunnable.__init__(self)
        QObject.__init__(self, parent)
        self.__func = func
        self.__args = args

    def run(self):
        try:
            result = helpers.sync_func(self.__func, *self.__args)
            self.work_finished.emit(result)
        except Exception as ex:
            self.work_error.emit(ex)
