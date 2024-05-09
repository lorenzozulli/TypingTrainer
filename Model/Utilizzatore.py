class Utilizzatore(object):
    def __init__(self):
        self.id = ""
        self.password = ""
        self.username = ""
        self.isAdmin: bool

    def getId(self):
        return self.id

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username
    
    def getIsAdmin(self):
        return self.isAdmin

    def setId(self, id):
        self.id = id

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

    def setIsAdmin(self, isAdmin):
        self.isAdmin = isAdmin