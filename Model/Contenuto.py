from Model.Test import Test

class Contenuto(Test):
    def __init__(self):
        self.elementi

    def getElemento(self, i):
        return self.elementi[i]
    
    def setElemento(self, elementi, i):
        self.elementi[i] = elementi[i]
