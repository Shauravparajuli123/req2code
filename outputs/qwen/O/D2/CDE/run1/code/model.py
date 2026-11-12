class IumlType:
    pass

class IumlClass(IumlType):
    pass

class IumlComponent(IumlClass):
    pass

class ICdeServer:
    pass

class ICdeComponent:
    pass

class ICdeMember:
    def __init__(self, executionPerformance: str, executionDetails: str):
        self.executionPerformance = executionPerformance
        self.executionDetails = executionDetails

class IumlMember:
    pass