from datetime import date

from Model import Test
from Controller import ControllerPickle
from PyQt5.QtWidgets import *

class ControllerTest(object):
    def aggiungiTest(self, nome, contenuto):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()

        listaTest = controllerPickle.listaTest

        nuovoTest = Test()
        identifierCandidato = len(listaTest)

        for i in listaTest:
            if not(identifierCandidato == i.identifier):
                nuovoTest.setIdentifier(identifierCandidato)
            else:
                nuovoTest.setIdentifier(identifierCandidato+1)
            
            if not (nome == i.nome):
                nuovoTest.setNome(nome)
            else:
                registrazioneNonOK = QMessageBox()
                registrazioneNonOK.setWindowTitle("Errore!")
                registrazioneNonOK.setText("Nome già esistente!")
                registrazioneNonOK.exec_()
                return False
            
            nuovoTest.setContenutoTest([])

            text = contenuto.toPlainText()
            words = text.split(",")
            nuovoTest.contenuto.extend(words)
            
            nuovoTest.setDataCreazione(date.today())

            
        listaTest.append(nuovoTest)
        controllerPickle.salvaListaTest()
    '''
    def eliminaTest(self, identifier):
        controllerPickle = ControllerPickle()
        controllerPickle.caricaListaTest()

        listaTest = controllerPickle.listaTest
        del listaTest[id]

        controllerPickle.salvaListaTest()
    
    def modificaTest(self, identifier):
        #TODO: fare questa funzione

    def iniziaTest(self):
        #TODO: fare questa funzione
    
    def interrompiTest(self):
        #TODO: fare questa funzione
    
    def visualizzaListaTest(self):
        #TODO: fare questa funzione
    '''