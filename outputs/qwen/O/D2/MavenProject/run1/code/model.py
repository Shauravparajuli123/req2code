class Project:
    def __init__(self, identifier, artifactIdentifier, description):
        self.identifier = identifier
        self.artifactIdentifier = artifactIdentifier
        self.description = description

class BuildConfiguration:
    def __init__(self, defaultGoal, path):
        self.defaultGoal = defaultGoal
        self.path = path

class MailingList:
    def __init__(self, name, subscribeString, archiveString):
        self.name = name
        self.subscribeString = subscribeString
        self.archiveString = archiveString

class Resource:
    def __init__(self, targetPath, directory, excludes):
        self.targetPath = targetPath
        self.directory = directory
        self.excludes = excludes

class Contributor:
    def __init__(self, name, url, organizationUrl, timeZone):
        self.name = name
        self.url = url
        self.organizationUrl = organizationUrl
        self.timeZone = timeZone

class Developer:
    def __init__(self, identifier):
        self.identifier = identifier

class MavenProject:
    def __init__(self):
        self.contributors = []
        self.buildConfiguration = None
        self.mailingLists = []
        self.resources = []
    def addContributor(self, contributor):
        raise NotImplementedError
    def addMailingList(self, mailingList):
        raise NotImplementedError
    def addResource(self, resource):
        raise NotImplementedError