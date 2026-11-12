class Fsm:
    def __init__(self, name: str):
        self.name = name
        self.states = []
        self.root_folder = None
        self.transitions = []

    def initialize_fsm(self):
        raise NotImplementedError

    def add_state(self, state: State):
        raise NotImplementedError

    def add_root_folder(self, root_folder: RootFolder):
        raise NotImplementedError

    def add_transition(self, transition: Transition):
        raise NotImplementedError

class RootFolder:
    def __init__(self, name: str):
        self.name = name
        self.sub_folders = []

class State:
    def __init__(self):
        self.association_state_source = []

    def add_association_state_source(self, association_state: AssociationState):
        raise NotImplementedError

class Transition:
    def __init__(self, state_machine: Fsm):
        self.state_machine = state_machine
        self.states = []

    def add_state(self, state: State):
        raise NotImplementedError

class AssociationState:
    def __init__(self, transition: Transition):
        self.transition = transition