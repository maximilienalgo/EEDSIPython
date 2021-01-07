from Personne import *


class Employe(Personne):

    def __init__(self, nom, prenom, dateNaissance, salaire):
        super().__init__(nom, prenom, dateNaissance)
        self.salaire = salaire

    def afficher(self):
        super().afficher()
        print("Salaire: {}".format(self.salaire))