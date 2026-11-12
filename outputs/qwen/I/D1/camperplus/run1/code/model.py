from abc import ABC, abstractmethod

class Camper:
    def __init__(self, name: str, guardian: str, emergency_info: str):
        self.name = name
        self.guardian = guardian
        self.emergency_info = emergency_info
        self.problem = None

    def add_problem(self, problem: str):
        self.problem = problem

    def remove_problem(self):
        self.problem = None

    def __str__(self):
        return self.name

class Parent:
    def __init__(self, name: str, camper_behavior: str):
        self.name = name
        self.camper_behavior = camper_behavior

    def __str__(self):
        return self.name

class CampAdministrator:
    def __init__(self):
        self.campers = []
        self.parents = []
        self.groups = []
        self.tasks = []
        self.events = []
        self.rules = []
        self.forms = []
        self.emergency_info = []

    def add_camper(self, camper: Camper):
        self.campers.append(camper)

    def remove_camper(self, camper: Camper):
        self.campers.remove(camper)

    def keep_camper_record(self, camper: Camper):
        pass

    def keep_information(self, info: str):
        pass

    def keep_track(self, track: str):
        pass

    def log_attendance(self, camper: Camper):
        pass

    def make_nametag(self, camper: Camper):
        pass

    def modify_information(self, info: str):
        pass

    def delete_camper(self, camper: Camper):
        self.campers.remove(camper)

    def delete_parent(self, parent: Parent):
        self.parents.remove(parent)

    def delete_task(self, task: str):
        self.tasks.remove(task)

    def enroll_camper(self, camper: Camper):
        pass

    def create_account(self, parent: Parent):
        pass

    def create_avenue(self, feedback: Feedback):
        pass

    def create_group(self, group: CampGroup):
        self.groups.append(group)

    def create_nametag(self, camper: Camper):
        pass

    def create_registration_form(self, form: Form):
        self.forms.append(form)

    def create_rule(self, rule: str):
        self.rules.append(rule)

    def modify_task(self, task: str):
        pass

    def notify_parent(self, message: str):
        pass

    def provide_feedback(self, feedback: str):
        pass

    def suspend_camper(self, camper: Camper):
        pass

    def upload_consent_form(self, form: Form):
        self.forms.append(form)

    def warn_camp_worker(self, worker: CampWorker, message: str):
        pass

    def __str__(self):
        return 'Camp Administrator'

class CampWorker:
    def __init__(self, name: str):
        self.name = name
        self.campers = []

    def take_attendance(self, camper: Camper):
        pass

    def report_camper(self, camper: Camper, behavior: str):
        pass

    def report_list(self, supplies: list):
        pass

    def report_repair(self, repair: str):
        pass

    def __str__(self):
        return self.name

class CampCounselor(CampWorker):
    def take_attendance(self, camper: Camper):
        pass

    def __str__(self):
        return 'Camp Counselor'

class CamGroup:
    def __init__(self, name: str):
        self.name = name
        self.campers = []

    def add_camper(self, camper: Camper):
        self.campers.append(camper)

    def __str__(self):
        return self.name

class Activity:
    def __init__(self, name: str, schedule: Schedule):
        self.name = name
        self.schedule = schedule

    def __str__(self):
        return self.name

class Schedule:
    def __init__(self, date: Date, activity: Activity):
        self.date = date
        self.activity = activity

    def __str__(self):
        return f'{self.date} - {self.activity.name}'

class Event:
    def __init__(self, name: str, group: CampGroup):
        self.name = name
        self.group = group

    def __str__(self):
        return self.name

class Task:
    def __init__(self, name: str, due_date: Date):
        self.name = name
        self.due_date = due_date

    def __str__(self):
        return self.name

class Feedback:
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

class Form:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name
