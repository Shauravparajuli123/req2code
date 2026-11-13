class Car:
    def __init__(self, numberPlate, engine, seats, wheels):
        self.numberPlate = numberPlate
        self.engine = engine
        self.seats = seats
        self.wheels = wheels

    def identify(self):
        raise NotImplementedError

class Engine:
    def __init__(self, power):
        self.power = power

    def __str__(self):
        raise NotImplementedError

class Make:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        raise NotImplementedError

class Model:
    def __init__(self, name, make):
        self.name = name
        self.make = make

    def __str__(self):
        raise NotImplementedError

class Seat:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        raise NotImplementedError

class Wheel:
    def __init__(self, diameter):
        self.diameter = diameter

    def __str__(self):
        raise NotImplementedError
