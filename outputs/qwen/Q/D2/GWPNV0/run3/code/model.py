class PetriNet:
    def __init__(self):
        self.nets = []
    def definePetriNet(self):
        raise NotImplementedError

class Net:
    def __init__(self, places, transitions):
        self.places = places
        self.transitions = transitions
class Place:
    pass
class Transition:
    pass
class Network:
    pass