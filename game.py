import sys
import os
from random import randint
from carte import *
screen_width = 100



####################################################
# Fonctions du menu :
quitgame = "quit" 
def Menu():
    print("                                                     --------------------------------")
    print("                                                           1: Nouvelle partie")
    print("                                                           2: Charger partie")
    print("                                                           3: Credits")
    print("                                                           4: Quitter")
    print("                                                      -------------------------------")
    Choix = int(input(">"))
    if Choix == 1:
        LancerLeJeux()
    elif Choix == 2:
        ChargerPartie()
    elif Choix == 3:
        Credits()
    else:
        sys.exit()

def LancerLeJeux():
    print("")
    print("Qu'elle est ton nom jeune guerrier ?")
    joueur1.nom = Pseudo()
    print("Tu a une tête bizarre , Tu viens d'ou ?")
    joueur1.position = choixpays()
    print(carte[joueur1.position][DESCRIPTION])
    main_game_loop()

def ChargerPartie():
    print("TODO chargerpartir")


def Credits():
    print("TODO credits")
    Menu()

def main_game_loop():
    joueur1.Boss == False
    while joueur1.won is False:
        jeupasfini()

def jeupasfini():
    if joueur1.Boss == False:
        print("Ne présume pas de tes forces, entraine toi encore !!!!")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Que veux-tu faire?")
    print("aller")
    print("quit")
    maitre = carte[joueur1.position][MAITRE]
    combat = carte[joueur1.position][COMBAT]
    if combat == True:
        print("un" + carte[joueur1.position][NONMONSTRE] + "vient d'apparaitre devant toi!")
        print("combat") # rajouter print du nom du maitre
    elif maitre == True:
        print("parler")
    action = input("> ")
    acceptable_actions = ["aller", "combat", "parler" ,"quit", "save"]
    while action.lower() not in acceptable_actions:
        print("Action inconnue, Essaye encore.\n")
        action = input("> ")
    if action.lower() == quitgame:
        save()
    elif action.lower() in ["aller"]:
        move(action.lower())
    elif action.lower() in ["combat"]:
        Event()
    elif action.lower() in ["parler"]:
        master()


def save():
    print("save")

###########################################################################
# Fonction de l'exploration :

def print_location():
    	# info de la position du joueur
    print("\n" + ("#" * (4 +len(joueur1.position))))
    print("# " + joueur1.position.upper() + " #")
    print("#" * (4 +len(joueur1.position)))
    print("\n" + (carte[joueur1.position][DESCRIPTION]))

def move(myAction):
    print(">haut    :     " + (carte[joueur1.position][HAUT] ))
    print(">bas     :     " + (carte[joueur1.position][BAS] ))
    print(">gauche  :     " + (carte[joueur1.position][GAUCHE] ))
    print(">droite  :     " + (carte[joueur1.position][DROITE] ))
    print("               ")
    askString = "Ou veux-tu "+myAction+"?\n> "
    destination = input(askString)
    if destination == "haut":
        move_dest = carte[joueur1.position][HAUT]
        if move_dest == "ravin" or move_dest == "océan":
            print("c'est une voie sans issu, fais demi-tour")
            print("choisi un autre chemin.")
            move(myAction) 
        move_player(move_dest)   
    elif destination == "gauche":
        move_dest = carte[joueur1.position][GAUCHE]
        if move_dest == "ravin" or move_dest == "océan":
            print("c'est une voie sans issu, fais demi-tour")
            print("choisi un autre chemin.")
            move(myAction)
        move_player(move_dest)
    elif destination == "droite":
        move_dest = carte[joueur1.position][DROITE]
        if move_dest == "ravin" or move_dest == "océan":
            print("c'est une voie sans issu, fais demi-tour")
            print("choisi un autre chemin.")
            move(myAction)
        move_player(move_dest)
    elif destination == "bas":
        move_dest = carte[joueur1.position][BAS]
        if move_dest == "ravin" or move_dest == "océan":
            print("c'est une voie sans issu, fais demi-tour")
            print("choisi un autre chemin.")
            move(myAction)
        move_player(move_dest)
    else:
        print("Je ne comprend pas, essaye haut, bas, gauche, ou droite.\n")
        move(myAction)

def move_player(move_dest):
    print("\nTu est en " + move_dest + ".")
    joueur1.position = move_dest
    print_location()


###########################################################################
# fonction de l'action ou item :



def Event():
    De = De6()
    if De < 5:
        Combat()
    else:
        Item()

def Combat():
    print(carte[joueur1.position][NONMONSTRE]) 
    print(carte[joueur1.position][DESCRIPTIONMONSTRE]) 
    print("que veux-tu faire ?")
    print("combat \n  item  \n  quit")
    action = input("> ")
    acceptable_actions = ["combat", "item" ,"fuir"]
    while action.lower() not in acceptable_actions:
        print("Action inconnue, Essaye encore.\n")
        action = input("> ")
    if action.lower() in ["combat"]:
        TourParTour()
    elif action.lower() in ["item"]:
        print(joueur1.INVENTAIRE)
    elif action.lower() in ["fuir"]:
        print("Fiotte!")
        main_game_loop()

def TourParTour():      
    FirstAttack = DeFirstBlood()
    if FirstAttack == True:
        i = 1
        while carte[joueur1.position][HP] > 0:
            if joueur1.HP == 0:
                GameOver()
            else:
                Fight = defDe10()
                if Fight == True:
                    carte[joueur1.position][HP] = (joueur1.ARME + joueur1.ATTAQUE) - (carte[joueur1.position][HP] + carte[joueur1.position][DEF])
                    print("Tour " + i)
                    print(carte[joueur1.position][NONMONSTRE] + " a subi " + (joueur1.ARME + joueur1.ATTAQUE) + "de dégats")
                else:
                    print("Tour " + i)
                    print("il a bloqué ton attaque")
                Fight = defDe10()
                if Fight == True:
                    joueur1.HP = carte[joueur1.position][ATT] - (joueur1.HP + joueur1.DEFENSE)
                    print("Tour " + i)
                    print("Tu a subi" + carte[joueur1.position] + "de dégats")
                else:
                    print("Tour " + i)
                    print("Tu a bloqué ton attaque")
        i = i + 1                  
    else:
        i = 0
        while carte[joueur1.position][HP] > 0:
            if joueur1.HP == 0:
                GameOver()
            else:
                Fight = defDe10()
                if Fight == True:
                    joueur1.HP = carte[joueur1.position][ATT] - (joueur1.HP + joueur1.DEFENSE)
                    print("Tour 1")
                    print("Tu a subi" + carte[joueur1.position] + "de dégats")
                else:
                    print("Tour 1")
                    print("Tu a bloqué ton attaque")
                Fight = defDe10()
                if Fight == True:
                    carte[joueur1.position][HP] = (joueur1.ARME + joueur1.ATTAQUE) - (carte[joueur1.position][HP] + carte[joueur1.position][DEF])
                    print("Tour " + i)
                    print(carte[joueur1.position][NONMONSTRE] + " a subi " + (joueur1.ARME + joueur1.ATTAQUE) + "de dégats")
                else:
                    print("Tour " + i)
                    print("il a bloqué ton attaque")
        i = i + 1
       
def DeFirstBlood():
    print("Tour")
    De = De6()
    if De < 4 :
        print("Tu attaque en premier")
        return True
    else:
        print("Il a été plus rapide que toi pour lancer le combat")
        return False

def Item():
    print("TODO Item")

def master():
    print("master")

def defDe10():
    ResultatDe10 = De10()
    if ResultatDe10 < 6 :
        return True


def GameOver():
    print("GAME OVER")


#############################################################################
############################# Dé

def De6():
    return randint(1,6)

def De10():
    return randint(1,10)



###########################################################################
# intro :

def Pseudo():
    Nom = str(input(">"))
    print("Bienvenu",Nom)
    return Nom

def choixpays():
    print("japon, tapez 1")
    print("chine, tapez 2")
    print("indonésie, tapez 3")
    Pays = int(input(">"))
    if Pays == 1:
        print("histoire pays 1") # depart A1
        return "A1"
    elif Pays == 2:
        print("histoire pays 2") # depart B13
        return "B13"
    elif Pays == 3:
        print("histoire pays 3") # depart C16
        return "C16"
    else:
        print("Tu n'a pas compris la question ????")
        print("Je t'ai demander d'ou tu viens !!!!")
        choixpays()


####################################################################################
# Attribut du joueur au depart:

class joueur:
    def __init__(self):
        self.nom = ""
        self.HP = 100
        self.DEFENSE = 0
        self.ATTAQUE = 10
        self.position = ""
        self.INVENTAIRE = []
        self.ARME = []
        self.won = True
        self.Boss = False
joueur1 = joueur()



















Menu()