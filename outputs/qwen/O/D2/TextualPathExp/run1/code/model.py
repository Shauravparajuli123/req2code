class AlternativeTrans:
    def __init__(self):
        self.transitions = []
    def add_transition(self, transition):
        self.transitions.append(transition)

class Path:
    def __init__(self):
        self.transitions = []
    def add_transition(self, transition):
        self.transitions.append(transition)

class TextualPathExp:
    def __init__(self, path):
        self.path = path

class Transition:
    def __init__(self, name):
        self.name = name