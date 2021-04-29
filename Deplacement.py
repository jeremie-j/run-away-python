import os
from GenerationCarte import CreationCarte
from Menu import Question
import settings

Chemin1,Chemin2,Chemin3 = CreationCarte() #Creer 3 chemins differents que le joueur pourra emprunter

def EtageSuivant():
    Etage = settings.PositionJoueur[0]
    Proposition = []
    if Chemin1[Etage + 1][1] - settings.PositionJoueur[1] == 1:
        Proposition.append("Droite")
    elif Chemin1[Etage + 1][1] - settings.PositionJoueur[1] == 0:
        Proposition.append("Tout Droit")
    elif Chemin1[Etage + 1][1] - settings.PositionJoueur[1] == -1:
        Proposition.append("Gauche")
    if Chemin2[Etage + 1][1] - settings.PositionJoueur[1] == 1:
        Proposition.append("Droite")
    elif Chemin2[Etage + 1][1] - settings.PositionJoueur[1] == 0:
        Proposition.append("Tout Droit")
    elif Chemin2[Etage + 1][1] - settings.PositionJoueur[1] == -1:
        Proposition.append("Gauche")
    if Chemin3[Etage + 1][1] - settings.PositionJoueur[1] == 1:
        Proposition.append("Droite")
    elif Chemin3[Etage + 1][1] - settings.PositionJoueur[1] == 0:
        Proposition.append("Tout Droit")
    elif Chemin3[Etage + 1][1] - settings.PositionJoueur[1] == -1:
        Proposition.append("Gauche")
    #Regarde lorsque les chemins sont proche, et propose au de continuer sur son chemin, ou de passer sur un autre si ceux ci se croisent
    Proposition_Tri = [] #Les chemins possibles sont stockés dedans

    for i in Proposition:
        if i not in Proposition_Tri:
            Proposition_Tri.append(i)
    Proposition = sorted(Proposition_Tri)#Trie les propositions, enlève les doublons (deux fois la proposition gauche par exemple) et les classe par ordre alphabétique afin d'essayer de garder une regularité dans l'affichage des propositions (Pour ne pas proposer "1.Gauche 2.Droite" puis l'inverse a l'étage d'après)

    if Etage+1 == 9 or Etage+1 == 19: 
        Question("Un magasin se trouve devant vous","Entrer dans le magasin")
        Choix = 1
    elif Etage+1 == 10:
        Question("Derrière le comptoir se trouve une porte menant a une salle de mini Boss","Entrer dans la salle")
        Choix = 1
    elif Etage+1 == 20:
        Question("Au fond du magasin se trouve une énorme porte, menant probablement a un boss","Passer la porte")
        Choix = 1
    else:
        Choix = Question("Où voulez vous aller ?",*Proposition)

    if Proposition[Choix-1] == "Droite":
        settings.PositionJoueur[1] += 1
    elif Proposition[Choix-1] == "Gauche":
        settings.PositionJoueur[1] -= 1
    elif Proposition[Choix-1] == "Tout Droit":
        settings.PositionJoueur[1] += 0
    settings.PositionJoueur[0] += 1
    return settings.PositionJoueur