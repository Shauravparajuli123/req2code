class Vehicle:
    def __init__(self, position: str, speed: Speed, max_speed: Speed, environment: str):
        self.position = position
        self.speed = speed
        self.max_speed = max_speed
        self.environment = environment

    def move(self, time: float):
        raise NotImplementedError

class LandVehicle(Vehicle):
    pass
class MarineVehicle(Vehicle):
    pass
class AmphibiousVehicle(Vehicle):
    pass
class Speed:
    pass