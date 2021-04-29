import os
import settings

def Interface():
    os.system("cls")
    print("En Jeu, étage " +str(settings.PositionJoueur[0])+ " :")
    print("")
    print("Stats Joueur : | Vie: " + str(settings.StatsJoueur[0]) + "/"+ str(settings.StatsJoueur[1]) +" | Attaque : " + str(round(settings.StatsJoueur[2] * settings.StatsJoueur[3])) + " | Arme : " + str(settings.StatsJoueur[4]) + " | Argent : "+ str(settings.StatsJoueur[6]))
    print("")