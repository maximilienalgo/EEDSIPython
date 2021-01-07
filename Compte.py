class CompteBancaire:

    def __init__(self, nom = None, solde = None):
        self.nom = nom or 'Dupont'
        self.solde = solde or 1000

    def affiche(self):
        print('Le solde du compte bancaire de {} est de {} euros.'.format(self.nom, self.solde))

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme


