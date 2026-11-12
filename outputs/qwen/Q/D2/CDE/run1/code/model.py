from typing import List

class IumlType:
    def __init__(self):
        pass
    def __str__(self) -> str:
        raise NotImplementedError

class IumlClass(IumlType):
    def __init__(self):
        super().__init__()
    def __str__(self) -> str:
        raise NotImplementedError

class IumlComponent(IumlClass):
    def __init__(self):
        super().__init__()
    def __str__(self) -> str:
        raise NotImplementedError

class ICdeServer(IumlComponent):
    def __init__(self):
        super().__init__()
    def __str__(self) -> str:
        raise NotImplementedError

class ICdeComponent(IumlComponent):
    def __init__(self):
        super().__init__()
    def __str__(self) -> str:
        raise NotImplementedError

class ICdeComponentSpec(IumlType):
    def __init__(self):
        super().__init__()
    def __str__(self) -> str:
        raise NotImplementedError

class IUmlMember:
    def __init__(self):
        pass
    def __str__(self) -> str:
        raise NotImplementedError

class ICdeMember(IUmlMember):
    def __init__(self, executionPerformance: str, executionDetails: str):
        super().__init__()
        self.executionPerformance: str = executionPerformance
        self.executionDetails: str = executionDetails
    def __str__(self) -> str:
        raise NotImplementedError
