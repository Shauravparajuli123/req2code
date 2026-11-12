from enum import Enum

class Date:
    def __init__(self, day: int, year: int):
        self.day = day
        self.year = year

class ControlType(Enum):
    Day = 'Day'
    Year = 'Year'

class Control:
    def __init__(self, type: ControlType, date: Date):
        self.type = type
        self.date = date
    def hasDate(self) -> bool:
        raise NotImplementedError()

class ControlsObject:
    def __init__(self, role: str):
        self.role = role

class ControlsSequence:
    def __init__(self):
        self.controls = []
    def addControlsObject(self, controlsObject: ControlsObject) -> None:
        raise NotImplementedError()

class Bug:
    def __init__(self, number: int, description: str, originator: str, comments: str, closeDate: Date):
        self.number = number
        self.description = description
        self.originator = originator
        self.comments = comments
        self.closeDate = closeDate
    def describeBug(self) -> str:
        raise NotImplementedError()

class BugTracking:
    def __init__(self):
        self.bugs = []
    def trackBug(self, bug: Bug) -> None:
        raise NotImplementedError()

class SoftwareQualityControl:
    def __init__(self):
        self.bugTracking = BugTracking()

class Architecture:
    def __init__(self):
        pass

class SoftwareBugTrackingSystem:
    def __init__(self):
        self.controlTypes = []
    def associateBugWithControlType(self, bug: Bug, controlType: ControlType) -> None:
        raise NotImplementedError()