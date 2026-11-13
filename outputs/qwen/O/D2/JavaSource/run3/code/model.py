class Definition:
    def __init__(self, name):
        self.name = name
    def invokeMethod(self):
        raise NotImplementedError

class MethodDefinition:
    pass
class Method:
    def __init__(self, definition, method_definition):
        self.definition = definition
        self.method_definition = method_definition
    def invoke(self):
        raise NotImplementedError