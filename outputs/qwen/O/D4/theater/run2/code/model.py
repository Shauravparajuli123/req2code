class Author:
    def __init__(self, name):
        self.name = name
    def writePlay(self):
        raise NotImplementedError

class Musical:
    def __init__(self, name):
        self.name = name
class Opera:
    def __init__(self, name):
        self.name = name
class Participant:
    def __init__(self, name):
        self.name = name
    def actInSession(self, session):
        raise NotImplementedError
class Person:
    def __init__(self, name):
        self.name = name
class Play:
    def __init__(self, name, day, night):
        self.name = name
        self.day = day
        self.night = night
    def play(self):
        raise NotImplementedError
class Session:
    def __init__(self, beginTime, endTime):
        self.beginTime = beginTime
        self.endTime = endTime
class Theater:
    def __init__(self, location):
        self.location = location