from typing import List

class Project:
    def __init__(self, identifier: str, artifactIdentifier: str, description: str):
        self.identifier = identifier
        self.artifactIdentifier = artifactIdentifier
        self.description = description

    def __str__(self):
        return f'Project(identifier={self.identifier}, artifactIdentifier={self.artifactIdentifier}, description={self.description})'

    src = ['R1']

class BuildConfiguration:
    def __init__(self, defaultGoal: str, path: str):
        self.defaultGoal = defaultGoal
        self.path = path

    def __str__(self):
        return f'BuildConfiguration(defaultGoal={self.defaultGoal}, path={self.path})'

    src = ['R2', 'R9']

class MailingList:
    def __init__(self, name: str, subscribeString: str, archiveString: str):
        self.name = name
        self.subscribeString = subscribeString
        self.archiveString = archiveString

    def __str__(self):
        return f'MailingList(name={self.name}, subscribeString={self.subscribeString}, archiveString={self.archiveString})'

    src = ['R4', 'R8']

class Resource:
    def __init__(self, targetPath: str, directory: str, excludes: str):
        self.targetPath = targetPath
        self.directory = directory
        self.excludes = excludes

    def __str__(self):
        return f'Resource(targetPath={self.targetPath}, directory={self.directory}, excludes={self.excludes})'

    src = ['R3']

class Contributor:
    def __init__(self, name: str, url: str, organizationUrl: str, timeZone: str):
        self.name = name
        self.url = url
        self.organizationUrl = organizationUrl
        self.timeZone = timeZone

    def __str__(self):
        return f'Contributor(name={self.name}, url={self.url}, organizationUrl={self.organizationUrl}, timeZone={self.timeZone})'

    src = ['R5']

class Developer:
    def __init__(self, identifier: str):
        self.identifier = identifier

    def __str__(self):
        return f'Developer(identifier={self.identifier})'

    src = ['R6']

class MavenProject:
    def __init__(self, contributors: List[Contributor], buildConfiguration: BuildConfiguration, mailingLists: List[MailingList]):
        self.contributors = contributors
        self.buildConfiguration = buildConfiguration
        self.mailingLists = mailingLists

    def __str__(self):
        return f'MavenProject(contributors={self.contributors}, buildConfiguration={self.buildConfiguration}, mailingLists={self.mailingLists})'

    src = ['R7', 'R8', 'R9']
