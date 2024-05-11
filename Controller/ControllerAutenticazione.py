from datetime import date
import re

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
            nuovoUtente.setIdentifier(len(listaUtilizzatori)+1)
            for i in listaUtilizzatori:
                if not (username == i.username):
                    if len(username) >= 8:
                        nuovoUtente.setUsername(username)
                    else:
                        registrazioneNonOK = QMessageBox()
                        registrazioneNonOK.setWindowTitle("Errore!")
                        registrazioneNonOK.setText("Lunghezza Username minore di 8 caratteri!")
                        registrazioneNonOK.exec_()
                        return False
                else:
                    registrazioneNonOK = QMessageBox()
                    registrazioneNonOK.setWindowTitle("Errore!")
                    registrazioneNonOK.setText("Username già esistente!")
                    registrazioneNonOK.exec_()
                    return False
            
            pattern = r'\d'

            if re.search(pattern, password):
                nuovoUtente.setPassword(password)
            else:
                registrazioneNonOK = QMessageBox()
                registrazioneNonOK.setWindowTitle("Errore!")
                registrazioneNonOK.setText("La password non contiene almeno un numero che va da 0 a 9!")
                registrazioneNonOK.exec_()
                return False

            if email.__contains__('@'):
                nuovoUtente.setEmail(email)
            else:
                registrazioneNonOK = QMessageBox()
                registrazioneNonOK.setWindowTitle("Errore!")
                registrazioneNonOK.setText("La email non contiene il carattere @!")
                registrazioneNonOK.exec_()
                return False

            nuovoUtente.setDataCreazione(date.today())
            nuovoUtente.setStatistiche("")
            nuovoUtente.setIsAdmin(False)

            listaUtilizzatori.append(nuovoUtente)

            controllerPickle.salvaListaUtilizzatori()
        except Exception as error:
            print(error)
            return False
        return True
    
    def recuperaPassword(self, identifier, username, nuovaPassword):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()

            listaUtilizzatori = controllerPickle.listaUtilizzatori

            print("Numero di utilizzatori nella lista:", len(listaUtilizzatori))

            for i in listaUtilizzatori:
                if identifier == i.identifier:
                    i.password = nuovaPassword
                    break
            listaUtilizzatori.append(i)
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