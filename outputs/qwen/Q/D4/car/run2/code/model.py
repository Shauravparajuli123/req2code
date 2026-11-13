from typing import Set

class Make:
    def __init__(self, name: str):
        self.name = name
    def __repr__(self):
        return f'Make(name={self.name})'

class Model:
    def __init__(self, name: str, make: Make):
        self.name = name
        self.make = make
    def __repr__(self):
        return f'Model(name={self.name}, make={self.make.name})'

class Engine:
    def __init__(self, power: int):
        self.power = power
    def __repr__(self):
        return f'Engine(power={self.power})'

class Seat:
    def __init__(self, size: int):
        self.size = size
    def __repr__(self):
        return f'Seat(size={self.size})'

class Wheel:
    def __init__(self, diameter: int):
        self.diameter = diameter
    def __repr__(self):
        return f'Wheel(diameter={self.diameter})'

class Car:
    def __init__(self, numberPlate: str, engine: Engine, seats: Set[Seat], wheels: Set[Wheel]):
        self.numberPlate = numberPlate
        self.engine = engine
        self.seats = seats
        self.wheels = wheels
    def RepresentCar(self):
        raise NotImplementedError()
    def __repr__(self):
        return f'Car(numberPlate={self.numberPlate}, engine={self.engine}, seats={self.seats}, wheels={self.wheels})'