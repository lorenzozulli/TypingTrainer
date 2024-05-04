from Model.Test import Test


class Contenuto(Test):
    #TODO: non so ancora come fare con la lista
    def __init__(self, ):

    def getElemento(self, i):
        return self.elemento[i]
    
    def setElemento(self, elemento, i):
        self.elemento[i] = elemento[i]