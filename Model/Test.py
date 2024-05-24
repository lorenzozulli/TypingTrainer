import os
import pickle
import random

class Test(object):
    def __init__(self):
        self.contenutoTest = ""
        self.dataCreazione = ""
        self.identifier = ""
        self.nome = ""
    
    def getContenutoTest(self): 
        stringheConvertite = [str(i) for i in self.contenutoTest]
        return ','.join(stringheConvertite)
    
    def getDataCreazione(self):
        return self.dataCreazione
    
    def getIdentifier(self):
        return self.identifier
    
    def getNome(self):
        return self.nome
    
    def setContenutoTest(self, contenutoTest):
        self.contenutoTest = contenutoTest

    def setDataCreazione(self, dataCreazione):
        self.dataCreazione = dataCreazione

    def setIdentifier(self, identifier):
        self.identifier = identifier

    def setNome(self, nome):
        self.nome = nome

    def loadTest(self):
        listaTest = [self]
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), 'wb') as f:
            pickle.dump(listaTest, f)

    def shuffleTest(self):
        contenutoTestRandomizzato = self.contenutoTest
        random.shuffle(contenutoTestRandomizzato)
        stringheConvertite = [str(i) for i in contenutoTestRandomizzato]
        return ' '.join(stringheConvertite)

        

    