class Point:
    def __init__(self, name: str, coordinatesX: float, coordinatesZ: float):
        self.name = name
        self.coordinatesX = coordinatesX
        self.coordinatesZ = coordinatesZ

    def __str__(self):
        return f'Point(name={self.name}, coordinatesX={self.coordinatesX}, coordinatesZ={self.coordinatesZ})'


class Mesh:
    def __init__(self, name: str):
        self.name = name
        self.points = []

    def addPoint(self, point: Point):
        self.points.append(point)
        raise NotImplementedError

    def createMesh(self):
        raise NotImplementedError

    def __str__(self):
        return f'Mesh(name={self.name}, points={self.points})'