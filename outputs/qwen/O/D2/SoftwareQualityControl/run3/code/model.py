class Date:
    def __init__(self, day: int, year: int):
        self.day = day
        self.year = year

    def verbObject(self):
        raise NotImplementedError


class Control:
    def __init__(self, type: str, date: Date):
        self.type = type
        self.date = date

    def verbObject(self):
        raise NotImplementedError


class ControlsSequence:
    pass


class ControlsObject:
    def __init__(self, role: str):
        self.role = role


class Bug:
    def __init__(self, number: int, description: str, originator: str, commentsanswer: str, closedate: Date):
        self.number = number
        self.description = description
        self.originator = originator
        self.commentsanswer = commentsanswer
        self.closedate = closedate


class BugTracking:
    pass


class ControlType:
    pass


class Architecture:
    pass


class SoftwareQualityControl:
    def __init__(self, bugTracking: BugTracking):
        self.bugTracking = bugTracking
