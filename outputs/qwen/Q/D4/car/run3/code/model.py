from typing import Set, int, String

class Make:
    def __init__(self, name: String):
        self.name = name

class Model:
    def __init__(self, name: String, make: Make):
        self.name = name
        self.make = make

class Engine:
    def __init__(self, power: int):
        self.power = power

class Seat:
    def __init__(self, size: int):
        self.size = size

class Wheel:
    def __init__(self, diameter: int):
        self.diameter = diameter

class Car:
    def __init__(self, numberPlate: String, engine: Engine, seats: Set[Seat], wheels: Set[Wheel]):
        self.numberPlate = numberPlate
        self.engine = engine
        self.seats = seats
        self.wheels = wheels
    def RepresentCar(self):
        raise NotImplementedError
