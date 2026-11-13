from typing import List

class Person:
    def __init__(self, name: str):
        self.name = name

class Author(Person):
    def __init__(self, name: str):
        super().__init__(name)

class Participant(Person):
    def __init__(self, name: str):
        super().__init__(name)
    def actInPlay(self, play: 'Play') -> None:
        raise NotImplementedError

class Play:
    def __init__(self, name: str, day: bool, night: bool):
        self.name = name
        self.day = day
        self.night = night
        self.authors: List[Author] = []
        self.participants: List[Participant] = []
        self.session: Session = None

class Session:
    def __init__(self, beginTime: str, endTime: str):
        self.beginTime = beginTime
        self.endTime = endTime

class Theater:
    def __init__(self, location: str):
        self.location = location
        self.plays: List[Play] = []
