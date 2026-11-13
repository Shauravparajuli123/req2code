from typing import List

class State:
    def __init__(self, name: str):
        self.name = name

    def hasStateMachine(self) -> bool:
        raise NotImplementedError()

    def hasAssociationStateSource(self) -> bool:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        pass

    @name.setter
    def name(self, value: str):
        pass

class RootFolder:
    def __init__(self, name: str):
        self.name = name

    def hasRootFolder(self) -> bool:
        raise NotImplementedError()

    def hasRootFolders(self) -> bool:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        pass

    @name.setter
    def name(self, value: str):
        pass

class Transition:
    def __init__(self, name: str):
        self.name = name

    def hasStateMachine(self) -> bool:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        pass

    @name.setter
    def name(self, value: str):
        pass

class Fsm:
    def __init__(self, name: str, state: State, rootFolder: RootFolder, transition: List[Transition] = None):
        self.name = name
        self.state = state
        self.rootFolder = rootFolder
        self.transition = transition if transition is not None else []

    def transitionStateMachine(self) -> bool:
        raise NotImplementedError()

    def hasStateMachine(self) -> bool:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        pass

    @name.setter
    def name(self, value: str):
        pass

    @property
    def state(self) -> State:
        pass

    @state.setter
    def state(self, value: State):
        pass

    @property
    def rootFolder(self) -> RootFolder:
        pass

    @rootFolder.setter
    def rootFolder(self, value: RootFolder):
        pass

    @property
    def transition(self) -> List[Transition]:
        pass

    @transition.setter
    def transition(self, value: List[Transition]):
        pass