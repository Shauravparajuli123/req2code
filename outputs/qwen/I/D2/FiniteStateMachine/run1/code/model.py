from typing import List

class MgaObject:
    def __init__(self, name: str):
        self.name = name

class StateMachine:
    def __init__(self, root_folder_name: str):
        self.root_folder = RootFolder(root_folder_name)

class RootFolder:
    def __init__(self, name: str):
        self.name = name
        self.sub_folders: List[RootFolder] = []

class State:
    def __init__(self, fsm: StateMachine):
        self_fsm = fsm
        self.association_state_sources: List[AssociationState] = []

class Transition:
    def __init__(self, fsm: StateMachine):
        self_fsm = fsm
        self.state_machine = fsm

class AssociationState:
    def __init__(self, transition: Transition):
        self.transition = transition
