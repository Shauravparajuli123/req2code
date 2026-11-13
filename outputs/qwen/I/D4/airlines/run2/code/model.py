from typing import Optional

class OperatingCost:
    def __init__(self, cost: float):
        self.cost = cost

class Airline:
    def __init__(self, name: str):
        self.name = name
        self.operation = {}  # type: dict[Airport, OperatingCost]

class Airport:
    def __init__(self, code: str, city: str):
        self.code = code
        self.city = city

def start_operation(airline: Airline, airport: Airport, cost: float):
    raise NotImplementedError

def stop_operation(airline: Airline, airport: Airport):
    raise NotImplementedError

def update_cost(airline: Airline, airport: Airport, new_cost: float):
    raise NotImplementedError