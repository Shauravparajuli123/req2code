class Net:
    def __init__(self, name):
        self.name = name
        self.places = []
        self.transitions = []
    def add_place(self, place):
        self.places.append(place)
    def add_transition(self, transition):
        self.transitions.append(transition)

class Place:
    def __init__(self, name):
        self.name = name
        self.arcs = []
    def add_arc(self, arc):
        self.arcs.append(arc)

class Transition:
    def __init__(self, name):
        self.name = name
        self.outgoing_arcs = []
    def add_outgoing_arc(self, arc):
        self.outgoing_arcs.append(arc)

class Model:
    def __init__(self):
        self.nets = []
    def add_net(self, net):
        self.nets.append(net)

class Arc:
    def __init__(self, name):
        self.name = name

class Ptarc(Arc):
    pass

class Tparcs(Arc):
    pass