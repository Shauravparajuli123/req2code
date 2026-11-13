from typing import List

class Airport:
    def __init__(self, name: str):
        self.name = name

class Flight:
    def __init__(self, max_passengers: int, departure_time: 'Time', origin_airport: Airport):
        self.max_passengers = max_passengers
        self.departure_time = departure_time
        self.origin_airport = origin_airport
        self.passengers: List['Passenger'] = []

class Passenger:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

class Time:
    def __init__(self, year: int, day: int, minute: int):
        self.year = year
        self.day = day
        self.minute = minute

# Additional classes and methods as per requirements
# Airport has multiple flights departing from it
# Each flight has exactly one origin airport
# Each passenger is assigned to exactly one flight
# Flight is connected to Passenger via a directed association
# One end of the association is labeled 'passenger' and carries the multiplicity constraint '0..*'
# A Passenger object can be associated with 0 or more Flight objects
# An airline conducts any number of flights
