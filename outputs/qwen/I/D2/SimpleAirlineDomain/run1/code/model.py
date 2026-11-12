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

# Example usage
airport1 = Airport('JFK')
flight1 = Flight(150, Time(2023, 100, 30), airport1)
passenger1 = Passenger('Alice', 'Female')
passenger2 = Passenger('Bob', 'Male')
flight1.passengers.append(passenger1)
flight1.passengers.append(passenger2)