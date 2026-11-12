from typing import Set

class Make:
    def __init__(self, name: str):
        self.name = name
        self.models: Set[Model] = set()

class Model:
    def __init__(self, name: str, make: Make):
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
    def __init__(self, numberPlate: str, engine: Engine, seats: Set[Seat], wheels: Set[Wheel]):
        self.numberPlate = numberPlate
        self.engine = engine
        self.seats = seats
        self.wheels = wheels
    def RepresentCar(self):
        raise NotImplementedError