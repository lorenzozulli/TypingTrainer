import os
import pickle

from Model.Utilizzatore import Utilizzatore

class Admin(Utilizzatore):
     
    def loadAdmin(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.pickle'), 'wb') as f:
            pickle.dump(self, f)