from DateNaissance import *

class Personne:

    def __init__(self, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance

    def afficher(self):
        print("Nom: {}".format(self.nom))
        print("Prénom: {}".format(self.prenom))
        print("Date de naissance: {}".format(self.dateNaissance))