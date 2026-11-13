from typing import List

class Transition:
    def __init__(self, name: str):
        self.name = name

class Path:
    def __init__(self):
        self.transitions: List[Transition] = []
    def add_transition(self, transition: Transition):
        self.transitions.append(transition)

class AlternativeTrans:
    def __init__(self):
        self.transitions: List[Transition] = []
    def add_transition(self, transition: Transition):
        self.transitions.append(transition)

class TextualPathExp:
    def __init__(self):
        self.path: Path = Path()
    def get_path(self) -> Path:
        return self.path
