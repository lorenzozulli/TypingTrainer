import json
import os
import time

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Model import Utilizzatore, Utente, Admin
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
                        utente = Utente.Utente()
                        utente.setId(i['id'])
                        utente.setUsername(i['username'])
                        utente.setPassword(i['password'])
                        return "Utente", utente
                    else:
                        admin = Admin.Admin()
                        admin.Admin.setId(i['id'])
                        admin.setUsername(i['username'])
                        admin.setPassword(i['password'])
                        return "Admin", admin
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
        self.nuovoUtente = Utente.Utente()
        self.nuovoUtente.setId(len(self.listaUtenti)+1)
        self.nuovoUtente.setUsername(username)
        self.nuovoUtente.setPassword(password)
        self.nuovoUtente.setEmail(email)
        self.nuovoUtente.setDataOraCreazione(time.time())
        self.nuovoUtente.setStatistiche("")
        self.nuovoUtente.setIsAdmin("False")
        self.salvaListaUtenti(self.nuovoUtente)
        return True
    
    # --- metodo per salvare la lista di utenti ---
    def salvaListaUtenti(self, data):
        self.caricaListaUtenti()
        self.datiEsistenti.append(data)
        with open(os.path.join('BaseDiDati', 'listaUtenti.json'), 'w') as f:
            json.dump(self.datiEsistenti, f, indent=2)