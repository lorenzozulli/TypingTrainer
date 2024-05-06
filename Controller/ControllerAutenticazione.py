import json
import os

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *

from View import LandingPageUtenteView
class ControllerAutenticazione(object):

    #--- metodo per caricare la lista degli utenti ---
    def caricaListaUtenti(self):
        with open('listaUtenti.json') as f:
            self.listaUtenti = json.load(f)

    def logIn(self):
        for utente in self.listaUtenti:
            if self.UsernameInput.text() == utente.utente['username']:
                if self.PasswordInput.text() == utente.utente['password']:
                    self.authorized = QtWidgets.QMainWindow()
                    LandingPageUtenteView().setupUi(self.authorized)
                    self.authorized.show()


        '''
    def logOut():
        #TODO: fare questa funzione
    
    def registrazione():
        #TODO: fare questa funzione
    
    def salvaListaUtenti():
        #TODO: fare questa funzione
    '''