class MavenProject:
    def __init__(self, identifier, artifactIdentifier, description):
        self.identifier = identifier
        self.artifactIdentifier = artifactIdentifier
        self.description = description
        self.buildConfiguration = None
        self.mailingLists = []
        self.contributors = []

    def addMailingList(self, mailingList):
        self.mailingLists.append(mailingList)

    def addContributor(self, contributor):
        self.contributors.append(contributor)

class BuildConfiguration:
    def __init__(self, defaultGoal, path):
        self.defaultGoal = defaultGoal
        self.path = path

class Resource:
    def __init__(self, targetPath, directory, excludes):
        self.targetPath = targetPath
        self.directory = directory
        self.excludes = excludes

class MailingList:
    def __init__(self, name, subscribeString, archiveString):
        self.name = name
        self.subscribeString = subscribeString
        self.archiveString = archiveString

class Contributor:
    def __init__(self, name, url, organizationUrl, timeZone):
        self.name = name
        self.url = url
        self.organizationUrl = organizationUrl
        self.timeZone = timeZone

class Developer:
    def __init__(self, identifier):
        self.identifier = identifier