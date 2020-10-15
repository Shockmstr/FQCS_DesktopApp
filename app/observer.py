class Subject:
    def __init__(self):
        self.observers = []

    def register(self, ob: (object)):
        self.observers.append(ob)

    def unregister(self, ob: (object)):
        self.observers.remove(ob) 

    def notify(self):
        for ob in self.observers:
            ob(self)       