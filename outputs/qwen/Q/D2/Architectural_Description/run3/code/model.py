from typing import List

class Component:
    pass

class Architecture:
    pass

class ArchitectureDescription:
    def __init__(self):
        self.architecture: Architecture = None

class ArchitectureView(Component):
    def __init__(self):
        self.architecture_views_points: List[ArchitectureViewPoint] = []

class ArchitectureViewPoint(Component):
    def __init__(self):
        self.architecture_views: List[ArchitectureView] = []

class MainView(ArchitectureView):
    def __init__(self):
        super().__init__()
        self.architecture_views_points: List[ArchitectureViewPoint] = []

class ArchitectureDescription:
    def __init__(self):
        self.architecture_views: List[ArchitectureView] = []
        self.main_view: MainView = None
        self.architecture: Architecture = None

    def add_architecture_view(self, view: ArchitectureView) -> None:
        raise NotImplementedError

    def add_architecture_views_points(self, view_point: ArchitectureViewPoint) -> None:
        raise NotImplementedError

    def set_main_view(self, view: MainView) -> None:
        raise NotImplementedError

    def set_architecture(self, architecture: Architecture) -> None:
        raise NotImplementedError
