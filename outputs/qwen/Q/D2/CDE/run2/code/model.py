from typing import List

class IumlType:
    def __init__(self):
        pass
    def get_type(self) -> str:
        raise NotImplementedError

class IumlClass(IumlType):
    def __init__(self):
        super().__init__()
    def get_class_name(self) -> str:
        raise NotImplementedError

class IumlComponent(IumlClass):
    def __init__(self):
        super().__init__()
    def get_component_id(self) -> str:
        raise NotImplementedError

class ICdeServer(ICdeComponent):
    def __init__(self):
        super().__init__()
    def get_server_name(self) -> str:
        raise NotImplementedError
    def get_components(self) -> List[ICdeComponent]:
        raise NotImplementedError

class ICdeComponentSpec(IumlType):
    def __init__(self):
        super().__init__()
    def get_specification(self) -> str:
        raise NotImplementedError

class ICdeComponent(ICdeServer):
    def __init__(self):
        super().__init__()
    def get_component_id(self) -> str:
        raise NotImplementedError

class IUmlMember:
    def __init__(self):
        pass
    def get_member_name(self) -> str:
        raise NotImplementedError

class ICdeMember(IUmlMember):
    def __init__(self):
        super().__init__()
    def get_execution_performance(self) -> str:
        raise NotImplementedError
    def get_execution_details(self) -> str:
        raise NotImplementedError