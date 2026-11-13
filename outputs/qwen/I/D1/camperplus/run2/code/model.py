from typing import TypedDict, List, Dict, Optional

class Camper:
    id: int
    name: str
    emergency_information: Dict[str, str]
    guardian: Parent
    problem: Optional[str] = None

class Parent:
    id: int
    name: str
    camper_behavior: Dict[str, str]
    forms_submitted: List[str]
    account: Optional[str] = None

class CampAdministrator:
    def add_camper(self, camper: Camper) -> None:
        raise NotImplementedError
    def remove_camper(self, camper_id: int) -> None:
        raise NotImplementedError
    def keep_camper_record(self, year: int) -> None:
        raise NotImplementedError
    def upload_consent_form(self, form: str) -> None:
        raise NotImplementedError
    def keep_track(self, form: str, camper_id: int) -> None:
        raise NotImplementedError
    def schedule_activity(self, activity: str, group: CampGroup) -> None:
        raise NotImplementedError
    def create_nametag(self, camper: Camper) -> None:
        raise NotImplementedError
    def suspend_camper(self, camper_id: int) -> None:
        raise NotImplementedError
    def set_reminder(self, task: str, date: str) -> None:
        raise NotImplementedError
    def modify_information(self, camper_id: int, attribute: str, value: str) -> None:
        raise NotImplementedError
    def delete_camper(self, camper_id: int) -> None:
        raise NotImplementedError
    def delete_parent(self, parent_id: int) -> None:
        raise NotImplementedError
    def modify_task(self, task_id: int, new_task: str) -> None:
        raise NotImplementedError
    def notify_parent(self, message: str) -> None:
        raise NotImplementedError
    def provide_feedback(self, camper_id: int, feedback: str) -> None:
        raise NotImplementedError
    def store_emergency_information(self, camper_id: int, info: Dict[str, str]) -> None:
        raise NotImplementedError
    def store_information(self, camper_id: int, attribute: str, value: str) -> None:
        raise NotImplementedError

class CampCounselor:
    def take_attendance(self, camper_id: int) -> None:
        raise NotImplementedError
    def report_camper(self, camper_id: int, behavior: str) -> None:
        raise NotImplementedError
    def report_list(self, supplies: List[str]) -> None:
        raise NotImplementedError
    def report_repair(self, repair: str) -> None:
        raise NotImplementedError

class CampWorker:
    def submit_completion_report(self, task: str, status: str) -> None:
        raise NotImplementedError
    def warn_camp_worker(self, worker_id: int, reason: str) -> None:
        raise NotImplementedError

class CampGroup:
    id: int
    name: str
    schedule: List[str]

class Activity:
    id: int
    name: str
    date: str

class Event:
    id: int
    name: str
    date: str
    group: CampGroup

class Nametag:
    id: int
    camper: Camper
    text: str
