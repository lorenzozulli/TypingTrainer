import json
import os
import time
import pickle

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Model import Utilizzatore, Utente, Admin
class ControllerAutenticazione(object):

    #--- metodo per caricare la lista degli utenti ---
    def caricaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.pickle'), "rb") as f:
            self.listaUtenti = pickle.load(f)
    
    # --- metodo per salvare la lista di utenti ---
    def salvaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.pickle'), "wb") as f:
            pickle.dump(self.listaUtenti, f, pickle.HIGHEST_PROTOCOL)

    #--- metodo per entrare nel sistema ---
    def logIn(self, username, password):
        self.caricaListaUtenti()

        for i in self.listaUtenti:
            if username == i.username:
                if password == i.password:
                    if self.isAdmin == "False":
                        return "Utente", i
                    else:
                        return "Admin", i
                else:
                    return "PasswordErrata"
        return "UsernameNonTrovato"
    
    # --- metodo per effettuare la registrazione nel sistema ---
    def registrazione(self, username, password, email):
        print("registering")
        try:
            
            self.caricaListaUtenti()

            nuovoUtente = Utente.Utente()
            nuovoUtente.setId(len(self.listaUtenti)+1)
            nuovoUtente.setUsername(username)
            nuovoUtente.setPassword(password)
            nuovoUtente.setEmail(email)
            nuovoUtente.setDataOraCreazione(time.time())
            nuovoUtente.setStatistiche("")
            nuovoUtente.setIsAdmin("False")

            self.listaUtenti.append(nuovoUtente)

            self.salvaListaUtenti()
        except Exception as error:
            print(error)
        return True 
    '''
     # --- metodo per uscire dal sistema ---
    def logOut():
        #TODO: fare questa funzione
    '''