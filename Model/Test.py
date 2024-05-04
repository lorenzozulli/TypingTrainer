class Test(object):
    def __init__(self):
        self.contenutoTest = ""
        self.dataOraCreazione = ""
        self.id = id
        self.nome = ""
    
    def getContenutoTest(self):
        return self.contenutoTest
    
    def getDataOraCreazione(self):
        return self.dataOraCreazione
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def setContenutoTest(self, contenutoTest):
        self.contenutoTest = contenutoTest

    def setDataOraCreazione(self, dataOraCreazione):
        self.dataOraCreazione = dataOraCreazione

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome