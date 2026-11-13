from typing import List

class TypeString:
    def __init__(self, name: str):
        self.name = name

class Point:
    def __init__(self, name: str, x: float, z: float, type_string: TypeString):
        self.name = name
        self.x = x
        self.z = z
        self.type_string = type_string

class Mesh:
    def __init__(self, name: str):
        self.name = name
        self.points: List[Point] = []

class DrawingInterchangeModel:
    def __init__(self):
        self.meshes: List[Mesh] = []

    def add_mesh(self, mesh: Mesh):
        raise NotImplementedError

    def add_point_to_mesh(self, point: Point, mesh: Mesh):
        raise NotImplementedError