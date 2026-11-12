from typing import List

class Net:
    def __init__(self):
        self.places: List[Place] = []
        self.tokens: List[Token] = []
        self.arc: List[Arc] = []

    def add_place(self, place: Place):
        self.places.append(place)

    def add_token(self, token: Token):
        self.tokens.append(token)

    def add_arc(self, arc: Arc):
        self.arc.append(arc)

    def __str__(self):
        return f'Net with {len(self.places)} places and {len(self.tokens)} tokens'

    src: List[str] = ['R3', 'R7', 'R8', 'R12']

class Place:
    def __init__(self, name: str):
        self.name: str = name
        self.inputArcs: List[Arc] = []
        self.outputArcs: List[Arc] = []

    def add_input_arc(self, arc: Arc):
        self.inputArcs.append(arc)

    def add_output_arc(self, arc: Arc):
        self.outputArcs.append(arc)

    def __str__(self):
        return f'Place {self.name} with {len(self.inputArcs)} input arcs and {len(self.outputArcs)} output arcs'

    src: List[str] = ['R1', 'R9', 'R11']

class Arc:
    def __init__(self, weight: float):
        self.weight: float = weight

    def __str__(self):
        return f'Arc with weight {self.weight}'

    src: List[str] = ['R4']

class Transition:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return f'Transition {self.name}'

    src: List[str] = ['R2', 'R10']

class PlaceTransitionArc:
    def __init__(self, transition: Transition):
        self.transition: Transition = transition

    def __str__(self):
        return f'PlaceTransitionArc to {self.transition.name}'

    src: List[str] = ['R5', 'R6', 'R13', 'R14']

class Token:
    def __init__(self):
        pass

    def __str__(self):
        return 'Token'

    src: List[str] = ['R7', 'R15']
