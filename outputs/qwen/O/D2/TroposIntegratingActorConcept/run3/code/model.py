class Actor:
    pass

class Agent:
    def __init__(self, position=None):
        self.position = position
    def occupies_position(self):
        raise NotImplementedError

class Position:
    def __init__(self, role=None):
        self.role = role

class Role:
    pass