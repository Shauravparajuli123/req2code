class Fsm:
    def __init__(self, name):
        self.name = name
    def initialize_fsm(self):
        raise NotImplementedError

class RootFolder:
    def __init__(self, name):
        self.name = name
class StateMachine:
    def __init__(self):
        pass
    def has_root_folder(self):
        raise NotImplementedError
    def has_transitions(self):
        raise NotImplementedError
class State:
    def __init__(self, association_state_source):
        self.association_state_source = association_state_source
    def has_state_machine(self):
        raise NotImplementedError
    def has_transitions(self):
        raise NotImplementedError
class Transition:
    def __init__(self, state_machine):
        self.state_machine = state_machine
    def has_state_machine(self):
        raise NotImplementedError
    def has_association_state(self):
        raise NotImplementedError
class AssociationState:
    def __init__(self, transition):
        self.transition = transition