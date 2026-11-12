from typing import List

class RModelElement:
    def __init__(self, kind: str):
        self.kind: str = kind
    
    def __str__(self) -> str:
        return self.kind
    
    src = 'R1'

class Schema:
    def __init__(self):
        pass
    
    src = 'R2'

class Table:
    def __init__(self):
        pass
    
    src = 'R3'

class Column:
    def __init__(self, type: str):
        self.type: str = type
    
    src = 'R4'

class Key:
    def __init__(self):
        pass
    
    src = 'R5'

class ForeignKey:
    def __init__(self):
        pass
    
    src = 'R6'
