import os
def Question(Question,*Choix):
    Running = True
    while Running == True:
        print(Question)
        for i, Proposition in enumerate(Choix):
            print(i+1,":",Proposition)
        try:
            Numero_Choisi = int(input("Choix : "))
            if Numero_Choisi < 1 or Numero_Choisi > len(Choix):
                print("Merci de selectionner une proposition valide")
                os.system("pause")
                os.system("cls")
            else:
                running = False
                return Numero_Choisi
        except ValueError:
            print("Merci de rentrer un nombre")
            os.system("pause")
            os.system("cls")
#Fonction permettant de creer un menu, principalement pour poser des questions, on entre la question en parametre 1, puis toutes les propositions en parametres 2, la fonctions demande alors au joueur de choisir parmis ces propositions, et retourne
#le numéro de la proposition choisie, empeche également a l'utilisateur de rentrer un choix autre que ceux proposés