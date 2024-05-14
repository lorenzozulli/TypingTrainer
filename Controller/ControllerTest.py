from datetime import date

from Model import Test
from Controller import ControllerPickle
from PyQt5.QtWidgets import *

class ControllerTest(object):
    def aggiungiTest(self, nome, contenuto):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()
        listaTest = controllerPickle.listaTest

        self.nuovoTest = Test()
        identifierCandidato = len(listaTest)
        for self.i in listaTest:
            try:
                self.assegnaIdentificatoreUnivoco(identifierCandidato)
                self.assegnaNomeAppropriato(nome)
            except Exception as error:
                print(error)
                return False
            
            self.assegnaContenutoTest(contenuto) 
            self.nuovoTest.setDataCreazione(date.today())
            
        listaTest.append(self.nuovoTest)
        controllerPickle.salvaListaTest()
    
    def assegnaIdentificatoreUnivoco(self, identifierCandidato):
        if not(identifierCandidato == self.i.identifier):
            self.nuovoTest.setIdentifier(identifierCandidato)
        else:
            self.nuovoTest.setIdentifier(identifierCandidato+1)
    
    def assegnaNomeAppropriato(self, nome):
        if not (nome == self.i.nome):
            self.nuovoTest.setNome(nome)
        else:
            registrazioneNonOK = QMessageBox()
            registrazioneNonOK.setWindowTitle("Errore!")
            registrazioneNonOK.setText("Nome già esistente!")
            registrazioneNonOK.exec_()
            return False
    
    def assegnaContenutoTest(self, contenuto):
            self.nuovoTest.setContenutoTest([])

            text = contenuto.toPlainText()
            words = text.split(",")
            for i in words:
                self.nuovoTest.setElemento(words[i], i)

    def eliminaTest(self, identifier):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()

        listaTest = controllerPickle.listaTest
        listaTest.remove(listaTest[identifier])

        controllerPickle.salvaListaTest()
    
    def modificaTest(self, nuovoNome, nuovoContenuto):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()

        listaTest = controllerPickle.listaTest
        
        self.testDaModificare.setNome(nuovoNome)
        self.testDaModificare.setContenuto(nuovoContenuto)
'''
    def iniziaTest(self):
        #TODO: fare questa funzione
    
    def interrompiTest(self):
        #TODO: fare questa funzione
    '''