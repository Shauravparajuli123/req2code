# Artefact set D4_amphibious_Y

## Use cases
- MoveVehicle (actor: User)

## Class diagram
- Vehicle: attributes ['position', 'speed', 'maxSpeed', 'environment']; methods ['move']
- LandVehicle: attributes []; methods []
- MarineVehicle: attributes []; methods []
- AmphibiousVehicle: attributes []; methods []
- LandVehicle --generalization--> Vehicle
- MarineVehicle --generalization--> Vehicle
- AmphibiousVehicle --generalization--> Vehicle

## Python code
```python
from enum import Enum

class Environment(Enum):
    LAND = 'land'
    WATER = 'water'
    AIR = 'air'

class Speed:
    pass

class Vehicle:
    def __init__(self, position: float, speed: Speed, max_speed: float, environment: Environment):
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

class AmphibiousVehicle(LandVehicle, MarineVehicle):
    pass
```