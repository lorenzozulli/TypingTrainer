from Controller.ControllerPickle import ControllerPickle
from Controller.ControllerAutenticazione import ControllerAutenticazione
from PyQt5.QtWidgets import *

class ControllerUtente(object):
    def eliminaUtente(self, identifier):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            for i in listaUtilizzatori:
                if identifier == i.getIdentifier():
                    listaUtilizzatori.remove(i)

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False
    
    def modificaUtente(self, utenteDaModificare, nuovoUsername, nuovaEmail):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            self.controllaUsernameModificabile(nuovoUsername, listaUtilizzatori, utenteDaModificare)

            for utente in listaUtilizzatori:
                if utenteDaModificare.getIdentifier() == utente.getIdentifier():
                    utente.setUsername(nuovoUsername)
                    utente.setEmail(nuovaEmail)

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False

    def modificaProfilo(self, utenteDaModificare, nuovoUsername, nuovaEmail, nuovaPassword):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            self.controllaUsernameModificabile(nuovoUsername, listaUtilizzatori, utenteDaModificare)

            for utente in listaUtilizzatori:
                if utenteDaModificare.getIdentifier() == utente.getIdentifier():
                    utente.setUsername(nuovoUsername)
                    utente.setEmail(nuovaEmail)
                    utente.setPassword(nuovaPassword)

                    utenteDaModificare.setUsername(nuovoUsername)
                    utenteDaModificare.setEmail(nuovaEmail)
                    utenteDaModificare.setPassword(nuovaPassword)


            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception:
            return False
        
    def controllaUsernameModificabile(self, nuovoUsername, listaUtilizzatori, utenteDaModificare):
        if any(utente.getUsername() == nuovoUsername for utente in listaUtilizzatori if utente.getUsername() != utenteDaModificare.getUsername()):
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Nome già esistente!")
            registrazioneNonOK.exec_()
            raise Exception

        