from typing import List

class RmodelElement:
    def __init__(self, kind: str):
        self.kind: str = kind
    
    def __str__(self) -> str:
        return self.kind
    
    def __repr__(self) -> str:
        return self.__str__()
    
    src = 'R1'

class Schema:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'Schema'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    src = 'R2'

class Table:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'Table'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    src = 'R3'

class Column:
    def __init__(self, type: str):
        self.type: str = type
    
    def __str__(self) -> str:
        return self.type
    
    def __repr__(self) -> str:
        return self.__str__()
    
    src = 'R4'

class Key:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'Key'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    src = 'R5'

class ForeignKey:
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return 'ForeignKey'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    src = 'R6'
