from typing import List

class Trace:
    def __init__(self, name: str):
        self.name = name
        self.levels: List[Level] = []

    def DefineTraceName(self) -> None:
        raise NotImplementedError()

class Level:
    def __init__(self, trace: Trace):
        self.trace = trace

    def __str__(self) -> str:
        return f'Level for {self.trace.name}'

class Call:
    def __init__(self, methodName: str, databaseRow: int):
        self.methodName = methodName
        self.databaseRow = databaseRow
        self.level: Level = None

    def setLevel(self, level: Level) -> None:
        if self.level is not None:
            raise ValueError('Call already has a level')
        self.level = level

    def __str__(self) -> str:
        return f'Call to {self.methodName} with {self.databaseRow} database rows'
