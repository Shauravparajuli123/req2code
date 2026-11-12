class Label:
    def __init__(self):
        self.label = None
    def set_label(self, label):
        raise NotImplementedError

class LabelSuite:
    def __init__(self):
        self.labels = []
    def add_label(self, label):
        raise NotImplementedError

class Map:
    def __init__(self):
        self.map_string = None

class Node:
    def __init__(self):
        self.name = None
        self.icon = None
        self.label = None
        self.maps = []
    def add_map(self, map):
        raise NotImplementedError

class Outline:
    def __init__(self):
        self.extension = None
    def add_node(self, node):
        raise NotImplementedError