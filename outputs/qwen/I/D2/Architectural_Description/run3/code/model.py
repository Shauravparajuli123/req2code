from abc import ABC


class Component:
    pass


class ArchitectureView(Component):
    def __init__(self, main_view: MainView):
        self.main_view = main_view


class ArchitectureViewPoint(Component):
    def __init__(self, architecture_view: ArchitectureView):
        self.architecture_view = architecture_view


class MainView(Component):
    def __init__(self, architecture_view: ArchitectureView):
        self.architecture_view = architecture_view


class ArchitectureDescription(Component):
    def __init__(self, architecture_views: list[ArchitectureView]):
        self.architecture_views = architecture_views


class ArchitecturalDescription:
    def __init__(self, architecture_description: ArchitectureDescription, architecture_views: list[ArchitectureView], architecture_view_points: list[ArchitectureViewPoint], main_views: list[MainView]):
        self.architecture_description = architecture_description
        self.architecture_views = architecture_views
        self.architecture_view_points = architecture_view_points
        self.main_views = main_views

    def select_architecture_view(self, architecture_view: ArchitectureView):
        raise NotImplementedError

    def conform_to_architecture_view_point(self, architecture_view_point: ArchitectureViewPoint):
        raise NotImplementedError

    def project_main_view(self, main_view: MainView):
        raise NotImplementedError