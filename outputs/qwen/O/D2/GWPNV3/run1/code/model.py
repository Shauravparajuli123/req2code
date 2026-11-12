class Net:
    def __init__(self, name):
        self.name = name
        self.places = []
        self.arcs = []
    def add_place(self, place):
        self.places.append(place)
    def add_arc(self, arc):
        self.arcs.append(arc)

class Place:
    def __init__(self, name):
        self.name = name
        self.arcs = []
    def add_arc(self, arc):
        self.arcs.append(arc)

class Arc:
    def __init__(self, name):
        self.name = name
        self.src = None
        self.dst = None
    def src(self):
        raise NotImplementedError
    def dst(self):
        raise NotImplementedError

class Model:
    def __init__(self):
        self.nets = []
    def add_net(self, net):
        self.nets.append(net)

class Transition:
    def __init__(self, name):
        self.name = name
        self.outgoing_arcs = []
    def add_outgoing_arc(self, arc):
        self.outgoing_arcs.append(arc)

class PTArc(Arc):
    def __init__(self, name):
        super().__init__(name)

class TPArc(Arc):
    def __init__(self, name):
        super().__init__(name)
