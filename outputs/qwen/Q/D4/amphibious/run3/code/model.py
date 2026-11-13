from typing import TypeVar, Generic, Protocol

class Speed(Protocol):
    def __str__(self) -> str: ...

class Vehicle(Generic[Speed]):
    position: str
    speed: Speed
    maxSpeed: Speed
    environment: str

    def move(self, time: float) -> None: ...

class LandVehicle(Vehicle[Speed]):
    pass

class MarineVehicle(Vehicle[Speed]):
    pass
