class Net:
    def __init__(self, name):
        self.name = name
        self.places = []
        self.tparcs = []
        self.transitions = []

    def add_place(self, place):
        self.places.append(place)

    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_tparc(self, tparc):
        self.tparcs.append(tparc)

class Place:
    def __init__(self, name):
        self.name = name
        self.arcs = []

    def add_arc(self, arc):
        self.arcs.append(arc)

class Arc:
    def __init__(self, name, src, dst):
        self.name = name
        self.src = src
        self.dst = dst

class Model:
    def __init__(self):
        self.nets = []

    def add_net(self, net):
        self.nets.append(net)

class PTArc(Arc):
    def __init__(self, name, src, dst):
        super().__init__(name, src, dst)

class TPArc(Arc):
    def __init__(self, name, src, dst):
        super().__init__(name, src, dst)

class Transition:
    def __init__(self, name):
        self.name = name
        self.outgoing_arcs = []

    def add_outgoing_arc(self, tparc):
        self.outgoing_arcs.append(tparc)