from typing import List

class Net:
    def __init__(self):
        self.places: List[Place] = []
        self.tokens: List[Token] = []
    def add_place(self, place: Place):
        raise NotImplementedError
    def add_token(self, token: Token):
        raise NotImplementedError
    src = ['R1', 'R3', 'R7', 'R8', 'R12']

class Place:
    def __init__(self, name: str):
        self.name: str = name
        self.inputArcs: List[Arc] = []
        self.outputArcs: List[Arc] = []
    def add_input_arc(self, arc: Arc):
        raise NotImplementedError
    def add_output_arc(self, arc: Arc):
        raise NotImplementedError
    src = ['R1', 'R9']

class Arc:
    def __init__(self, weight: Weight):
        self.weight: Weight = weight
    src = ['R4']

class Transition:
    def __init__(self, name: str):
        self.name: str = name
    src = ['R2', 'R10']

class PlaceTransitionArc:
    def __init__(self, transition: Transition):
        self.transition: Transition = transition
    src = ['R5', 'R6', 'R13', 'R14']

class Token:
    def __init__(self):
        pass
    src = ['R7', 'R15']

class Weight:
    def __init__(self):
        pass
    src = ['R4']