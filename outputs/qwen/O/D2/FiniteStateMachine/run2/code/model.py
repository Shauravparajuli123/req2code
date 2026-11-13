from typing import List

class AssociationState:
    pass

class State:
    def __init__(self):
        self.association_state_source: List[AssociationState] = []
    def add_association_state(self, association_state: AssociationState):
        raise NotImplementedError

class Transition:
    def __init__(self, state_machine: 'FSM'):
        self.state_machine = state_machine
    def add_source_state(self, source_state: State):
        raise NotImplementedError

class Fsm:
    def __init__(self, name: str):
        self.name = name
    def initialize_fsm(self):
        raise NotImplementedError

class RootFolder:
    def __init__(self, name: str):
        self.name = name