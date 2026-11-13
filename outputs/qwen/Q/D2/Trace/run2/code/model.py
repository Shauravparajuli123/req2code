from typing import List

class Trace:
    def __init__(self, name: str):
        self.name = name
        self.levels: List[Level] = []

    def add_level(self, level: Level):
        raise NotImplementedError

    def remove_level(self, level: Level):
        raise NotImplementedError

    def get_levels(self) -> List[Level]:
        raise NotImplementedError

    src = ['R1', 'R5', 'R6']

class Level:
    def __init__(self, trace: Trace):
        self.trace = trace

    def get_trace(self) -> Trace:
        raise NotImplementedError

    src = ['R2', 'R6']

class Call:
    def __init__(self, method_name: str, database_rows: int):
        self.method_name = method_name
        self.database_rows = database_rows

    def get_method_name(self) -> str:
        raise NotImplementedError

    def get_database_rows(self) -> int:
        raise NotImplementedError

    def set_database_rows(self, database_rows: int):
        raise NotImplementedError

    src = ['R3']