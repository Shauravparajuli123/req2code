from typing import List

class Fsm:
    def __init__(self, name: str):
        self.name = name
        self.state_machine = None

    def set_state_machine(self, state_machine) -> None:
        self.state_machine = state_machine

    def get_state_machine(self) -> 'StateMachine':
        return self.state_machine

    src = ['R5', 'R1']

class StateMachine:
    def __init__(self):
        self.root_folder = None
        self.transitions = []

    def has_root_folder(self) -> bool:
        raise NotImplementedError

    def has_transitions(self) -> bool:
        raise NotImplementedError

    src = ['R4', 'R6', 'R10', 'R11']

class State:
    def __init__(self):
        self.state_machine = None
        self.association_states = []

    def has_state_machine(self) -> bool:
        raise NotImplementedError

    def has_association_states(self) -> bool:
        raise NotImplementedError

    src = ['R3', 'R8', 'R9']

class Transition:
    def __init__(self):
        self.state_machine = None
        self.state = None

    def has_state_machine(self) -> bool:
        raise NotImplementedError

    def has_state(self) -> bool:
        raise NotImplementedError

    src = ['R2', 'R7', 'R11', 'R13']

class AssociationState:
    def __init__(self):
        self.transition = None
        self.source_states = []

    def has_transition(self) -> bool:
        raise NotImplementedError

    def has_source_states(self) -> bool:
        raise NotImplementedError

    src = ['R9', 'R14']