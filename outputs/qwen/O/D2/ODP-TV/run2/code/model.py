class ImplementableStandard:
    def __init__(self, name):
        self.name = name
    def extendTechnologyObject(self):
        raise NotImplementedError

class Implementation:
    def __init__(self):
        pass

class IXIT:
    def __init__(self):
        pass

class TechnologyObject:
    def __init__(self, implementableStandard):
        self.implementableStandard = implementableStandard
    def implement(self):
        raise NotImplementedError