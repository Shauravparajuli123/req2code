from typing import Optional

class Position:
    def __init__(self, role: Optional[str] = None):
        self.role = role

class Actor:
    pass

class Agent(Actor):
    def __init__(self, position: Position):
        self.position = position

class Role:
    pass