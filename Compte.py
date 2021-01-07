class CompteBancaire:

    def __init__(self, nom = 'Dupont', solde = 1000):
        self.nom = nom
        self.solde = solde

    def affiche(self):
        print('Le solde du compte bancaire de {} est de {} euros.'.format(self.nom, self.solde))

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme


