from typing import Optional

class Airline:
    def __init__(self, name: str):
        self.name = name
        self.operation = {}  # type: dict[Airport, OperatingCost]

class Airport:
    def __init__(self, code: str, city: str):
        self.code = code
        self.city = city

class OperatingCost:
    def __init__(self, cost: float):
        self.cost = cost

    def update_cost(self, new_cost: float) -> None:
        raise NotImplementedError

    def start_operation(self) -> None:
        raise NotImplementedError

    def stop_operation(self) -> None:
        raise NotImplementedError

    def get_cost(self) -> float:
        raise NotImplementedError