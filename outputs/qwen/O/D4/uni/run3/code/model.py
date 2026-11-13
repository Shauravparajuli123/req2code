class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.professors = []
        self.students = []

    def addProfessor(self, professor):
        raise NotImplementedError

    def addStudent(self, student):
        raise NotImplementedError
class Dormitory:
    def __init__(self, price):
        self.price = price
class Professor:
    def __init__(self, name):
        self.name = name
class Student:
    def __init__(self, name):
        self.name = name