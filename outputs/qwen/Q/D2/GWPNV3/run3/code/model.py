from typing import List, TypeVar, Generic, Optional

T = TypeVar('T')

class String(str):
    pass

class Net:
    def __init__(self, name: String):
        self.name = name
    def __str__(self) -> str:
        return self.name

class Place:
    def __init__(self, net: Net):
        self.net = net
    def __str__(self) -> str:
        return f'Place in {self.net}'

class Arc:
    def __init__(self, src: Transition, dst: Transition):
        self.src = src
        self.dst = dst
    def __str__(self) -> str:
        return f'Arc from {self.src} to {self.dst}'

class Model:
    def __init__(self):
        self.arcs: List[Arc] = []
    def add_arc(self, arc: Arc):
        self.arcs.append(arc)
    def __str__(self) -> str:
        return f'Model with {len(self.arcs)} arcs'

class Transition:
    def __init__(self, model: Model):
        self.model = model
    def __str__(self) -> str:
        return f'Transition in {self.model}'

class Ptarc(Generic[T]):
    def __init__(self, dst: T):
        self.dst = dst
    def __str__(self) -> str:
        return f'Ptarc to {self.dst}'

class Tparcs(Generic[T]):
    def __init__(self, src: T):
        self.src = src
    def __str__(self) -> str:
        return f'Tparcs from {self.src}'