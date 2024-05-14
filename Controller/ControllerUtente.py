from Controller.ControllerPickle import ControllerPickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class ControllerUtente(object):
    def eliminaUtente(self, identifier):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        listaUtilizzatori.remove(listaUtilizzatori[identifier])

        controllerPickle.salvaListaUtilizzatori()
    
    def modificaUtente(self, nuovoUsername, nuovaEmail):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaUtilizzatori()
        listaUtilizzatori = controllerPickle.listaUtilizzatori

        self.utenteDaModificare.setUsername(nuovoUsername)
        self.utenteDaModificare.setEmail(nuovaEmail)

        controllerPickle.salvaListaUtilizzatori()


    def modificaProfilo(self, identifier, nuovoUsername, nuovaEmail, nuovaPassword):
        try:
            controllerPickle = ControllerPickle()
            controllerPickle.caricaListaUtilizzatori()
            listaUtilizzatori = controllerPickle.listaUtilizzatori

            listaUtilizzatori[identifier].setUsername(nuovoUsername)
            listaUtilizzatori[identifier].setEmail(nuovaEmail)
            listaUtilizzatori[identifier].setPassword(nuovaPassword)
            
            controllerPickle.salvaListaUtilizzatori()
            return True
        except Exception as error:
            print(error)
            return False

        