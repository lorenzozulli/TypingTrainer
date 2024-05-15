from datetime import date
import re

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Model.Utente import Utente
from Controller.ControllerPickle import ControllerPickle

class ControllerAutenticazione(object):
    def logIn(self, username, password):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        for i in listaUtilizzatori:
            if username == i.username and password == i.password and i.isAdmin == False:
                        return "Utente", i
            elif username == i.username and password == i.password and i.isAdmin == True:
                        return "Admin", i
            elif username == i.username:
                    return "PasswordErrata", "errore"
        return "UsernameNonTrovato", "errore"
    
    def registrazione(self, username, password, email):
        controllerPickle = ControllerPickle() 
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        self.nuovoUtente = Utente()
        identifierCandidato = len(listaUtilizzatori)
        for self.i in listaUtilizzatori:
            try:
                self.assegnaIdentificatoreUnivoco(identifierCandidato)
                self.assegnaUsernameAppropriato(username)
                self.assegnaPasswordAppropriata(password)
                self.assegnaEmailAppropriata(email)
            except Exception as error:
                print(error)
                return False
            
        self.nuovoUtente.setDataCreazione(date.today())
        self.nuovoUtente.setStatistiche("")
        self.nuovoUtente.setIsAdmin(False)

        listaUtilizzatori.append(self.nuovoUtente)
        controllerPickle.salvaListaUtilizzatori()
        return True

    def assegnaIdentificatoreUnivoco(self, identifierCandidato):
        if not (identifierCandidato == self.i.identifier): 
            self.nuovoUtente.setIdentifier(identifierCandidato)
        else:
            self.nuovoUtente.setIdentifier(identifierCandidato+1)
    
    def assegnaUsernameAppropriato(self, username):
        if not (username == self.i.username):
            if len(username) >= 8:
                self.nuovoUtente.setUsername(username)
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
        
    def assegnaPasswordAppropriata(self, password):
        pattern = r'\d'

        if re.search(pattern, password):
            self.nuovoUtente.setPassword(password)
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("La password non contiene almeno un numero che va da 0 a 9!")
            registrazioneNonOK.exec_()
            return False
        
    def assegnaEmailAppropriata(self, email):
        if email.__contains__('@'):
            self.nuovoUtente.setEmail(email)
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("La email non contiene il carattere @!")
            registrazioneNonOK.exec_()
            return False

    def recuperaPassword(self, identifier, nuovaPassword):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        for i in listaUtilizzatori:
            if identifier == i.identifier:
                pattern = r'\d'
                if re.search(pattern, nuovaPassword):
                    i.password = nuovaPassword
                    break
                else:
                    registrazioneNonOK = QMessageBox()
                    registrazioneNonOK.setWindowTitle("Errore!")
                    registrazioneNonOK.setText("La password non contiene almeno un numero che va da 0 a 9!")
                    registrazioneNonOK.exec_()
            else:
                continue
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Identificatore non trovato!")
            registrazioneNonOK.exec_()
        
            return False

        controllerPickle.salvaListaUtilizzatori()
        return True

    '''
     # --- metodo per uscire dal sistema ---
    def logOut():
        #TODO: fare questa funzione
    '''