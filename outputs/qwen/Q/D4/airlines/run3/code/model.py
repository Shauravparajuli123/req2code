from typing import List, Double

class Airline:
    def __init__(self, name: String):
        self.name = name
        self.operations: List[OperatingCost] = []

    def startOperation(self, airport: Airport, cost: Double):
        raise NotImplementedError

    def stopOperation(self, airport: Airport):
        raise NotImplementedError

    def updateOperatingCost(self, airport: Airport, new_cost: Double):
        raise NotImplementedError

class Airport:
    def __init__(self, code: String, city: String):
        self.code = code
        self.city = city

class OperatingCost:
    def __init__(self, cost: Double, airport: Airport, airline: Airline):
        self.cost = cost
        self.airport = airport
        self.airline = airline