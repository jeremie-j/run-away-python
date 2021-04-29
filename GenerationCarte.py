import os
from random import randrange

def CreationCarte():
    Chemin1 = GenerationChemin()
    Chemin2 = GenerationChemin()
    Chemin3 = GenerationChemin()
    return Chemin1,Chemin2,Chemin3

def GenerationChemin():#Crée 3 chemins differents que l'utilisateur pourra suivre
    Chemin = [[0,2,"Spawn"]]
    old_x = 2
    for Etage in range(0,21):
        x = randrange(0,3)-1
        if old_x + x > 3 or old_x + x < 1:
            x = 0
        x += old_x
        if Etage == 9 or Etage == 19:
            TypeSalle = "Magasin"
            x = 2
        elif Etage == 10:
            TypeSalle = "Mini-Boss"
            x = 2
        elif Etage == 20:
            TypeSalle = "Boss"
            x = 2
        else:
            TypeSalle = "Normal"
        Chemin.append([Etage,x,TypeSalle])
        old_x = x
    return Chemin