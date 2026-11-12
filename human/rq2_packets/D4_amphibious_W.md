# Artefact set D4_amphibious_W

## Use cases
- MoveVehicle (actor: User)

## Class diagram
- Vehicle: attributes ['position', 'speed', 'maxSpeed', 'environment']; methods ['move']
- LandVehicle: attributes []; methods []
- MarineVehicle: attributes []; methods []
- Speed: attributes []; methods []
- LandVehicle --generalization--> Vehicle
- MarineVehicle --generalization--> Vehicle

## Python code
```python
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
```