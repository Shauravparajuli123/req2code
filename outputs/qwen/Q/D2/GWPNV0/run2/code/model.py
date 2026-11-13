from typing import List

class PetriNet:
    def __init__(self):
        self.net: List[Net] = []
        self.src = ['R1', 'R3']
    def add_net(self, net: Net):
        raise NotImplementedError
    def remove_net(self, net: Net):
        raise NotImplementedError

class Net:
    def __init__(self):
        self.src = ['R3']

class Place:
    def __init__(self):
        self.net: Net = None
        self.src = ['R5', 'R8']
    def set_net(self, net: Net):
        raise NotImplementedError

class Transition:
    def __init__(self):
        self.net: Net = None
        self.place: Place = None
        self.src = ['R5', 'R6', 'R7']
    def set_net(self, net: Net):
        raise NotImplementedError
    def set_place(self, place: Place):
        raise NotImplementedError

class Network:
    def __init__(self):
        self.src = ['R4']
