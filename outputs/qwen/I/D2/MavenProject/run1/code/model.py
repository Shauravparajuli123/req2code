from typing import List, Optional

class Project:
    def __init__(self, identifier: str, artifact_identifier: str, description: str):
        self.identifier = identifier
        self.artifact_identifier = artifact_identifier
        self.description = description

class BuildConfiguration:
    def __init__(self, default_goal: str, path: str):
        self.default_goal = default_goal
        self.path = path
        self.resources: List['Resource'] = []

class Resource:
    def __init__(self, target_path: str, directory: str, excludes: str):
        self.target_path = target_path
        self.directory = directory
        self.excludes = excludes

class MailingList:
    def __init__(self, name: str, subscribe_string: str, archive_string: str):
        self.name = name
        self.subscribe_string = subscribe_string
        self.archive_string = archive_string

class Person:
    def __init__(self, name: str, url: str, organization_url: str, time_zone: str):
        self.name = name
        self.url = url
        self.organization_url = organization_url
        self.time_zone = time_zone

class Developer(Person):
    def __init__(self, identifier: str, name: str, url: str, organization_url: str, time_zone: str):
        super().__init__(name, url, organization_url, time_zone)
        self.identifier = identifier

class MavenProject:
    def __init__(self, contributors: List[Person], mailing_lists: Optional[List[MailingList]] = None, build_configuration: Optional[BuildConfiguration] = None):
        self.contributors = contributors
        self.mailing_lists = mailing_lists
        self.build_configuration = build_configuration
