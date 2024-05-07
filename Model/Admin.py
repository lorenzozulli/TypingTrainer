from Model.Utilizzatore import Utilizzatore


class Admin(Utilizzatore):
    def __init__(self):
        self.id = 0
        self.password = ""
        self.username = ""