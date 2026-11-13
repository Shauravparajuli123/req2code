from typing import List

class Trace:
    def __init__(self, name: str):
        self.name = name
        self.levels: List['Level'] = []

class Level:
    def __init__(self, trace: Trace, index: int):
        self.trace = trace
        self.index = index

class Call:
    def __init__(self, method_name: str, database_row: int):
        self.method_name = method_name
        self.database_row = database_row

class Index:
    def __init__(self, value: int):
        self.value = value