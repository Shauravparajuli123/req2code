class Position:
    def __init__(self, role=None):
        self.role = role

class Agent:
    def __init__(self, position):
        self.position = position
    def occupyPosition(self):
        raise NotImplementedError

class Actor:
    pass

class Role:
    pass