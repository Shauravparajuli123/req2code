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
    def __init__(self, net: Net, destination_places: List[Place] = []) -> None:
        self.net = net
        self.destination_places = destination_places
        if not self.net.transitions or self.net.transitions[0] != self:
            raise ValueError('A transition has exactly one net and vice versa.')
        if not self.destination_places:
            raise ValueError('A transition has at least one destination place.')
