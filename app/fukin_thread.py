from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import trio
import asyncio


class FukinThread(QThread):
    def __init__(self, func, *args, parent=None):
        QThread.__init__(self, parent)
        self.__func = func
        self.__args = args
        self.error_signal = Signal(Exception, "error_signal")
        self.finish_signal = Signal("finish_signal")

    def run(self):
        try:
            if (len(self.__args) > 0):
                if asyncio.iscoroutinefunction(self.__func):
                    trio.run(self.__func, self.__args)
                else:
                    self.__func(self.__args)
            else:
                if asyncio.iscoroutinefunction(self.__func):
                    trio.run(self.__func)
                else:
                    self.__func()
            self.finish_signal.emit()
        except Exception as ex:
            self.error_signal.emit(ex)
