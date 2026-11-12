# Artefact set D2_DXF_W

## Use cases
- LoadDrawingInterchangeFormat (actor: User)

## Class diagram
- Mesh: attributes ['name']; methods ['addPoint']
- Point: attributes ['name', 'coordinatesX', 'coordinatesZ']; methods []
- Mesh --association--> Point

## Python code
```python
class Mesh:
    def __init__(self, name):
        self.name = name
        self.points = []

    def addPoint(self, point):
        if point not in self.points:
            self.points.append(point)

    def __str__(self):
        return f'Mesh: {self.name} with {len(self.points)} points'

class Point:
    def __init__(self, name, coordinatesX, coordinatesZ):
        self.name = name
        self.coordinatesX = coordinatesX
        self.coordinatesZ = coordinatesZ

    def __str__(self):
        return f'Point: {self.name} with coordinates X={self.coordinatesX} and Z={self.coordinatesZ}'
```