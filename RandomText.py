import os
from random import randrange
def RandomText(Phrases):
    Running = True
    nb = randrange(0,len(Phrases))
    print(Phrases[nb])
#Permet de retourner une phrase au hasard parmis la liste donnée en paramètres de la fonction