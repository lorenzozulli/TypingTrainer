import re

from PyQt5.QtWidgets import *

class Utilizzatore(object):
    def __init__(self):
        self.identifier = ""
        self.password = ""
        self.username = ""
        self.isAdmin: bool
    
    def getIdentifier(self):
        return self.identifier

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username
    
    def getIsAdmin(self):
        return self.isAdmin

    def setIdentifier(self, identifier):
        self.identifier = identifier
          
    def setPassword(self, password):
        pattern = r'\d'

        if re.search(pattern, password):
            self.password = password
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("La password non contiene almeno un numero che va da 0 a 9!")
            registrazioneNonOK.exec_()
            raise Exception

    def setUsername(self, username):
        if (len(username) >= 8 and len(username) <= 16):
            self.username = username
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Lunghezza username non compresa tra 8 e 16 caratteri!")
            registrazioneNonOK.exec_()
            raise Exception

    def setIsAdmin(self, isAdmin):
        self.isAdmin = isAdmin