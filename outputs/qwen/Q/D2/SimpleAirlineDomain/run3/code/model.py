from typing import List, Time

class Airport:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

class Flight:
    def __init__(self, departureTime: Time, originAirport: Airport, maxPassengers: int):
        self.departureTime = departureTime
        self.originAirport = originAirport
        self.maxPassengers = maxPassengers
        self.passengers: List[Passenger] = []

    def depart(self) -> None:
        raise NotImplementedError('Method not implemented')

    def assignPassenger(self, passenger: Passenger) -> None:
        raise NotImplementedError('Method not implemented')

class Passenger:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

    def __str__(self):
        return self.name
