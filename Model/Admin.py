import os
import pickle

from Model.Utilizzatore import Utilizzatore, ListUtilizzatore

class Admin(Utilizzatore):
     
    def loadAdmin(self):
        with open(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle'), 'wb') as f:
            pickle.dump(self, f)