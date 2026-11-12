from typing import List

class Airport:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Airport(name={self.name})'

class Flight:
    def __init__(self, departureTime: str, maxPassengers: int, originAirport: Airport):
        self.departureTime = departureTime
        self.maxPassengers = maxPassengers
        self.originAirport = originAirport
        self.passengers: List[Passenger] = []
    
    def addPassenger(self, passenger: Passenger):
        if len(self.passengers) < self.maxPassengers:
            self.passengers.append(passenger)
        else:
            raise ValueError('Flight is at maximum passenger capacity')
    
    def __str__(self):
        return f'Flight(departureTime={self.departureTime}, maxPassengers={self.maxPassengers}, originAirport={self.originAirport.name})'
    
    def __repr__(self):
        return f'Flight(departureTime={self.departureTime}, maxPassengers={self.maxPassengers}, originAirport={self.originAirport.name})'

class Passenger:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Passenger(name={self.name}, gender={self.gender})'
