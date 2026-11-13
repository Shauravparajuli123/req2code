from typing import Optional

class Actor:
    pass

class Position:
    def __init__(self, role: Optional[Role] = None):
        self.role = role

class Role:
    pass
class Agent:
    def __init__(self, position: Position):
        self.position = position
    def occupiesPosition(self) -> None:
        raise NotImplementedError