class Arc:
    def __init__(self, source: Place, destination: Transition, weight: Weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def set_weight(self, weight: Weight):
        raise NotImplementedError

class Net:
    def __init__(self):
        self.places = []
        self.transitions = []

    def add_place(self, place: Place):
        raise NotImplementedError

    def add_transition(self, transition: Transition):
        raise NotImplementedError

class Place:
    def __init__(self, net: Net):
        self.net = net
        self.input_arcs = []

    def add_input_arc(self, arc: Arc):
        raise NotImplementedError

class PlaceTransitionArc:
    def __init__(self, transition: Transition):
        self.transition = transition

    def set_transition(self, transition: Transition):
        raise NotImplementedError

class Transition:
    def __init__(self, net: Net):
        self.net = net
        self.output_arcs = []

    def add_output_arc(self, arc: Arc):
        raise NotImplementedError

class Weight:
    pass