import os
from random import randrange
from tkinter import *
from math import ceil

startLevel = True
print("********************************************* Game CAN2019 *********************************************")
nom = input("Entrez votre psuedo \n")

print("-------------------------------------------------------------------------\n")
print("Bonjour "+nom+" Bienvenue au Game CAN2019 \n")

while startLevel:
    sommeInitiale = input("Veuillez entrer votre montant initial svp \n")
    try:
        sommeInitiale = int(sommeInitiale)
    except ValueError:
        print("Montant initial non defini")
        continue
    if sommeInitiale <0:
        print("Vous avez entrer un nombre négatif ")
        continue
    print("Liste des rencontres")
    print("----------------------------------------------------------------------------------------")
    print("n°1-Cote d'ivoire  VS   n°2-Algerie\nn°3-Afrique du sud VS   n°4-Nigeria\nn°5-Senegal        VS   n°6-Benin\nn°7-Madagascar     VS   n°8-Tunisie")
    print("----------------------------------------------------------------------------------------")
    print("Vous debutez le jeu avec ",sommeInitiale,"$")
    nombre = input("Veuillez entrer le numero de votre équipe \n ")
    try:
        nombre = int(nombre)
    except ValueError:
        print("le nombre entré est invalide")
        continue
    montant_mise = input("Veuillez entrer le montant de votre mise \n ")
    try:
        montant_mise = float(montant_mise)
    except ValueError:
        print("Le montant entré est invalide")
        continue
    # Verifie le numero de l'equipe
    if nombre > 8:
        print("le numero choisi ne correspond pas à une équipe")
        continue
    elif nombre < 0:
        print("le nombre entré est negatif")
        continue
    # verifie le motant
    if montant_mise > sommeInitiale:
        print("Vous ne pouvez miser autant d'argent vous avez que ", sommeInitiale,"$")
        continue
    elif montant_mise < 0:
        print("Le motant entré est negatif")
        continue
    #Choix de l'equipe gagnante
    success = randrange(1, 8)
    # si succes l'utilisateur gagne 2 fois la somme misée
    if (nombre == success):
        gain = montant_mise * 2
        sommeInitiale += gain
        print("---***************************FELICITATION******************************************---")
        print("---*********************************************************************************---")
        print("---***************************FELICITATION******************************************---")
        print("---*********************************************************************************---")
        print("---***************************FELICITATION******************************************---")
        print("Félicitation vous avez gagné ", gain, " $ votre  nouveau solde est", sommeInitiale, "$")
        #Si les deux nombre sont pairs ou impairs l'utilisateur gagne 50% du montant misé
    elif (nombre % 2 == success % 2):
        gain = montant_mise * 0.5
        sommeInitiale += gain
        print("---***************************FELICITATION******************************************---")
        print("---*********************************************************************************---")
        print("---*********************************************************************************---")
        print("---*********************************************************************************---")
        print("---***************************FELICITATION******************************************---")
        print("vous avez gagné ", gain, " $ votre nouveau solde est", sommeInitiale, "$")
        #le seul cas ou l'utilisateur perd la somme misée
    else:
        sommeInitiale -= montant_mise
        print("---***************************ECHEC************************************************---")
        print("---*********************************************************************************---")
        print("---*********************************************************************************---")
        print("---*********************************************************************************---")
        print("---***************************ECHEC************************************************---")
        print("Désolé vous perdez ", montant_mise, "$ votre nouveau solde est", sommeInitiale, "$")
        #Si l'utilisateur n'a plus d'argent sur sont compte il est alors ruiné...
    if (sommeInitiale <= 0):
        print("---***************************ECHEC************************************************---")
        print("---*********************************************************************************---")
        print("---*********************************************************************************---")
        print("---***************************ECHEC************************************************---")
        question = input("Voulez-vous Quitter  O/N? \n ")
        question = str(question)
        if (question == 'O' or question == 'o'):

            print("Désolé "+nom+" vous etre ruiné, Merci de votre participation et à bientot....")
            startLevel = False
    else:
        print("Vous avez", sommeInitiale, "$")
        question = input("Voulez-vous Quitter  O/N? \n ")
        question = str(question)
        if (question == 'O' or question == 'o'):
            print("Aurevoir " + nom + " et merci d'avoir essayer Vous partez avec la somme de", sommeInitiale, "$")
            startLevel = False

os.system("pause")

