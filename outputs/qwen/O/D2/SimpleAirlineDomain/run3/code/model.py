class Airport:
    def __init__(self, name: str):
        self.name = name

class Time:
    def __init__(self, year: int, day: int, minute: int):
        self.year = year
        self.day = day
        self.minute = minute

class Flight:
    def __init__(self, originAirport: Airport, departureTime: Time):
        self.originAirport = originAirport
        self.departureTime = departureTime
        self.passengers = []

    def assignPassenger(self, passenger: Passenger):
        if len(self.passengers) < self.maximumPassengers:
            self.passengers.append(passenger)
        else:
            raise Exception('Flight is full')

class Passenger:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender