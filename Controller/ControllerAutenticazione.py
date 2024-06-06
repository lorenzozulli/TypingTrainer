from datetime import date

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
        try:
            controllerPickle = ControllerPickle() 
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            nuovoUtente = Utente()
            identifierCandidato = len(listaUtilizzatori)

            for self.i in listaUtilizzatori:
                nuovoUtente.setIdentifier(self.controllaIdentificatoreUnivoco(identifierCandidato))
                if self.controllaUsernameUnivoco(username) == True:
                    nuovoUtente.setUsername(username)
                nuovoUtente.setPassword(password)
                nuovoUtente.setEmail(email)

            nuovoUtente.setDataCreazione(date.today())

            nuovoUtente.setMediaErroriPerTest(0)
            nuovoUtente.setMediaNumeroParolePerMinuto(0)
            nuovoUtente.setMediaPrecisionePercentuale(0)
            nuovoUtente.setTotaleTestEseguiti(0)

            nuovoUtente.setIsAdmin(False)

            listaUtilizzatori.append(nuovoUtente)
            controllerPickle.salvaListaUtilizzatori()
        except Exception:
            return False
        return True

    def controllaIdentificatoreUnivoco(self, identifierCandidato):
        if not (identifierCandidato == self.i.getIdentifier()): 
            return identifierCandidato
        else:
            return identifierCandidato+1
        
    def controllaUsernameUnivoco(self, username):
        if not (username == self.i.getUsername()):
            return True
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Username già esistente!")
            registrazioneNonOK.exec_()
            raise Exception
        
    def recuperaPassword(self, identifier, nuovaPassword):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        identificatore_trovato = False

        for i in listaUtilizzatori:
            if identifier == i.getIdentifier():
                i.setPassword(nuovaPassword)
                identificatore_trovato = True
                break

        if not identificatore_trovato:
            recuperoNonOK = QMessageBox()
            recuperoNonOK.setWindowTitle("Errore!")
            recuperoNonOK.setText("Identificatore non trovato!")
            recuperoNonOK.exec_()
            return False

        controllerPickle.salvaListaUtilizzatori()
        return True