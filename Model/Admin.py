import os
import pickle

class Admin:
    def __init__(self, identifier, password, username, isAdmin):
        self.identifier = identifier
        self.password = password
        self.username = username
        self.isAdmin = isAdmin
    def loadAdmin(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.pickle'), 'wb') as f:
            pickle.dump(admin, f)
            
if __name__ == "__main__":
    admin = Admin(0, 'Admin', 'Admin', True) 
    admin.loadAdmin()
