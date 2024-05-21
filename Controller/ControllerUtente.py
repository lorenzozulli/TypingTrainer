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
            controllerAutenticazione = ControllerAutenticazione()

            if any(utente.getUsername() == nuovoUsername for utente in listaUtilizzatori if utente.getUsername() != utenteDaModificare.getUsername()):
                registrazioneNonOK = QMessageBox()
                registrazioneNonOK.setWindowTitle("Errore!")
                registrazioneNonOK.setText("Nome già esistente!")
                registrazioneNonOK.exec_()
                raise Exception


            for utente in listaUtilizzatori:
                if utenteDaModificare.getIdentifier() == utente.getIdentifier():
                    utente.setUsername(nuovoUsername)
                    utente.setEmail(controllerAutenticazione.assegnaEmailAppropriata(nuovaEmail))

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception as e:
            print(e)
            return False

    def modificaProfilo(self, utenteDaModificare, nuovoUsername, nuovaEmail, nuovaPassword):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori
            controllerAutenticazione = ControllerAutenticazione()

            if any(utente.getUsername() == nuovoUsername for utente in listaUtilizzatori if utente.getUsername() != utenteDaModificare.getUsername()):
                registrazioneNonOK = QMessageBox()
                registrazioneNonOK.setWindowTitle("Errore!")
                registrazioneNonOK.setText("Nome già esistente!")
                registrazioneNonOK.exec_()
                raise Exception


            for utente in listaUtilizzatori:
                if utenteDaModificare.getIdentifier() == utente.getIdentifier():
                    utenteDaModificare.setUsername(nuovoUsername)
                    utenteDaModificare.setEmail(controllerAutenticazione.assegnaEmailAppropriata(nuovaEmail))
                    utenteDaModificare.setPassword(controllerAutenticazione.assegnaPasswordAppropriata(nuovaPassword))

                    utente.setUsername(nuovoUsername)
                    utente.setEmail(controllerAutenticazione.assegnaEmailAppropriata(nuovaEmail))
                    utente.setPassword(controllerAutenticazione.assegnaPasswordAppropriata(nuovaPassword))

            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception as e:
            print(e)
            return False

        