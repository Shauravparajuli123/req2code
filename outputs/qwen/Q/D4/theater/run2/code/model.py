from typing import List, DateTime
class Person:
    pass
class Author(Person):
    def __init__(self, name: str):
        self.name = name
class Play:
    def __init__(self, name: str, day: bool, night: bool, location: str, beginTime: DateTime, endTime: DateTime):
        self.name = name
        self.day = day
        self.night = night
        self.location = location
        self.beginTime = beginTime
        self.endTime = endTime
class Participant(Person):
    def __init__(self, name: str):
        self.name = name
def actInPlay(self, play: Play, session: Session):
    raise NotImplementedError
class Theater:
    def __init__(self, location: str):
        self.location = location
class Session:
    def __init__(self, beginTime: DateTime, endTime: DateTime):
        self.beginTime = beginTime
        self.endTime = endTime