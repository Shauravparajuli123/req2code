from typing import List

class Net:
    def __init__(self):
        pass
    def hasNet(self) -> bool:
        raise NotImplementedError
    def hasPlace(self) -> bool:
        raise NotImplementedError
    src = ['R3', 'R8']

class PetriNet:
    def __init__(self):
        pass
    def hasTransition(self, transition) -> bool:
        raise NotImplementedError
    src = ['R2']

class Place:
    def __init__(self):
        pass
    def hasTransition(self, transition) -> bool:
        raise NotImplementedError
    src = ['R4', 'R5']

class Transition:
    def __init__(self):
        pass
    def hasNet(self) -> bool:
        raise NotImplementedError
    def hasDestinationPlace(self) -> bool:
        raise NotImplementedError
    src = ['R6', 'R7']