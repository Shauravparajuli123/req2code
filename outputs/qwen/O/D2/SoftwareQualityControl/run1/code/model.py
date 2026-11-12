class Date:
    def __init__(self, day: int, year: int):
        self.day = day
        self.year = year

class Control:
    def __init__(self, type: ControlType, date: Date):
        self.type = type
        self.date = date

class ControlsSequence:
    def __init__(self):
        pass

class ControlType:
    pass

class ControlsObject:
    def __init__(self, role: str):
        self.role = role

class Bug:
    def __init__(self, number: int, description: str, originator: str, comments: str, closeDate: Date):
        self.number = number
        self.description = description
        self.originator = originator
        self.comments = comments
        self.closeDate = closeDate

class BugTracking:
    pass

class Architecture:
    pass

class SoftwareQualityControl:
    def __init__(self, bugTracking: BugTracking):
        self.bugTracking = bugTracking

class SoftwareBugTrackingSystem:
    def __init__(self, controlType: ControlType):
        self.controlType = controlType