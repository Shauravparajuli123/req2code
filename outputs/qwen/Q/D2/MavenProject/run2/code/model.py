from typing import List, Optional

class Project:
    def __init__(self, identifier: str, artifactIdentifier: str, description: str):
        self.identifier = identifier
        self.artifactIdentifier = artifactIdentifier
        self.description = description

    def __str__(self) -> str:
        return f'Project(identifier={self.identifier}, artifactIdentifier={self.artifactIdentifier}, description={self.description})'

    src = ['R1']

class BuildConfiguration:
    def __init__(self, defaultGoal: str, path: str):
        self.defaultGoal = defaultGoal
        self.path = path

    def __str__(self) -> str:
        return f'BuildConfiguration(defaultGoal={self.defaultGoal}, path={self.path})'

    src = ['R2']

class Resource:
    def __init__(self, targetPath: str, directory: str, excludes: str):
        self.targetPath = targetPath
        self.directory = directory
        self.excludes = excludes

    def __str__(self) -> str:
        return f'Resource(targetPath={self.targetPath}, directory={self.directory}, excludes={self.excludes})'

    src = ['R3']

class MailingList:
    def __init__(self, name: str, subscribeString: str, archiveString: str):
        self.name = name
        self.subscribeString = subscribeString
        self.archiveString = archiveString

    def __str__(self) -> str:
        return f'MailingList(name={self.name}, subscribeString={self.subscribeString}, archiveString={self.archiveString})'

    src = ['R4']

class Person:
    def __init__(self, name: str, url: str, organizationUrl: str, timeZone: str):
        self.name = name
        self.url = url
        self.organizationUrl = organizationUrl
        self.timeZone = timeZone

    def __str__(self) -> str:
        return f'Person(name={self.name}, url={self.url}, organizationUrl={self.organizationUrl}, timeZone={self.timeZone})'

    src = ['R5']

class Developer:
    def __init__(self, identifier: str):
        self.identifier = identifier

    def __str__(self) -> str:
        return f'Developer(identifier={self.identifier})'

    src = ['R6']

class MavenProject:
    def __init__(self, buildConfiguration: Optional[BuildConfiguration] = None, contributors: List[Person] = []):
        self.buildConfiguration = buildConfiguration
        self.contributors = contributors

    def addContributor(self, contributor: Person) -> None:
        self.contributors.append(contributor)

    def __str__(self) -> str:
        return f'MavenProject(buildConfiguration={self.buildConfiguration}, contributors={self.contributors})'

    src = ['R7', 'R9']

class MavenProject:
    def addMailingList(self, mailingList: MailingList) -> None:
        pass

    src = ['R8']

class BuildConfiguration:
    def addResource(self, resource: Resource) -> None:
        pass

    src = ['R9', 'R10']

class MavenProject:
    def __init__(self, buildConfiguration: Optional[BuildConfiguration] = None, resources: List[Resource] = [], mailingLists: List[MailingList] = []):
        self.buildConfiguration = buildConfiguration
        self.resources = resources
        self.mailingLists = mailingLists

    src = ['R9', 'R10']
