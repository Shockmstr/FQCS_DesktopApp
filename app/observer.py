class Subject:
    def __init__(self):
        self.observers = {}

    def register(self, key: str, ob: (object)):
        if (key not in self.observers):
            self.observers[key] = []
        self.observers[key].append(ob)

    def unregister(self, key: str, ob: (object)):
        if (key not in self.observers):
            self.observers[key] = []
        self.observers[key].remove(ob)

    def notify(self, key: str):
        if key in self.observers:
            for ob in self.observers[key]:
                ob(self)
