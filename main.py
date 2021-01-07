from Compte import *
from Point import *
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

P1=Point(2,3)
P1.ToString()
P2=Point(1,-5,6)
P2.ToString()