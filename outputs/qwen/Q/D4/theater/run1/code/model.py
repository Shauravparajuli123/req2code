class Author:
    def __init__(self, name: str):
        self.name = name

    def writePlay(self):
        raise NotImplementedError('R10')


class Participant:
    def __init__(self, name: str):
        self.name = name

    def actInPlay(self):
        raise NotImplementedError('R5', 'R9', 'R12')


class Play:
    def __init__(self, name: str, day: bool, night: bool):
        self.name = name
        self.day = day
        self.night = night


class Session:
    def __init__(self, beginTime: str, endTime: str):
        self.beginTime = beginTime
        self.endTime = endTime


class Theater:
    def __init__(self, location: str):
        self.location = location