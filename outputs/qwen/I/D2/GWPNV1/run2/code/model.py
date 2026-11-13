from typing import List

class Net:
    def __init__(self, places: List[Place] = []) -> None:
        self.places = places

class PetriNet:
    def __init__(self, transitions: List[Transition] = []) -> None:
        self.transitions = transitions

class Place:
    def __init__(self, destination: Transition = None) -> None:
        self.destination = destination

class Transition:
    def __init__(self, net: Net, destination: Place = None) -> None:
        self.net = net
        self.destination = destination
        self.net.has(self)

    def set_destination(self, place: Place) -> None:
        raise NotImplementedError

    def get_net(self) -> Net:
        raise NotImplementedError

class Net:
    def add_place(self, place: Place) -> None:
        raise NotImplementedError

class PetriNet:
    def add_transition(self, transition: Transition) -> None:
        raise NotImplementedError