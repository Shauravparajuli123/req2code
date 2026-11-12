# Artefact set D2_Architectural_Description_Y

## Use cases
(none)

## Class diagram
- Architecture: attributes []; methods []
- ArchitectureDescription: attributes []; methods []
- ArchitectureView: attributes []; methods []
- MainView: attributes []; methods []
- ArchitectureViewPoint: attributes []; methods []
- ArchitectureDescription --association--> Architecture
- ArchitectureDescription --association--> ArchitectureView
- ArchitectureViewPoint --association--> ArchitectureView
- MainView --association--> ArchitectureView

## Python code
```python
class Architecture:
    def __init__(self):
        pass

    def describe(self):
        raise NotImplementedError


class ArchitectureDescription:
    def __init__(self):
        pass

    def select_view(self, view):
        raise NotImplementedError


class ArchitectureView:
    def __init__(self):
        pass

    def conform_to(self, view_point):
        raise NotImplementedError


class MainView(ArchitectureView):
    def __init__(self):
        super().__init__()

    def project(self, architecture_view):
        raise NotImplementedError


class ArchitectureViewPoint:
    def __init__(self):
        pass

    def conform_to_view(self, view):
        raise NotImplementedError
```