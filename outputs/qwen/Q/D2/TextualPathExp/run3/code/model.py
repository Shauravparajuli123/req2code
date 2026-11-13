from typing import List

class Transition:
    def __init__(self, name: str):
        self.name = name

class Path:
    def __init__(self, transitions: List[Transition]):
        self.transitions = transitions

class AlternativeTrans:
    def __init__(self):
        pass

class TextualPathExp:
    def __init__(self, path: Path):
        self.path = path
        if path.transitions is None or len(path.transitions) == 0:
            raise ValueError('A path must contain at least one transition.')
