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
    src = ['R1', 'R2', 'R7', 'R11', 'R8', 'R9', 'R13']

class Place:
    def __init__(self):
        pass
    src = ['R1', 'R2', 'R7']

class Model:
    def __init__(self):
        self.nets: List[Net] = []
    def add_net(self, net: Net):
        raise NotImplementedError
    src = ['R3', 'R4']

class Arc:
    def __init__(self):
        pass
    src = ['R4']

class PTArc(Arc):
    def __init__(self):
        super().__init__()
    src = ['R5']

class TPArc(Arc):
    def __init__(self):
        super().__init__()
    src = ['R6']

class Transition:
    def __init__(self):
        pass
    src = ['R9', 'R10', 'R12', 'R13']