class Actor:
    pass

class Association:
    pass

class CaseContainer:
    pass

class Extend:
    def extend(self):
        raise NotImplementedError

class UseCase:
    def __init__(self, name):
        self.name = name
    def include(self):
        raise NotImplementedError
    def extend(self):
        raise NotImplementedError

class UseCaseDiagram:
    def __init__(self, name):
        self.name = name
    def has(self, association):
        raise NotImplementedError
    def has(self, actor):
        raise NotImplementedError
