from abc import ABC, abstractmethod

class IUmlType(ABC):
    @abstractmethod
define_type(self):
        pass

class ICdeComponentSpec(IUmlType):
    pass

class IUmlClass(IUmlType):
    pass

class ICdeComponent(IUmlClass):
    pass

class ICdeServer:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

class IUmlMember(ABC):
    @abstractmethod
define_member(self):
        pass

class ICdeMember(IUmlMember):
    def __init__(self, execution_performance: str, execution_details: str):
        self.execution_performance = execution_performance
        self.execution_details = execution_details
