from typing import List, Weight

class Net:
    def __init__(self, name: str):
        self.name = name
        self.places: List[Place] = []
        self.transitions: List[Transition] = []
        self.arcs: List[Arc] = []
        self.place_transition_arcs: List[PlaceTransitionArc] = []

    def definePetriNet(self):
        raise NotImplementedError

    def addPlace(self, place: Place):
        raise NotImplementedError

    def addTransition(self, transition: Transition):
        raise NotImplementedError

    def createArc(self, arc: Arc):
        raise NotImplementedError

    def associateToken(self, token: Token):
        raise NotImplementedError

class Place:
    def __init__(self, tokens: List[Token] = []):
        self.tokens: List[Token] = tokens

class Transition:
    pass

class Arc:
    def __init__(self, weight: Weight):
        self.weight: Weight = weight

class PlaceTransitionArc:
    pass

class Token:
    pass

class Weight:
    pass