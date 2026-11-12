from typing import Set

class Wheel:
    def __init__(self, diameter: float):
        self.diameter: float = diameter

class Seat:
    def __init__(self, size: float):
        self.size: float = size

class Engine:
    def __init__(self, power: float):
        self.power: float = power

class Model:
    def __init__(self, name: str):
        self.name: str = name
        self.cars: Set[Car] = set()

class Make:
    def __init__(self, name: str):
        self.name: str = name
        self.models: Set[Model] = set()

class Car:
    def __init__(self, number_plate: str, engine: Engine, seats: Set[Seat], wheels: Set[Wheel]):
        self.number_plate: str = number_plate
        self.engine: Engine = engine
        self.seats: Set[Seat] = seats
        self.wheels: Set[Wheel] = wheels
        self.model: Model = None

    def associate_with_model(self, model: Model):
        raise NotImplementedError

    def get_model_name(self) -> str:
        raise NotImplementedError

class CarFactory:
    def create_car(self, number_plate: str, engine: Engine, seats: Set[Seat], wheels: Set[Wheel], model: Model) -> Car:
        car = Car(number_plate, engine, seats, wheels)
        model.cars.add(car)
        return car