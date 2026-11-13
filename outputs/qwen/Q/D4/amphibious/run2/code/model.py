from enum import Enum

class Speed:
    pass

class Environment(Enum):
    LAND = 'land'
    WATER = 'water'
    AIR = 'air'

class Vehicle:
    def __init__(self, position: str, speed: Speed, maxSpeed: Speed, environment: Environment):
        self.position = position
        self.speed = speed
        self.maxSpeed = maxSpeed
        self.environment = environment

    def move(self, time: float):
        raise NotImplementedError('Move method not implemented')

class LandVehicle(Vehicle):
    pass

class MarineVehicle(Vehicle):
    pass