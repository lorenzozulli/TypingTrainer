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
        self.utenteDaModificare.setUsername(nuovoUsername)
        self.utenteDaModificare.setEmail(nuovaEmail)

    def modificaProfilo(self, nuovoUsername, nuovaEmail, nuovaPassword):
        self.utenteDaModificare.setUsername(nuovoUsername)
        self.utenteDaModificare.setEmail(nuovaEmail)
        self.utenteDaModificare.setPassword(nuovaPassword)
        
        