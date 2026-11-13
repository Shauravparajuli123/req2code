from abc import ABC

class ImplementableStandard(ABC):
    pass

class Implementation(IXIT):
    def __init__(self):
        self.ixin = []

    def add_ixin(self, ixin):
        raise NotImplementedError

class IXIT(Implementation):
    pass

class TechnologyObject(ImplementableStandard):
    def __init__(self):
        self.implementable_standards = []

    def add_implementable_standard(self, standard):
        raise NotImplementedError
