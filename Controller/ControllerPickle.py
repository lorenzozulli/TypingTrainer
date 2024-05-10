import os
import pickle    


from Model.Admin import Admin
from Model.Test import Test

class ControllerPickle(object):
    def __init__(self):
        if not os.path.isfile(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle')): 
            admin = Admin()
            admin.setIdentifier(0)
            admin.setUsername("Admin")
            admin.setPassword("Admin")
            admin.setIsAdmin(True)
            admin.loadAdmin()
        if not os.path.isfile(os.path.join('BaseDiDati', 'listaTest.pickle')): 
            test = Test()
            test.loadTest()
        
    #--- metodo per caricare la lista degli utenti ---
    def caricaListaUtilizzatori(self):
        with open(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle'), "rb") as f:
            self.listaUtilizzatori = pickle.load(f)
    
    # --- metodo per salvare la lista di utenti ---
    def salvaListaUtilizzatori(self):
        with open(os.path.join('BaseDiDati', 'listaUtilizzatori.pickle'), "wb") as f:
            pickle.dump(self.listaUtilizzatori, f, pickle.HIGHEST_PROTOCOL)

    # --- metodo per caricare la lista dei test
    def caricaListaTest(self):
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), 'rb') as f:
            self.listaTest = pickle.load(f)

    # --- metodo per salvare la lista dei test
    def salvaListaTest(self):
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), "wb") as f:
            pickle.dump(self.listaTest, f, pickle.HIGHEST_PROTOCOL)


