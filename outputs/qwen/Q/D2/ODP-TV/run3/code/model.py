from abc import ABC, abstractmethod

class TechnologyObject:
    def __init__(self):
        pass
    @abstractmethod
def CreateTechnologyObject(self):
        raise NotImplementedError

class ImplementableStandard(ABC):
    pass

class Implementation:
    pass

class IXIT:
    pass

TechnologyObject.__bases__ = (ImplementableStandard,)
Implementation.__bases__ = (IXIT,)
IXIT.__bases__ = (Implementation,)
ImplementableStandard.__bases__ = (TechnologyObject,)