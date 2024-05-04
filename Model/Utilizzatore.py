class Utilizzatore(object):
    def __init__(self):
        self.id = ""
        self.password = ""
        self.username = ""
    
    def getId(self):
        return self.id

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username

    def setId(self, id):
        self.id = id

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username