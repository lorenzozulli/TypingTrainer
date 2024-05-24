import time
import threading


class ControllerTestGame(object):
    def __init__(self):
        self.counter = 0
        self.running = False

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                time = threading.Thread(target=self.timeThread())
                time.start()
        
        if not self.testDisplayLabel.cget('text').startswith(self.WordInputLineEdit) == self.WordInputLineEdit.get():
            self.WordInputLineEdit.config(fg='red')
        else:
            self.WordInputLineEdit.config(fg='black')
        
        if self.WordInputLineEdit.get() == self.TestDisplayLabel.cget('text')[-1]:
            self.running = False
            self.WordInputLineEdit.config(fg='green')



    def timeThread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            CaratteriAlSecondo = len(self.testSelezionato) / self.counter
            CaratteriAlMinuto = CaratteriAlSecondo * 60

    def reset(self):
        self.running = False
        self.counter = 0
        pass