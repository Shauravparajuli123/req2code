# Artefact set D2_Architectural_Description_W

## Use cases
(none)

## Class diagram
- Architecture: attributes []; methods []
- ArchitectureDescription: attributes []; methods []
- ArchitectureView: attributes []; methods []
- ArchitectureViewPoint: attributes []; methods []
- MainView: attributes []; methods []
- ArchitectureDescription --association--> Architecture
- ArchitectureDescription --association--> ArchitectureView
- ArchitectureViewPoint --association--> ArchitectureView
- MainView --association--> ArchitectureView

## Python code
```python
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

class MainView:
    pass

class ArchitecturalDescription:
    def __init__(self):
        self.architecture_views: List[ArchitectureView] = []
        self.architecture_view_points: List[ArchitectureViewPoint] = []
        self.main_view: MainView = MainView()

    def select_architecture_view(self, view: ArchitectureView) -> None:
        raise NotImplementedError

    def conform_to_view_point(self, view_point: ArchitectureViewPoint) -> None:
        raise NotImplementedError

    def project_main_view(self) -> None:
        raise NotImplementedError
```