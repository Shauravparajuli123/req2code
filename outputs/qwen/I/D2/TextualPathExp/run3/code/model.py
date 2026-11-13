from typing import List

class String:
    pass

class AlternativeTrans:
    def __init__(self, name: String):
        self.name = name

class Transition:
    pass

class Path:
    def __init__(self, transitions: List[Transition]):
        self.transitions = transitions

class Paths:
    pass

class TextualPathExp:
    def __init__(self, path: Path):
        self.path = path

class String:
    pass