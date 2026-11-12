# Artefact set D4_amphibious_X

## Use cases
- MoveVehicle (actor: User)

## Class diagram
- Vehicle: attributes ['position', 'speed', 'max_speed', 'environment']; methods ['move']
- LandVehicle: attributes []; methods []
- MarineVehicle: attributes []; methods []
- AmphibiousVehicle: attributes []; methods []
- Speed: attributes []; methods []
- LandVehicle --generalization--> Vehicle
- MarineVehicle --generalization--> Vehicle
- AmphibiousVehicle --generalization--> Vehicle
- Vehicle --association--> Speed

## Python code
```python
class Vehicle:
    def __init__(self, position, speed, max_speed, environment):
        self.position = position
        self.speed = speed
        self.max_speed = max_speed
        self.environment = environment

    def move(self, time):
        raise NotImplementedError

class LandVehicle(Vehicle):
    pass
class MarineVehicle(Vehicle):
    pass
class AmphibiousVehicle(Vehicle):
    pass
class Speed:
    pass
```