from typing import List

class Trace:
    def __init__(self, name: str):
        self.name = name
        self.levels: List[Level] = []

    def DefineTraceName(self, name: str):
        raise NotImplementedError

    def add_level(self, level: Level):
        self.levels.append(level)

class Level:
    def __init__(self, trace: Trace):
        self.trace = trace

class Call:
    def __init__(self, method_name: str, database_row: int):
        self.methodName = method_name
        self.databaseRow = database_row