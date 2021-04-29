import os
from Menu import *
from Combats import *
from Deplacement import *
from Evenements import *
from GenerationCarte import *
from Sauvegarde import * 
import settings
import pickle


def Accueil():
    Running = True
    while Running == True:
        os.system("cls")
        print("Bienvenue sur Run Away !")
        Choix = Question("Que voulez vous faire ?","Jouer","Supprimer la sauvegarde","Quitter")
        if Choix == 1: #Jouer
            with open("sauvegarde", "rb") as file :#Charge les données du joueur depuis le fichier sauvegarde
                settings.init()
                mon_deplicker = pickle.Unpickler(file)
                recup_sauvegarde = mon_deplicker.load()
                settings.StatsJoueur = recup_sauvegarde["statsJoueur"]
                settings.Name = recup_sauvegarde["nom"]
                settings.PositionJoueur = recup_sauvegarde["position"]
                #Recuperation de la sauvegarde
            Game()
        elif Choix == 2: #Remise a 0 des stats
            print("Sauvegarde supprimée")
            remise_sauvegarde("Waow",[20,20,7,1,"Poing",[],0,True],[0,2])#remplaces les données du joueur dans le fichier sauvegarde par les statistiques de base 
        elif Choix == 3: #Quitter
            Running = False
        os.system("pause")

Accueil()