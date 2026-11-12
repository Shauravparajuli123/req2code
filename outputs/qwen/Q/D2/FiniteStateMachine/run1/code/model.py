from typing import List

class State:
    def __init__(self, name: str):
        self.name = name
        self_fsm: Fsm = None

    def hasStateMachine(self) -> bool:
        return self_fsm is not None

    def hasAssociationStateSource(self) -> bool:
        raise NotImplementedError

class RootFolder:
    def __init__(self, name: str):
        self.name = name
        self.sub_folders: List[RootFolder] = []

    def hasRootFolder(self) -> bool:
        return len(self.sub_folders) > 0

    def hasRootFolders(self) -> bool:
        return len(self.sub_folders) > 1

class Transition:
    def __init__(self, name: str):
        self.name = name
        self_fsm: Fsm = None

    def hasStateMachine(self) -> bool:
        return self_fsm is not None

class Fsm:
    def __init__(self, name: str, state: State, rootFolder: RootFolder, transition: List[Transition] = None):
        self.name = name
        self.state = state
        self.rootFolder = rootFolder
        self.transition = transition if transition is not None else []

    def transitionStateMachine(self):
        raise NotImplementedError

    def hasStateMachine(self) -> bool:
        return True
