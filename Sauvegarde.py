import pickle 

#from setting import *

nom = "Booooom"

#etablissement des données pour la sauvegarde :


#Mise en sauvegarde
def remise_sauvegarde(nom,StatsJoueur,PositionJoueur):#Sauvegarde les données du joueur sous forme de dictionnaire
    sauvegarde = {
    "nom" : nom,
    "statsJoueur" : StatsJoueur,
    "position" : PositionJoueur,
    }
    with open("sauvegarde", "wb") as file :
        mon_pickler = pickle.Pickler(file)
        mon_pickler.dump(sauvegarde)







 




