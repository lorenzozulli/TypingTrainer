import os
import pickle

from Model.Utilizzatore import Utilizzatore

class Admin(Utilizzatore):
            
    def loadAdmin(self):
        listaUtilizztatori = [self]
        with open(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle'), 'wb') as f:
            pickle.dump(listaUtilizztatori, f)