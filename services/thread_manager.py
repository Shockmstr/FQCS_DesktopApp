from PySide2.QtCore import QThread
import abc


class ThreadManagerAbs(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_thread(self, th: QThread, group: str = None):
        pass

    @abc.abstractmethod
    def cancel_threads(self, th: QThread = None, group: str = None):
        pass

    @abc.abstractmethod
    def wait(self):
        pass

    @abc.abstractmethod
    def cancel_all(self):
        pass


class ThreadManager(ThreadManagerAbs):
    __instance: ThreadManagerAbs = None

    @staticmethod
    def instance():
        if (ThreadManager.__instance is None):
            ThreadManager.__instance = ThreadManager()
        return ThreadManager.__instance

    def __init__(self):
        self.threads = {None: []}
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cancel_all()
        return

    def cancel_all(self):
        for k in self.threads.keys():
            self.cancel_threads(group=k)

    def add_thread(self, th: QThread, group: str = None):
        if group not in self.threads:
            self.threads[group] = []
        self.threads[group].append(th)

        def remove_thread():
            self.threads[group].remove(th)

        th.finished.connect(remove_thread)

    def cancel_threads(self, th: QThread = None, group: str = None):
        if group not in self.threads: return
        if th is None:
            for t in self.threads[group].copy():
                t.quit()
        else:
            self.threads[group].remove(th)

    def wait(self):
        for k in self.threads.keys():
            for t in self.threads[k].copy():
                t.wait()