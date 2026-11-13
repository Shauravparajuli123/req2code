from typing import List

class Place:
    def __init__(self):
        self.destination: Transition = None

    def addDestination(self, destination: Transition) -> None:
        raise NotImplementedError()

class Transition:
    def __init__(self):
        self.net: Net = None
        self.destinationPlace: Place = None

    def setNet(self, net: Net) -> None:
        raise NotImplementedError()

    def setDestinationPlace(self, destinationPlace: Place) -> None:
        raise NotImplementedError()

class Net:
    pass

class PetriNet:
    pass