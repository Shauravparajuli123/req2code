from typing import List

class RmodelElement:
    def __init__(self, kind: str):
        self.kind: str = kind
    
    def __str__(self) -> str:
        return self.kind
    
    def __repr__(self) -> str:
        return f'RmodelElement(kind={self.kind!r})'
    
    src: List[str] = ['R1']

class Schema:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'Schema()'
    
    def __repr__(self) -> str:
        return 'Schema()'
    
    src: List[str] = ['R2']

class Table:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'Table()'
    
    def __repr__(self) -> str:
        return 'Table()'
    
    src: List[str] = ['R3', 'R7', 'R8']

class Column:
    def __init__(self, type: str):
        self.type: str = type
    
    def __str__(self) -> str:
        return f'Column(type={self.type!r})'
    
    def __repr__(self) -> str:
        return f'Column(type={self.type!r})'
    
    src: List[str] = ['R4', 'R10', 'R11']

class Key:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'Key()'
    
    def __repr__(self) -> str:
        return 'Key()'
    
    src: List[str] = ['R5', 'R9', 'R12']

class ForeignKey:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'ForeignKey()'
    
    def __repr__(self) -> str:
        return 'ForeignKey()'
    
    src: List[str] = ['R6', 'R13', 'R14', 'R15']
