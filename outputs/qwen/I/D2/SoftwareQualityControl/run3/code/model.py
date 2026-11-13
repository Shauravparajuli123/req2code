from typing import List

class Day(int):
    pass

class Year(int):
    pass

class ControlType:
    pass

class ControlsObject:
    def __init__(self, role: str):
        self.role = role

class ControlsSequence:
    def __init__(self):
        self.controls: List[Control] = []

class Control:
    def __init__(self, type: ControlType, date: 'Date', sequence: ControlsSequence):
        self.type = type
        self.date = date
        self.sequence = sequence

class Date:
    def __init__(self, day: Day, year: Year):
        self.day = day
        self.year = year

class Bug:
    def __init__(self, number: int, description: str, originator: str, commentsanswer: str, closedate: 'Date'):
        self.number = number
        self.description = description
        self.originator = originator
        self.commentsanswer = commentsanswer
        self.closedate = closedate

class BugTracking:
    def __init__(self):
        self.bugs: List[Bug] = []

class Architecture:
    pass

class SoftwareQualityControl:
    def __init__(self, bug_tracking: BugTracking):
        self.bug_tracking = bug_tracking

class SoftwareBugTrackingSystem:
    def __init__(self):
        self.control_types: List[ControlType] = []
        self.controls: List[Control] = []
