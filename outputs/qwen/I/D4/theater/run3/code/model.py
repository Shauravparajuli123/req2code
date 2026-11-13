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

class Play:
    def __init__(self, name: str, authors: List[Author], participants: List[Participant], sessions: List[Session], day: bool, night: bool):
        self.name = name
        self.authors = authors
        self.participants = participants
        self.sessions = sessions
        self.day = day
        self.night = night

class Session:
    def __init__(self, begin_time: int, end_time: int):
        self.begin_time = begin_time
        self.end_time = end_time

class Theater:
    def __init__(self, location: str):
        self.location = location
    def play(self, play: Play):
        raise NotImplementedError

class Musical(Play):
    pass

class Opera(Play):
    pass