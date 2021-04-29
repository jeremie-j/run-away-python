import os
from GenerationCarte import *
from Deplacement import *
from Menu import *
from Combats import *
from Interface import *
from Magasin import *
import settings
import pickle
from Sauvegarde import *

def Game():
    while settings.StatsJoueur[7] == True: #Tant que joueur est vivant
        remise_sauvegarde("Waow",settings.StatsJoueur,settings.PositionJoueur)
        Interface()
        settings.PositionJoueur = EtageSuivant()
        if settings.PositionJoueur[0] == 9 or settings.PositionJoueur[0] == 19:
            Magasin()
        elif settings.PositionJoueur[0] == 10:
            Boss("MiniBoss")
        elif settings.PositionJoueur[0] == 20:
            Boss("Boss")
        else:
            Combats()

    remise_sauvegarde("Waow",[20,20,7,1,"Poing",[],0,True],[0,2]) #Remise a 0 des stats si mort du joueur