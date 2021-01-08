from Compte import *
from Point import *
from DateNaissance import *
from Personne import *
from Employe import *
from Chef import *


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

P = Personne('Ilyass', 'Math', DateNaissance(1, 7, 1982))
P.afficher()

E= Employe('Ilyass','Math',DateNaissance(1,7,1985),7865.548)
E.afficher()

Ch= Chef('Ilyass','Math',DateNaissance(1,7,1988),7865.548,'Ressource humaine')
Ch.afficher()