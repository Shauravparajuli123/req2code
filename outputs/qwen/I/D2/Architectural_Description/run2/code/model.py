from typing import List

class Architecture:
    pass

class ArchitectureDescription:
    def __init__(self, architecture: Architecture):
        self._architecture = architecture

class ArchitectureView:
    pass

class ArchitectureViewPoint:
    pass

class MainView(ArchitectureView):
    pass

class ArchitecturalDescription:
    def __init__(self):
        self.architecture_views: List[ArchitectureView] = []
        self.architecture_viewpoints: List[ArchitectureViewPoint] = []
        self.main_view: MainView = MainView()

    def select_architecture_view(self, view: ArchitectureView):
        raise NotImplementedError

    def select_architecture_viewpoint(self, viewpoint: ArchitectureViewPoint):
        raise NotImplementedError
