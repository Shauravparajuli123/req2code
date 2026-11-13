from abc import ABC

class ImplementableStandard(ABC):
    pass

class Implementation(IXIT):
    def __init__(self):
        self.xit_list = []

class IXIT(Implementation):
    pass

class TechnologyObject(ImplementableStandard):
    def __init__(self):
        self.implementable_standard_list = []

    def add_implementable_standard(self, standard: ImplementableStandard):
        raise NotImplementedError

    def remove_implementable_standard(self, standard: ImplementableStandard):
        raise NotImplementedError
