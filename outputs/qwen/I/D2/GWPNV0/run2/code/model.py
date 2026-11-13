from typing import List, Optional

class Concept:
    pass

class Net(Concept):
    pass

class Network(Concept):
    def __init__(self, nets: List[Net]):
        self.nets = nets

class PetriNet(Network):
    def __init__(self, nets: List[Net], places: List[Place], transitions: List[Transition]):
        self.nets = nets
        self.places = places
        self.transitions = transitions

class Place(Concept):
    def __init__(self, destination: Optional[Place] = None):
        self.destination = destination

class Transition(Concept):
    def __init__(self, destination: Place):
        self.destination = destination
