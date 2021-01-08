class DateNaissance:

    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        return ("{} / {} / {}").format(self.jour, self.mois, self.annee)
