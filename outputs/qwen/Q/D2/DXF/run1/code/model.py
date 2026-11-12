class Mesh:
    def __init__(self, name: str):
        self.name = name
        self.points = []

    def addPoint(self, point: Point):
        self.points.append(point)

    def __str__(self):
        return f'Mesh(name={self.name}, points={self.points})'

class Point:
    def __init__(self, name: str, x: float, z: float):
        self.name = name
        self.x = x
        self.z = z

    def __str__(self):
        return f'Point(name={self.name}, x={self.x}, z={self.z})'
