class Airline:
    def __init__(self, name):
        self.name = name
        self.operations = []
    def startOperation(self, airport, cost):
        raise NotImplementedError
    def stopOperation(self, airport):
        raise NotImplementedError
    def updateOperatingCost(self, airport, new_cost):
        raise NotImplementedError
class Airport:
    def __init__(self, code, city):
        self.code = code
        self.city = city
class OperatingCost:
    def __init__(self, cost, airport):
        self.cost = cost
        self.airport = airport