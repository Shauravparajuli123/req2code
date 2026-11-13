class Net:
    def __init__(self):
        self.places = []
    def add_place(self, place):
        raise NotImplementedError

class PetriNet:
    def __init__(self):
        self.transitions = []
    def add_transition(self, transition):
        raise NotImplementedError
class Place:
    def __init__(self):
        self.destination = []
    def add_transition(self, transition):
        raise NotImplementedError
class Transition:
    def __init__(self, net):
        self.net = net
        self.destination_places = []
    def add_place(self, place):
        raise NotImplementedError