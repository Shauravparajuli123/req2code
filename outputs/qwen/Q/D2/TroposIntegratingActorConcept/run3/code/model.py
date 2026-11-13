from typing import Optional

class Actor:
    pass

class Agent:
    def __init__(self, position: Position):
        self.position = position
    def occupyPosition(self) -> None:
        raise NotImplementedError

class Position:
    def __init__(self, role: Optional[Role] = None):
        self.role = role

class Role:
    pass