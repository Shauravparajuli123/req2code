from typing import List

class Course:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits
        self.professors: List[Professor] = []
        self.students: List[Student] = []

    def enrollStudent(self, student: Student):
        self.students.append(student)
        raise NotImplementedError

    def addProfessor(self, professor: Professor):
        self.professors.append(professor)
        raise NotImplementedError

class Dormitory:
    def __init__(self, price: float):
        self.price = price
        self.students: List[Student] = []

    def accommodateStudent(self, student: Student):
        self.students.append(student)
        raise NotImplementedError

class Professor:
    def __init__(self, name: str):
        self.name = name

class Student:
    def __init__(self, name: str):
        self.name = name

    def enrollInCourse(self, course: Course):
        course.students.append(self)
        raise NotImplementedError

    def accommodateInDormitory(self, dormitory: Dormitory):
        dormitory.accommodateStudent(self)
        raise NotImplementedError