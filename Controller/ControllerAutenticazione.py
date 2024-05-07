import json
import os

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from View import LandingPageUtenteView
class ControllerAutenticazione(object):

    #--- metodo per caricare la lista degli utenti ---
    def caricaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.json'), 'r') as f:
            self.listaUtenti = json.load(f)

    #--- metodo per effettuare il login ---
    def logIn(self, username, password):
        self.caricaListaUtenti()

        for i in self.listaUtenti['Utenti']:
            if i['username'] == username:
                if i['password'] == password:
                    if i['isAdmin'] == "False":
                        return "Utente"
                    else:
                        return "Admin"
                else:
                    return "PasswordErrata"
        return "UsernameNonTrovato"
        '''
    def logOut():
        #TODO: fare questa funzione
    
    def registrazione():
        #TODO: fare questa funzione
    
    def salvaListaUtenti():
        #TODO: fare questa funzione
    '''