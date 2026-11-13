from typing import List

class Course:
    def __init__(self, name: str, credit: int):
        self.name = name
        self.credit = credit
        self.professors: List[Professor] = []
        self.students: List[Student] = []

    def enrollStudent(self, student: Student):
        # R5: For a course to exist, it must aggregate, at least, five students
        if len(self.students) < 5:
            raise ValueError("Course must have at least 5 students.")
        self.students.append(student)
        student.enrollInCourse(self)

    def accommodateStudent(self, student: Student):
        # R7: Students can be accommodated in dormitories
        pass

    def __str__(self):
        return f'Course: {self.name}, Credit: {self.credit}'

class Dormitory:
    def __init__(self, price: float):
        self.price = price
        self.students: List[Student] = []

    def __str__(self):
        return f'Dormitory: Price {self.price}, Students: {len(self.students)}'

class Professor:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Professor: {self.name}'

class Student:
    def __init__(self, name: str):
        self.name = name

    def enrollInCourse(self, course: Course):
        # R6: Students can be enrolled in any number of courses
        course.enrollStudent(self)

    def accommodateInDormitory(self, dormitory: Dormitory):
        # R7: Students can be accommodated in dormitories
        pass

    def __str__(self):
        return f'Student: {self.name}'