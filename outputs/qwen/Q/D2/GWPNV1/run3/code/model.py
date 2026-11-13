from typing import List

class Place:
    def __init__(self, name: str):
        self.name = name
        self.transitions: List[Transition] = []

    def addTransition(self, transition: Transition) -> None:
        raise NotImplementedError

class Transition:
    def __init__(self, name: str):
        self.name = name
        self.net: Net = None

    def setNet(self, net: Net) -> None:
        raise NotImplementedError

class PetriNet:
    def __init__(self):
        pass

class Net:
    def __init__(self):
        pass