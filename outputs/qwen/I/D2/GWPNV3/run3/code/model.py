from typing import List

class Arc:
    pass
class Model:
    def __init__(self):
        self.arcs: List[Arc] = []
        self.nets: List[Net] = []
class Net:
    def __init__(self):
        self.places: List[Place] = []
        self.tparcs: List[TPArc] = []
        self.transitions: List[Transition] = []
class Place:
    def __init__(self, net: Net):
        self.net: Net = net
class PtArc:
    pass
class TPArc:
    def __init__(self, src: Transition, dst: Transition):
        self.src: Transition = src
        self.dst: Transition = dst
class Transition:
    def __init__(self):
        self.outgoing_tparcs: List[TPArc] = []
        self.net: Net = None

class Model:
    def __init__(self):
        self.arcs: List[Arc] = []
        self.nets: List[Net] = []

class Net:
    def __init__(self):
        self.places: List[Place] = []
        self.tparcs: List[TPArc] = []
        self.transitions: List[Transition] = []

class Place:
    def __init__(self, net: Net):
        self.net: Net = net

class PtArc:
    pass
class TPArc:
    def __init__(self, src: Transition, dst: Transition):
        self.src: Transition = src
        self.dst: Transition = dst
class Transition:
    def __init__(self):
        self.outgoing_tparcs: List[TPArc] = []
        self.net: Net = None
