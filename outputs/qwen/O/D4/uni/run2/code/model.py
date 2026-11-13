class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.professors = []
        self.students = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f'Course: {self.name}, Credits: {self.credits}'

class Dormitory:
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f'Dormitory: Price: {self.price}'

class Professor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Professor: {self.name}'

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Student: {self.name}'