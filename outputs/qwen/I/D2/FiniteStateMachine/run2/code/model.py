from typing import List

class MgaObject:
    def __init__(self, name: str):
        self.name = name

class AssociationStateState:
    pass
class FiniteStateMachine:
    def __init__(self, root_folder: RootFolder):
        self.root_folder = root_folder
        self.states: List[State] = []
        self.transitions: List[Transition] = []

class RootFolder:
    def __init__(self, name: str):
        self.name = name

class State:
    def __init__(self, fsm: FiniteStateMachine):
        self.fsm = fsm
        self.association_state_sources: List[AssociationStateState] = []

class Transition:
    def __init__(self, fsm: FiniteStateMachine):
        self.fsm = fsm
        self.state_machine = fsm
        self.association_state_source: AssociationStateState = None
