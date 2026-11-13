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
    def __init__(self, source: Place, destination: Transition):
        super().__init__(source, destination)

class TransitionPlaceArc(Arc):
    def __init__(self, source: Transition, destination: Place):
        super().__init__(source, destination)

class Weight:
    pass
