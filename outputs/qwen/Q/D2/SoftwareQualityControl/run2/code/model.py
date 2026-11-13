from typing import TypedDict, List

class Date:
    day: int
    year: int

    def __init__(self, day: int, year: int):
        self.day = day
        self.year = year


class ControlType:
    pass


class ControlsObject:
    role: str

    def __init__(self, role: str):
        self.role = role


class Control:
    type: ControlType
    date: Date

    def __init__(self, type: ControlType, date: Date):
        self.type = type
        self.date = date

    def has(self) -> bool:
        raise NotImplementedError


class ControlsSequence:
    controls: List[ControlsObject]

    def __init__(self, controls: List[ControlsObject]):
        self.controls = controls

    def belongs_to(self) -> bool:
        raise NotImplementedError


class Bug(TypedDict):
    number: int
    description: str
    originator: str
    comments: str
    closeDate: Date


class BugTracking:
    def trackBug(self, bug: Bug) -> None:
        raise NotImplementedError

    def describeControl(self, control: Control) -> str:
        raise NotImplementedError


class SoftwareQualityControl:
    bugTracking: BugTracking

    def __init__(self, bugTracking: BugTracking):
        self.bugTracking = bugTracking


class SoftwareBugTrackingSystem:
    controlType: ControlType

    def __init__(self, controlType: ControlType):
        self.controlType = controlType