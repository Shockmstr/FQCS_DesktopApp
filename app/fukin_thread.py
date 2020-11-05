from PySide2.QtCore import QThread, Signal
import trio
import asyncio
from app import helpers


class FukinThread(QThread):

    func_executed_err = Signal(Exception)
    func_executed = Signal(object)

    def __init__(self, func, *args, parent=None):
        QThread.__init__(self, parent)
        self.__func = func
        self.__args = (self) + args

    def run(self):
        print("Start thread")
        try:
            result = helpers.sync_func(self.__func, self.__args)
            self.func_executed.emit(result)
        except Exception as ex:
            self.func_executed_err.emit(ex)
        self.exec_()
        print("End thread")
