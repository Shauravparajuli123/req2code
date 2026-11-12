class Definition:
    def __init__(self, name):
        self.name = name

    def invokeMethod(self):
        raise NotImplementedError

class MethodDefinition:
    pass