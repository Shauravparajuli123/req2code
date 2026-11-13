class LocatedElement:
    def __init__(self, location: str):
        self.location = location

    def __str__(self):
        return self.location

    src = 'R1'


class Outline:
    def __init__(self, extension: str):
        self.extension = extension

    def __str__(self):
        return self.extension

    src = 'R2'


class Node:
    def __init__(self, name: str, icon: str):
        self.name = name
        self.icon = icon

    def __str__(self):
        return f'Node(name={self.name}, icon={self.icon})'

    src = 'R3'


class Label:
    def __init__(self, label: str):
        self.label = label

    def __str__(self):
        return self.label

    src = 'R4'


class LabelSuite:
    def __init__(self):
        pass

    def hasLabel(self, label: Label):
        raise NotImplementedError

    src = 'R10'


class Map:
    def __init__(self, mapString: str):
        self.mapString = mapString

    def __str__(self):
        return self.mapString

    src = 'R6'

