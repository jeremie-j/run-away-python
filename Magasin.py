from RandomText import *
from random import *
from Menu import*
from Interface import *
import os
import settings
#StatsJoueur = [20,20,100,1,"Poing",[],10,True] #Pv, Pv max, Attaque, multiplicateur, Nom arme, liste des potions, Or, Vivant ?,
#ItemsVente.append([Type,Arme,attaque,prix])

def Magasin():
    ItemsVente,ItemsVenteMenu = GenItems()
    Running = True
    while Running == True:
        Interface()
        RandomText(["Vous arrivez a distinguer le marchand caché dans l'ombre au fond du magasin","Derrière le comptoire se trouve le marchand, il n'a pas l'air sympathique","La lumière ne fonctione pas très bien ici","Est-ce qu'ils vendent des glaces ici ?","J'ai faim...","Le marchand vous propose de lui acheter des objets","Tu veux des V-Bucks ?","Enfin un peu de repos","Dans quel état est ce magasin ?? J'aimerai parler de suite a un manager"])
        print("")
        Choix = Question("Que voulez vous acheter ?","Quitter",*ItemsVenteMenu)
        if Choix == 1:
            Running = False
        elif Choix == 2:
            if ItemsVente[0][0] == "Arme" and settings.StatsJoueur[6] - ItemsVente[0][3] >= 0:
                
                settings.StatsJoueur[2] = ItemsVente[0][2]
                settings.StatsJoueur[4] = ItemsVente[0][1]
                settings.StatsJoueur[6] -= ItemsVente[0][3]
                ItemsVente.pop(0)
                ItemsVenteMenu.pop(0)
                print("Vous avez acheté un objet")
                os.system("pause")

            elif ItemsVente[0][0] == "Potion" and settings.StatsJoueur[6] - ItemsVente[0][3] >= 0:
                settings.StatsJoueur[5].append("Vie")
                settings.StatsJoueur[6] -= ItemsVente[0][3]
                ItemsVente.pop(0)
                ItemsVenteMenu.pop(0)
                print("Vous avez acheté un objet")
                os.system("pause")
            else:
                print("Vous n'avez pas assez d'argent pour acheter ce objet")
                os.system("pause")

        elif Choix == 3:
            if ItemsVente[1][0] == "Arme" and settings.StatsJoueur[6] - ItemsVente[1][3] >= 0:
                settings.StatsJoueur[2] = ItemsVente[1][2]
                settings.StatsJoueur[4] = ItemsVente[1][1]
                settings.StatsJoueur[6] -= ItemsVente[1][3]
                ItemsVente.pop(1)
                ItemsVenteMenu.pop(1)
                
                print("Vous avez acheté un objet")
                os.system("pause")
            
            elif ItemsVente[1][0] == "Potion" and settings.StatsJoueur[6] - ItemsVente[1][3] >= 0:
                settings.StatsJoueur[5].append("Vie")
                settings.StatsJoueur[6] -= ItemsVente[1][3]
                ItemsVente.pop(1)
                ItemsVenteMenu.pop(1)

                print("Vous avez acheté un objet")
                os.system("pause")
            else:
                print("Vous n'avez pas assez d'argent pour acheter ce objet")
                os.system("pause")

        elif Choix == 4:
            if ItemsVente[2][0] == "Arme" and settings.StatsJoueur[6] - ItemsVente[2][3] >= 0:
                settings.StatsJoueur[2] = ItemsVente[2][2]
                settings.StatsJoueur[4] = ItemsVente[2][1]
                settings.StatsJoueur[6] -= ItemsVente[2][3]
                ItemsVente.pop(2)
                ItemsVenteMenu.pop(2)
                
                print("Vous avez acheté un objet")
                os.system("pause")
            elif ItemsVente[2][0] == "Potion" and settings.StatsJoueur[6] - ItemsVente[2][3] >= 0:
                settings.StatsJoueur[5].append("Vie")
                settings.StatsJoueur[6] -= ItemsVente[2][3]
                ItemsVente.pop(2)
                ItemsVenteMenu.pop(2)

                print("Vous avez acheté un objet")
                os.system("pause")
            else:
                print("Vous n'avez pas assez d'argent pour acheter cet objet")
                os.system("pause")
                
def GenItems():
    Armes = ["Lances","Dague","Epée","Branche","Fouet"]
    ItemsVente = []
    ItemsVenteMenu = []
    for i in range(0,2): #Definis une arme avec une attaque et un prix afin de la mettre en vente
        Type = "Arme"
        Arme = Armes[randrange(0,len(Armes))]
        attaque = settings.PositionJoueur[0]*randrange(2,6)
        prix = attaque*4
        ItemsVente.append([Type,Arme,attaque,prix])
        ItemsVenteMenu.append(Arme + " (" + str(round(attaque*settings.StatsJoueur[3]))+ "PA)" + ", " + str(prix) + " crédits")
    Type = "Potion"
    Arme = "Potion de Vie"
    attaque = "Restaure tous vos PV"
    prix = 25
    ItemsVente.append([Type,Arme,attaque,prix])
    ItemsVenteMenu.append(Arme + " (" + str(attaque)+ ")" + ", " + str(prix) + " crédits")
    return ItemsVente,ItemsVenteMenu
