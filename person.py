class person:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def changeEmail(self, newEmail):
        self.email  = newEmail
        print("Email succefully changed to: " + self.email)

    def getPersonInfo(self):
        print("{self.firstName} {self.lastName}: {self.email}")