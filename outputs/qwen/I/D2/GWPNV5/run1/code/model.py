from typing import List, Optional

class Arc:
    def __init__(self, source: 'Place', destination: 'Transition', weight: Optional[Weight] = None):
        self.source = source
        self.destination = destination
        self.weight = weight

class Net:
    def __init__(self):
        self.places = []
        self.transitions = []

class PetriNet(Net):
    def __init__(self):
        super().__init__()
        self.places = []
        self.transitions = []

class Place:
    def __init__(self, net: PetriNet):
        self.net = net
        self.input_arcs = []

class Transition:
    def __init__(self, net: PetriNet):
        self.net = net
        self.output_arcs = []

class PlaceTransitionArc(Arc):
    def __init__(self, transition: Transition, destination: Place, weight: Optional[Weight] = None):
        super().__init__(source=transition, destination=destination, weight=weight)

class TransitionPlaceArc(Arc):
    def __init__(self, source: Transition, place: Place, weight: Optional[Weight] = None):
        super().__init__(source=source, destination=place, weight=weight)

class Weight:
    pass
