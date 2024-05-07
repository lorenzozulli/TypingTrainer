import json
import os

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Model import Utente
class ControllerAutenticazione(object):

    #--- metodo per caricare la lista degli utenti ---
    def caricaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.json'), 'r') as f:
            self.listaUtenti = json.load(f)

    #--- metodo per entrare nel sistema ---
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
    # --- metodo per uscire dal sistema ---
    def logOut():
        #TODO: fare questa funzione
    '''
    # --- metodo per effettuare la registrazione nel sistema ---
    def registrazione(self, username, password, email):
        self.caricaListaUtenti()
        nuovoUtente = Utente.Utente()
        nuovoUtente.setId(len(self.listaUtenti)+1)
        nuovoUtente.setUsername(username)
        nuovoUtente.setPassword(password)
        nuovoUtente.setEmail(email)
        self.salvaListaUtenti(nuovoUtente)
    
    # --- metodo per salvare la lista di utenti ---
    def salvaListaUtenti(self, data):
        self.caricaListaUtenti()
        self.datiEsistenti.append(data)
        with open(os.path.join('BaseDiDati', 'listaUtenti.json'), 'w') as f:
            json.dump(self.datiEsistenti, f, indent=2)