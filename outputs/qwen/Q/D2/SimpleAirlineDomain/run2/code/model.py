from typing import List, Optional

class Airport:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

class Time:
    def __init__(self, year: int, day: int, minute: int):
        self.year = year
        self.day = day
        self.minute = minute
    
    def __str__(self):
        return f'{self.year}-{self.day}-{self.minute}''

class Flight:
    def __init__(self, departureTime: Time, originAirport: Airport, maxPassengers: int):
        self.departureTime = departureTime
        self.originAirport = originAirport
        self.maxPassengers = maxPassengers
        self.passengers: List[Passenger] = []
    
    def assignPassenger(self, passenger: Passenger):
        if len(self.passengers) < self.maxPassengers:
            self.passengers.append(passenger)
        else:
            raise ValueError('Flight is full')
    
    def scheduleFlight(self):
        pass
    
    def __str__(self):
        return f'Flight from {self.originAirport.name} at {self.departureTime}'

class Passenger:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
    
    def assignToFlight(self, flight: Flight):
        flight.assignPassenger(self)
    
    def __str__(self):
        return self.name