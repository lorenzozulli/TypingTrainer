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

    # --- metodo per salvare la lista di utenti ---
    def salvaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.json'), 'w') as f:
            json.dump(self.listaUtenti['Utenti'], f, indent=2)

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
    
    # --- metodo per effettuare la registrazione nel sistema ---
    def registrazione(self, username, password, email):
        print("registering")
        self.caricaListaUtenti()

        nuovoUtente = Utente.Utente()
        nuovoUtente.setId(len(self.listaUtenti)+1)
        nuovoUtente.setUsername(username)
        nuovoUtente.setPassword(password)
        nuovoUtente.setEmail(email)
        nuovoUtente.setDataOraCreazione(time.time())
        nuovoUtente.setStatistiche("")
        nuovoUtente.setIsAdmin("False")
        print(nuovoUtente)

        self.listaUtenti['Utenti'].append(json.dumps(nuovoUtente))
        self.salvaListaUtenti()
        return True
    
    '''
     # --- metodo per uscire dal sistema ---
    def logOut():
        #TODO: fare questa funzione
    '''