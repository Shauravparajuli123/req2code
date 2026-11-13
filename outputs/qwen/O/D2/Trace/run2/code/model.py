class Trace:
    def __init__(self, name):
        self.name = name
        self.levels = []
    def addLevel(self):
        raise NotImplementedError

class Level:
    def __init__(self):
        pass
    def call(self, methodName, databaseRow):
        raise NotImplementedError
class Call:
    def __init__(self, methodName, databaseRow):
        self.methodName = methodName
        self.databaseRow = databaseRow