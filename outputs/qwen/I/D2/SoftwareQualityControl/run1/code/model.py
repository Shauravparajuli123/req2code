from typing import List, Optional

class Date:
    def __init__(self, day: int, year: int):
        self.day: int = day
        self.year: int = year

class ControlType:
    pass

class Control:
    def __init__(self, type: ControlType, date: Date):
        self.type: ControlType = type
        self.date: Date = date
        self.role: Optional[str] = None
        self.controls_sequence: Optional[ControlsSequence] = None

class ControlsSequence:
    def __init__(self):
        self.controls: List[Control] = []

class ControlsObject:
    def __init__(self, role: str):
        self.role: str = role
        self.controls_sequence: Optional[ControlsSequence] = None

class Bug:
    def __init__(self, number: int, description: str, originator: str, commentsanswer: str, closedate: Date):
        self.number: int = number
        self.description: str = description
        self.originator: str = originator
        self.commentsanswer: str = commentsanswer
        self.closedate: Date = closedate

class BugTracking:
    def __init__(self):
        self.bugs: List[Bug] = []

class Architecture:
    pass

class SoftwareQualityControl:
    def __init__(self, bug_tracking: BugTracking):
        self.bug_tracking: BugTracking = bug_tracking

class SoftwareBugTrackingSystem:
    def __init__(self):
        self.control_types: List[ControlType] = []
        self.controls: List[Control] = []
        self.bug_tracking_system: Optional[BugTracking] = None
