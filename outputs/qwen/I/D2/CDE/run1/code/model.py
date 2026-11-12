from abc import ABC, abstractmethod

class IUmlType(ABC):
    @abstractmethod
definition: str
    @abstractmethod
def members(self) -> list[IUmlMember]:
        pass

class ICdeComponentSpec(IUmlType):
    pass

class IUmlClass(IUmlType):
    pass

class IUmlComponent(IUmlClass):
    pass

class ICdeServer:
    def __init__(self):
        self.components: list[ICdeComponent] = []

class ICdeComponent:
    pass

class IUmlMember(ABC):
    @abstractmethod
definition: str
    pass

class ICdeMember(IUmlMember):
    execution_performance: str
    execution_details: str
    def __init__(self, execution_performance: str, execution_details: str):
        self.execution_performance = execution_performance
        self.execution_details = execution_details
