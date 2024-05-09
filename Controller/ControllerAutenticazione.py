import time

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Model.Utente import Utente
from Controller.ControllerPickle import ControllerPickle

class ControllerAutenticazione(object):

    #--- metodo per entrare nel sistema ---
    def logIn(self, username, password):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()

            listaUtilizzatori = controllerPickle.listaUtilizzatori

            for i in listaUtilizzatori:
                if username == i.username:
                    if password == i.password:
                        if i.isAdmin == False:
                            return "Utente", i
                        else:
                            return "Admin", i
                    else:
                        return "PasswordErrata"
            return "UsernameNonTrovato"
        except Exception as error:
            print(error)
    
    # --- metodo per effettuare la registrazione nel sistema ---
    def registrazione(self, username, password, email):
        try:
            controllerPickle = ControllerPickle() 
            controllerPickle.caricaListaUtilizzatori()

            listaUtilizzatori = controllerPickle.listaUtilizzatori

            nuovoUtente = Utente()
            nuovoUtente.setId(len(listaUtilizzatori)+1)
            nuovoUtente.setUsername(username)
            nuovoUtente.setPassword(password)
            nuovoUtente.setEmail(email)
            nuovoUtente.setDataOraCreazione(time.time())
            nuovoUtente.setStatistiche("")
            nuovoUtente.setIsAdmin(False)

            listaUtilizzatori.append(nuovoUtente)

            controllerPickle.salvaListaUtilizzatori()
        except Exception as error:
            print(error)
            return False
        return True
    '''
     # --- metodo per uscire dal sistema ---
    def logOut():
        #TODO: fare questa funzione
    '''