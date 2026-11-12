class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.students = []
        self.professors = []

    def add_student(self, student):
        if len(self.students) < 5:
            self.students.append(student)
        else:
            raise Exception('Course must have at least 5 students')

    def add_professor(self, professor):
        self.professors.append(professor)

class Dormitory:
    def __init__(self, price):
        self.price = price

class Professor:
    def __init__(self, name):
        self.name = name
class Student:
    def __init__(self, name):
        self.name = name