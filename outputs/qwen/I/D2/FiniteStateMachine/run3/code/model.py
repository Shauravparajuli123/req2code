from typing import List

class MgaObject:
    def __init__(self, name: str):
        self.name = name

class StateMachine:
    def __init__(self, root_folder_name: str):
        self.root_folder_name = root_folder_name
        self.root_folder = RootFolder(root_folder_name)

class RootFolder:
    def __init__(self, name: str):
        self.name = name

class State:
    def __init__(self, state_machine: StateMachine):
        self.state_machine = state_machine
        self.association_state_sources: List['AssociationState'] = []

class AssociationState:
    def __init__(self, transition: Transition):
        self.transition = transition

class Transition:
    def __init__(self, state_machine: StateMachine):
        self.state_machine = state_machine
        self.states: List[State] = []

class FSM:
    def __init__(self, state_machine: StateMachine):
        self.state_machine = state_machine
        self.states: List[State] = []
        self.transitions: List[Transition] = []
