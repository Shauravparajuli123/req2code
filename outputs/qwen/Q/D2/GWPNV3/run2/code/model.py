from typing import List

class Net:
    def __init__(self, name: str):
        self.name = name
        self.places: List[Place] = []
        self.tpa Arcs: List[TPArc] = []
        self.transition: Transition = None
    def add_place(self, place: Place):
        raise NotImplementedError
    def add_tpa_arc(self, tpa_arc: TPArc):
        raise NotImplementedError
    def set_transition(self, transition: Transition):
        raise NotImplementedError

class Place:
    def __init__(self):
        pass
    def add_net(self, net: Net):
        raise NotImplementedError

class Model:
    def __init__(self):
        self.nets: List[Net] = []
    def add_net(self, net: Net):
        raise NotImplementedError

class Arc:
    def __init__(self):
        pass

class PTArc(Arc):
    def __init__(self):
        super().__init__()
        self.dst_transition: Transition = None

class TPArc(Arc):
    def __init__(self):
        super().__init__()
        self.src_transition: Transition = None

class Transition:
    def __init__(self):
        self.outgoing_tpa_arcs: List[TPArc] = []
