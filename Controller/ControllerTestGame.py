import time
import threading


class ControllerTestGame(object):
    def __init__(self):
        self.counter = 0
        self.running = False

    def start(self):
        pass

    def timeThread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1

    def interrompiTest(self):
        pass

    def riprendiTest(self):
        pass
