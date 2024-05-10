import os
import pickle

from Model.Test import Test

class Contenuto(Test):
    def __init__(self):
        self.elemento 

    def getElemento(self, i):
        return self.elemento[i]
    
    def setElemento(self, elemento, i):
        self.elemento[i] = elemento[i]
