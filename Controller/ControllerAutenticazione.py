import time

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Model.Utente import Utente
from Controller.ControllerPickle import ControllerPickle

class ControllerAutenticazione(object):

    #--- metodo per entrare nel sistema ---
    def logIn(self, username, password):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtenti()

        listaUtenti = controllerPickle.listaUtenti

        for i in self.listaUtenti:
            if username == i.username:
                if password == i.password:
                    if i.isAdmin == False:
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
            controllerPickle = ControllerPickle() 
            controllerPickle.caricaListaUtenti()

            listaUtenti = controllerPickle.listaUtenti


            nuovoUtente = Utente.Utente()
            nuovoUtente.setId(len(self.listaUtenti)+1)
            nuovoUtente.setUsername(username)
            nuovoUtente.setPassword(password)
            nuovoUtente.setEmail(email)
            nuovoUtente.setDataOraCreazione(time.time())
            nuovoUtente.setStatistiche("")
            nuovoUtente.setIsAdmin(False)

            listaUtenti.append(nuovoUtente)

            controllerPickle.salvaListaUtenti()
        except Exception as error:
            print(error) 
    '''
     # --- metodo per uscire dal sistema ---
    def logOut():
        #TODO: fare questa funzione
    '''