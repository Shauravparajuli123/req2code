from typing import List

class Architecture:
    def __init__(self):
        pass
    def describe(self) -> 'ArchitectureDescription':
        raise NotImplementedError

class ArchitectureDescription:
    def __init__(self):
        pass
    def __str__(self) -> str:
        raise NotImplementedError
    def describe_architecture(self, architecture: Architecture) -> None:
        raise NotImplementedError

class ArchitectureView:
    def __init__(self):
        pass
    def conform_to(self, view_point: 'ArchitectureViewPoint') -> None:
        raise NotImplementedError

class ArchitectureViewPoint:
    def __init__(self):
        pass
    def __str__(self) -> str:
        raise NotImplementedError

class MainView:
    def __init__(self):
        pass
    def project_on(self, view: ArchitectureView) -> None:
        raise NotImplementedError
