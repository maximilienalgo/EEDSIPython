from Employe import *

class Chef(Employe):

    def __init__(self, nom, prenom, dateNaissance, salaire, service):
        super().__init__(nom, prenom, dateNaissance, salaire)
        self.service = service

    def afficher(self):
        super().afficher()
        print("Service: {}".format(self.service))