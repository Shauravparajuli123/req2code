from typing import List

class Airport:
    def __init__(self, name: str):
        self.name = name
        self.flights: List[Flight] = []

class Flight:
    def __init__(self, max_passengers: int, departure_time: str):
        self.max_passengers = max_passengers
        self.departure_time = departure_time
        self.origin_airport: Airport = None
        self.passengers: List[Passenger] = []

class Passenger:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

class SimpleAirlineDomain:
    def __init__(self):
        self.flights: List[Flight] = []
        self.passengers: List[Passenger] = []

    def add_flight(self, flight: Flight):
        raise NotImplementedError

    def add_passenger(self, passenger: Passenger):
        raise NotImplementedError
