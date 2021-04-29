from Menu import *
from random import randrange
from Interface import *
from RandomText import *
import settings

def Combats():
    MonstreGen()
    Interface()
    Choix = Question("Vous etes attaqué par un "+str(Monstre[0])+" de niveau "+str(Monstre[1])+" ("+str(Monstre[2])+" PV et "+str(Monstre[3])+" PA). Que voulez vous faire ?","Attaquer","Fuir (pas de récompenses)")
    if Choix == 1:
        global Combats
        Combat = True
        while Combat == True:
            Boost = False
            Interface()
            print("")
            print("Stats "+str(Monstre[0])+" : | Vie: " + str(round(Monstre[2])) + " | Attaque : " + str(Monstre[3]) + " | Niveau : " + str(Monstre[1]))
            print("")
            Choix = Question("Que voulez-vous faire ?","Attaquer avec " + settings.StatsJoueur[4] + " pour infliger "+ str(round(settings.StatsJoueur[2]*settings.StatsJoueur[3])) + " dégats","Utiliser une potion","Fuir")
            if Choix == 1:
                Monstre[2] -= settings.StatsJoueur[2]*settings.StatsJoueur[3]
                Interface()
                if round(Monstre[2]) <= 0:
                    RandomText(["Le monstre n'est plus de ce monde","Les boyaux du monstre sont tombés par terre","Le monstre est mort...","Le monstre est mort... Il l'a bien mérité","Le monstre est mort... Quelle idée aussi de s'attaquer a quelqu'un comme moi"])
                    Combat = False
                    if Boost == True:
                        settings.StatsJoueur[3] -= 1.5
                    settings.StatsJoueur[6] += randrange(1,6) * Monstre[1]
                    Type,param1,param2 = Recompenses()
                    if Type == "Arme":
                        settings.StatsJoueur[2],settings.StatsJoueur[4] = param1,param2
                        os.system("pause")
                        Interface()
                        print("Vous avez recuperé l'arme")
                    if Type == "Rien":
                        Interface()
                        print("Vous avez laissé l'objet derrière vous")
                    if Type == "Potion":
                        settings.StatsJoueur[5].append(param1)
                        
                        os.system("pause")
                    NiveauSup()

                else:
                    print("Vous avez attaqué le monstre, il lui reste " + str(round(Monstre[2])) + " PV.")
                    os.system("pause")
                    settings.StatsJoueur[0] -= Monstre[3]
                    Interface()
                    RandomText(["Ça picote","OOF","Ce n'est qu'une égratinure","Ça saigne un peu","Il va le payer"])
                    print("Le monstre vous attaque et vous retire " + str(Monstre[3]) + "PV.")
                    os.system("pause")
                    if round(settings.StatsJoueur[0]) <= 0:
                        Combat = False
                        Mort()
            elif Choix == 2:
                if not settings.StatsJoueur[5]:
                    print("Vous n'avez pas de potions")
                    os.system("pause")
                else:
                    Interface()
                    Choix = Question("Quelle potion voulez vous utiliser ?","Quitter le menu",*settings.StatsJoueur[5])
                    if Choix == 1:
                        Retour_Au_Menu = "Ouep"
                    else:
                        print("Vous utilisez une potion : " + str(settings.StatsJoueur[5][Choix - 2]))
                        os.system("pause")
                        if settings.StatsJoueur[5][Choix-2] == "Vie":
                            settings.StatsJoueur[0] = settings.StatsJoueur[1]
                            settings.StatsJoueur[5].pop(Choix-2)
                        else:
                            Boost = True
                            settings.StatsJoueur[3] += 1.5
                            settings.StatsJoueur[5].pop(Choix-2)
                        Interface()
                        settings.StatsJoueur[0] -= Monstre[3]
                        print("Le monstre vous attaque et vous retire " + str(Monstre[3]) + "PV.")
                        os.system("pause")
                        if round(settings.StatsJoueur[0]) <= 0:
                            Combat = False
                            Mort()
            elif Choix == 3:
                if Boost == True:
                    settings.StatsJoueur[3] -= 1.5
                Combat = False
                Fuite()
    else:
        Combat = False
        Fuite()

def NiveauSup():
    Type = "Connaissance"
    Interface()
    Choix = Question("Vous avez gagné un point de compétence, que voulez vous améliorer ?","30%"+ " de vie max. suplémentaire","20%"+" d'attaque suplémentaire")
    if Choix == 1:
        param1 = "Vie"
        param2 = 1.3
        settings.StatsJoueur[1] = round(settings.StatsJoueur[1] * param2)
        settings.StatsJoueur[0] = round(settings.StatsJoueur[0] * param2)
    else:
        param1 = "Attaque"
        param2 = 0.2
        settings.StatsJoueur[3] += param2
        os.system("pause")

def Boss(Type):
    BossGen(Type)
    SalleBoss()
    Interface()
    print("Vous etes attaqué par un Boss !")
    os.system("pause")
    Combat = True
    while Combat == True:
        Boost = False
        Interface()
        print("")
        print("Stats "+str(Boss[0])+" : | Vie: " + str(Boss[1]) + " | Attaque : " + str(Boss[2]) + " | Niveau : 666")
        print("")
        Choix = Question("Que voulez-vous faire ?","Attaquer avec " + settings.StatsJoueur[4] + " pour infliger "+ str(round(settings.StatsJoueur[2]*settings.StatsJoueur[3])) + " dégats","Utiliser une potion")
        if Choix == 1:
            Boss[1] -= round(settings.StatsJoueur[2]*settings.StatsJoueur[3])
            Interface()
            if round(Boss[1]) <= 0:
                print("Vous avez tué le Boss, bien joué")
                os.system("pause")
                Combat = False
                if Boost == True:
                    settings.StatsJoueur[3] -= 1.5
                settings.StatsJoueur[6] += randrange(1,6) * Monstre[1]
                
                if Type == "MiniBoss":
                    print("Vous avez trouvé un trésor : 150 Pièces d'or")
                    settings.StatsJoueur[6] += 150
                    os.system("pause")
                    NiveauSup()
                else:
                    os.system("cls")
                    print("Tous ceci n'etait qu'en fait qu'un rêve")
                    os.system("pause")
                    os.system("cls")
                    print("C'est pas très original non ?")
                    os.system("pause")
                    os.system("cls")
                    print("Tant pis")
                    os.system("pause")
                    os.system("cls")
                    print("RunAway !")
                    print("Un jeu developpé par :")
                    print(" - Jérémie Jourda")
                    print(" - Nicolas Foessel")
                    print(" - Simon Chapelain")
                    print("")
                    print("Dans le cadre du projet RPG Python a Hetic")
                    settings.StatsJoueur[7] = False
                    os.system("pause")
                    os.system("cls")
            else:
                print("Vous avez attaqué le Boss, il lui reste " + str(round(Boss[1])) + " PV.")
                os.system("pause")
                settings.StatsJoueur[0] -= Boss[2]
                Interface()
                print("Le Boss vous attaque et vous retire " + str(Boss[2]) + "PV.")
                os.system("pause")
        elif Choix == 2:
            if not settings.StatsJoueur[5]:
                print("Vous n'avez pas de potions")
                os.system("pause")
            else:
                Interface()
                Choix = Question("Quelle potion voulez-vous utiliser ?","Quitter le menu",*settings.StatsJoueur[5])
                if Choix == 1:
                    Retour_Au_Menu = "Ouep"
                else:
                    print("Vous utilisez une potion : " + str(settings.StatsJoueur[5][Choix-2]))
                    os.system("pause")
                    if settings.StatsJoueur[5][Choix-2] == "Vie":
                        settings.StatsJoueur[0] = settings.StatsJoueur[1]
                        settings.StatsJoueur[5].pop(Choix-2)
                    else:
                        Boost = True
                        settings.StatsJoueur[3] += 1.5
                        settings.StatsJoueur[5].pop(Choix-2)
                    Interface()
                    settings.StatsJoueur[0] -= Boss[2]
                    print("Le Boss vous attaque et vous retire " + str(Boss[2]) + "PV.")
                    os.system("pause")
        if round(settings.StatsJoueur[0]) <= 0:
            Combat = False
            Mort()

def SalleBoss():
    phrases = ["Vous entrez dans la pièce","La porte s'est doucement refermée derrière vous","La salle est vide, mais il y a du sang sur les murs","Il y a quelque chose au fond, tapie dans l'ombre","Ça ressemble a un tas de chair et de sang"]
    for i in range(0,len(phrases)):
        Interface()
        print(phrases[i])
        os.system("pause")

def MonstreGen():
    global Monstre
    ListeMonstre = ["Loup","Escargot Mutant","Géant","Squelette","Fantome"]
    Monstre = ListeMonstre[randrange(0,len(ListeMonstre))]
    Niveau  = settings.PositionJoueur[0] + randrange(0,3)
    Vie = randrange(3,5) * Niveau
    Attaque = round(Vie/randrange(3,6))
    Monstre = [Monstre,Niveau,Vie,Attaque]

def BossGen(Type):
    global Boss
    if Type == "MiniBoss":
        Noms = ["Jawad"]
        Nom = Noms[randrange(0,len(Noms))]
        PV = 60
        PA = 15
        Boss = [Nom,PV,PA]
    elif Type == "Boss":
        Noms = ["Burak"]
        Nom = Noms[randrange(0,len(Noms))]
        PV = 500
        PA = 30
        Boss = [Nom,PV,PA]

def Recompenses():
    Armes = ["Lances","Dague","Epée","Branche","Fouet","Hache","Rapière","Marteau","Sabre","Baton"]
    Numero = randrange(0,3)

    if Numero < 2:
        Type = "Arme"
        Arme = Armes[randrange(0,len(Armes))]
        attaque = settings.PositionJoueur[0]*randrange(1,4)
        RandomText(["Il y avait quelque chose de planté dans le monstre...","Il y avait une arme sur un cadavre au fond de la salle","Il y a quelque chose derrière cette pierre","Oh !"])
        print("Vous avez trouvé un objet : " + Arme + "(" + str(round(attaque*settings.StatsJoueur[3])) + "PA)")
        print("")
        Choix = Question("Voulez vous recuperer l'arme ?", "Oui","Non")
        if Choix == 1:
            return Type,attaque,Arme
        if Choix == 2:
            Type = "Rien"
            return Type,attaque,Arme
    elif Numero == 2:
        Type = "Potion"
        random = randrange(0,2)
        if random == 0:
            Interface()
            print("Vous avez gagné une potion de vie. (Restaure tous vos PV)")
            param1 = "Vie"
            param2 = "Rien"
            return Type,param1,param2
        else:
            Interface()
            print("Vous avez gagné une potion d'attaque. (Augmente vos PA pour le combat)")
            param1 = "Attaque"
            param2 = "Rien"
            return Type,param1,param2

def Mort():
    Interface()
    RandomText(["Votre corp restera la, pour nourrir le monstre, ou avertir les autres aventuriers","Le monstre a pondu ses oeufs dans votre corp encore chaud et vivant, degueu..."])
    print("Vous etes mort...")
    settings.StatsJoueur[7] = False

def Fuite():
    pv_perdus = randrange(1,6)
    print("Vous avez fuis, mais vous vous etes legerement blessé, vous avez perdu "+ str(pv_perdus)+ " pv.")
    os.system("pause")
    settings.StatsJoueur[0] -= pv_perdus
    if round(settings.StatsJoueur[0]) <= 0:
        Mort()