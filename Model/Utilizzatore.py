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
        self.password = password

    def setUsername(self, username):
        self.username = username

    def setIsAdmin(self, isAdmin):
        self.isAdmin = isAdmin