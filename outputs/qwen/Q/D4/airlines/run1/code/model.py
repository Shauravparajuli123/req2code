from typing import List, Double

class Airport:
    def __init__(self, code: String, city: String):
        self.code = code
        self.city = city

class Operation:
    def __init__(self, airline: Airline, airport: Airport, cost: Double):
        self.airline = airline
        self.airport = airport
        self.cost = cost

class Airline:
    def __init__(self, name: String):
        self.name = name
        self.operations = []

    def startOperation(self, operation: Operation):
        raise NotImplementedError

    def stopOperation(self, operation: Operation):
        raise NotImplementedError

    def updateOperatingCost(self, operation: Operation, new_cost: Double):
        raise NotImplementedError