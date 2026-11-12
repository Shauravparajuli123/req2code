class ImplementableStandard:
    def __init__(self, name):
        self.name = name
    def extendTechnologyObject(self):
        raise NotImplementedError

class Implementation:
    def __init__(self):
        pass

class Ixit:
    def __init__(self):
        pass

class TechnologyObject:
    def __init__(self, implementableStandard):
        self.implementableStandard = implementableStandard
    def implementStandard(self):
        raise NotImplementedError