class Concept:
    pass

class Net:
    pass

class Network:
    pass

class PetriNet:
    pass

class Place:
    def has(self, concept):
        raise NotImplementedError

class Transition:
    def has(self, concept):
        raise NotImplementedError
    def has(self, destination):
        raise NotImplementedError