from PySide2.QtCore import QThread, Signal
import trio
import asyncio


class FukinThread(QThread):

    func_excuted_err = Signal(Exception)
    func_excuted = Signal()

    def __init__(self, func, *args, parent=None):
        QThread.__init__(self, parent)
        self.__func = func
        self.__args = args

    def run(self):
        print("Start thread")
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
            self.func_excuted.emit()
        except Exception as ex:
            self.func_excuted_err.emit(ex)
        self.exec_()
        print("End thread")
