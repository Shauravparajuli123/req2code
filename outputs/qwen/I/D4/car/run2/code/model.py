from typing import List, Set

class Wheel:
    def __init__(self, diameter: float):
        self.diameter: float = diameter

class Engine:
    def __init__(self, power: int):
        self.power: int = power

class Seat:
    def __init__(self, size: float):
        self.size: float = size

class Model:
    def __init__(self, name: str):
        self.name: str = name
        self.cars: Set[Car] = set()

class Make:
    def __init__(self, name: str):
        self.name: str = name
        self.models: Set[Model] = set()

class Car:
    def __init__(self, number_plate: str, engine: Engine, seats: Set[Seat], wheels: List[Wheel]):
        self.number_plate: str = number_plate
        self.engine: Engine = engine
        self.seats: Set[Seat] = seats
        self.wheels: List[Wheel] = wheels
        self.model: Model = None

    def associate_with_model(self, model: Model):
        if self.model is not None:
            raise ValueError("Car is already associated with a model.")
        self.model = model
        model.cars.add(self)

    def disassociate_from_model(self, model: Model):
        if self.model is model:
            self.model.cars.remove(self)
            self.model = None

    def get_model_name(self) -> str:
        if self.model is None:
            raise ValueError("Car is not associated with any model.")
        return self.model.name

    def get_make_name(self) -> str:
        if self.model is None:
            raise ValueError("Car is not associated with any model.")
        return self.model.make.name

    def get_engine_power(self) -> int:
        return self.engine.power

    def get_seat_size(self) -> float:
        if not self.seats:
            raise ValueError("Car has no seats.")
        return self.seats.pop().size

    def get_wheel_diameter(self) -> float:
        if not self.wheels:
            raise ValueError("Car has no wheels.")
        return self.wheels.pop().diameter
