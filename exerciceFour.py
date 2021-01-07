class Courrier():
    def __init__(self, destinationAdress, destinationShipping, poids, expeditionType):
        self.poids = poids / 1000
        self.expeditionType = expeditionType
        self.destinationAdress = destinationAdress
        self.destinationShipping = destinationShipping
        self.multiplicateur = 1 if self.expeditionType == "normal" else 2


    def ToString(self):
        print("Adresse destination: {}".format(self.destinationAdress))
        print("Adresse expédition: {}".format(self.destinationShipping))
        print("Poids: {}".format(self.poids * 1000))
        print("Type: {}".format(self.expeditionType))


class Lettre(Courrier):
    def __init__(self, destinationAdress, destinationShipping, poids, expeditionType, format):
        super().__init__(destinationAdress, destinationShipping, poids, expeditionType)
        self.format = format
        self.basicPrice = 2.50 if format == "A4" else 3.50

    def calculTimbre(self):
        return self.basicPrice * self.multiplicateur * self.poids

    def ToString(self):
        print("Lettre: ")
        super().ToString()
        print("Format: {}".format(self.format))
        print("Prix du timbre {:0.2f}€".format(self.calculTimbre()))

class Colis(Courrier):
    def __init__(self, destinationAdress, destinationShipping, poids, expeditionType, volume):
        super().__init__(destinationAdress, destinationShipping, poids, expeditionType)
        self.volume = volume

    def calculTimbre(self):
        return 0.25 * self.volume * self.poids * self.multiplicateur

    def ToString(self):
        print("Colis: ")
        super().ToString()
        print("Volume: {}".format(self.volume))
        print("Prix du timbre {:0.2f}€".format(self.calculTimbre()))

L1 = Lettre("Lille", "Paris", 80, "normal", "A4")
L1.ToString()

C1 = Colis("Marrakeche", "Barcelone", 3500, "expresse", 2.25)
C1.ToString()