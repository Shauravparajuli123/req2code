class Trace:
    def __init__(self, name):
        self.name = name

class Level:
    def __init__(self, trace):
        self.trace = trace

class Call:
    def __init__(self, methodName, databaseRows):
        self.methodName = methodName
        self.databaseRows = databaseRows
    def verbObject(self):
        raise NotImplementedError