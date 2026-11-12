# Artefact set D1_ticket_X

## Use cases
- SavePersonalInformation (actor: User)
- SavePaymentDetails (actor: User)
- FillSurvey (actor: User)
- SeePersonalizedContent (actor: User)
- EditPreferences (actor: User)
- ChangePassword (actor: User)
- EditPersonalInformation (actor: User)
- SeeTicketHistory (actor: User)
- SeeUpcomingEvents (actor: User)
- SeeFavoriteArtistsAndEvents (actor: User)
- ReadEventDetails (actor: Visitor)
- BuyTicket (actor: Visitor)
- ResellTicket (actor: Reseller)

## Class diagram
- User: attributes ['name', 'dateOfBirth', 'email', 'address', 'preferences']; methods ['savePersonalInformation', 'savePaymentDetails', 'fillSurvey', 'seePersonalizedContent', 'editPreferences', 'changePassword', 'editPersonalInformation']
- Visitor: attributes ['name', 'email']; methods ['buyTicket']
- Reseller: attributes ['bankAccount']; methods ['resellTicket']
- User --association--> Address
- User --association--> Preference

## Python code
```python
class User:
    def __init__(self, name, dateOfBirth, email, address, preferences):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.address = address
        self.preferences = preferences

    def savePersonalInformation(self):
        raise NotImplementedError

    def savePaymentDetails(self):
        raise NotImplementedError

    def fillSurvey(self):
        raise NotImplementedError

    def seePersonalizedContent(self):
        raise NotImplementedError

    def editPreferences(self):
        raise NotImplementedError

    def changePassword(self):
        raise NotImplementedError

    def editPersonalInformation(self):
        raise NotImplementedError

class Visitor:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def buyTicket(self):
        raise NotImplementedError

class Reseller:
    def __init__(self, bankAccount):
        self.bankAccount = bankAccount

    def resellTicket(self):
        raise NotImplementedError

class Address:
    pass

class Preference:
    pass

class BankAccount:
    pass
```