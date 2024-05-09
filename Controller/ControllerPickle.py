import os
import pickle    


class ControllerPickle(object):
    #--- metodo per caricare la lista degli utenti ---
    def caricaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.pickle'), "rb") as f:
            self.listaUtenti = pickle.load(f)
    
    # --- metodo per salvare la lista di utenti ---
    def salvaListaUtenti(self):
        with open(os.path.join('BaseDiDati', 'listaUtenti.pickle'), "wb") as f:
            pickle.dump(self.listaUtenti, f, pickle.HIGHEST_PROTOCOL)

    # --- metodo per caricare la lista dei test
    def caricaListaTest(self):
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), 'rb') as f:
            self.listaTest = pickle.load(f)

    # --- metodo per salvare la lista dei test
    def salvaListaTest(self):
        with open(os.path.join('BaseDiDati', 'listaTest.pickle'), "wb") as f:
            pickle.dump(self.listaTest, f, pickle.HIGHEST_PROTOCOL)


