from typing import List

class OperatingCost:
    pass

class Airport:
    def __init__(self, code: str, city: str):
        self.code = code
        self.city = city

class Operation:
    def __init__(self, airline: Airline, airport: Airport, cost: OperatingCost):
        self.airline = airline
        self.airport = airport
        self.cost = cost
    def start(self):
        raise NotImplementedError
    def stop(self):
        raise NotImplementedError

class Airline:
    def __init__(self, name: str):
        self.name = name
        self.operations: List[Operation] = []
    def operate(self):
        raise NotImplementedError
    def updateOperatingCost(self):
        raise NotImplementedError
    def startOperation(self):
        raise NotImplementedError
    def stopOperation(self):
        raise NotImplementedError
    def setOperatingCost(self):
        raise NotImplementedError