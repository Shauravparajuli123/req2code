from typing import Optional

class Speed:
    pass

class Vehicle:
    def __init__(self, position: float, speed: Speed, max_speed: float, environment: str):
        self.position = position
        self.speed = speed
        self.max_speed = max_speed
        self.environment = environment

def move(self, time: float) -> None:
    raise NotImplementedError

class LandVehicle(Vehicle):
    pass

class MarineVehicle(Vehicle):
    pass

class AmphibiousVehicle(LandVehicle, MarineVehicle):
    pass