from typing import Dict, List, Optional

class Camper:
    def __init__(self, name: str, guardian: str, emergency_information: str):
        self.name = name
        self.guardian = guardian
        self.emergency_information = emergency_information
        self.problem: Optional[str] = None
        self.behavior: Optional[str] = None

class Parent:
    def __init__(self, name: str, camper_behavior: str):
        self.name = name
        self.camper_behavior = camper_behavior

class CampAdministrator:
    def __init__(self):
        self.campers: Dict[str, Camper] = {}
        self.parents: Dict[str, Parent] = {}
        self.groups: Dict[str, List[Camper]] = {}
        self.tasks: Dict[str, List[str]] = {}
        self.events: Dict[str, List[str]] = {}
        self.forms: Dict[str, str] = {}
        self.reminders: Dict[str, str] = {}

def add_camper(self, name: str, guardian: str, emergency_information: str):
    raise NotImplementedError

def remove_camper(self, name: str):
    raise NotImplementedError

def keep_camper_record(self, name: str):
    raise NotImplementedError

def upload_consent_form(self, name: str, form_type: str, content: str):
    raise NotImplementedError

def keep_track(self, name: str, form_type: str):
    raise NotImplementedError

def schedule_activity(self, group: str, activity: str):
    raise NotImplementedError

def create_nametag(self, name: str):
    raise NotImplementedError

def suspend_camper(self, name: str):
    raise NotImplementedError

def set_reminder(self, task: str, date: str):
    raise NotImplementedError

def modify_information(self, name: str, attribute: str, value: str):
    raise NotImplementedError

def delete_task(self, task: str):
    raise NotImplementedError

def modify_task(self, task: str, new_task: str):
    raise NotImplementedError

def notify_parent(self, message: str):
    raise NotImplementedError

def provide_feedback(self, camper: str, feedback: str):
    raise NotImplementedError

def store_emergency_information(self, name: str, information: str):
    raise NotImplementedError

def store_information(self, name: str, information: str):
    raise NotImplementedError

class CampCounselor:
    def __init__(self, name: str):
        self.name = name
        self.kids: List[Camper] = []

def take_attendance(self, camper: Camper):
    raise NotImplementedError

def report_camper(self, camper: Camper, behavior: str):
    raise NotImplementedError

def report_list(self, supplies: List[str]) -> None:
    raise NotImplementedError

def report_repair(self, repair: str) -> None:
    raise NotImplementedError

class CampWorker:
    def __init__(self, name: str):
        self.name = name

def warn_camp_worker(self, worker: CampWorker, reason: str) -> None:
    raise NotImplementedError

class Activity:
    def __init__(self, name: str):
        self.name = name

class Event:
    def __init__(self, name: str):
        self.name = name

class Form:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

class Task:
    def __init__(self, name: str):
        self.name = name

class Group:
    def __init__(self, name: str):
        self.name = name

class Job:
    def __init__(self, name: str):
        self.name = name
