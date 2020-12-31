import sys
import os
from random import randint
from carte import *
screen_width = 100



####################################################
# Fonctions du menu :
def Menu():
  Title()
  print("                                       --------------------------------")
  print("                                             1: Nouvelle partie")
  print("                                             2: Charger partie")
  print("                                             3: Credits")
  print("                                             4: Quitter")
  print("                                        -------------------------------")
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
  print("\nQu'elle est ton nom jeune guerrier ?\n")
  joueur1.nom = Pseudo()
  print("\nTu a une tête bizarre , Tu viens d'ou ?")
  joueur1.position = choixpays()
  main_game_loop()

def ChargerPartie():
  print("TODO chargerpartir")


def Credits():
  print("TODO credits")
  Menu()

def main_game_loop():
  while joueur1.won is False:
    jeupasfini()

def jeupasfini():
  print("")
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  print("Que veux-tu faire?\n")
  AffichageAction()
  action = input("\n> ")
  acceptable_actions = ["aller", "combat", "parler" ,"fuir", "save", "quit"]
  while action.lower() not in acceptable_actions:
    print("Action inconnue, Essaye encore.\n")
    action = input("> ")
  if action.lower() in ["aller"]:
    move(action.lower())
  elif action.lower() in ["combat"]:
    Event()
  elif action.lower() in ["fuir"]:
    move(action.lower())
  elif action.lower() in ["parler"]:
    master()
  elif action.lower() in ["save"] or action.lower() in ["quit"]:
    save()
    Menu()
        


def save():
  print("save")

def AffichageAction ():
      if carte[joueur1.position][ACTION] == "combat":
            print("combat")
            print("fuir")
            print("save")
      elif carte[joueur1.position][ACTION] == "maitre":
            print("parler")
            print("aller")
            print("save")
      else:
            print("aller")
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
  print("\nhaut   ->   " + (carte[joueur1.position][HAUT] ))
  print("bas      ->   " + (carte[joueur1.position][BAS] ))
  print("gauche   ->   " + (carte[joueur1.position][GAUCHE] ))
  print("droite   ->   " + (carte[joueur1.position][DROITE] ))

  askString = "\nOu veux-tu "+myAction+"?\n> "
  destination = input(askString)
  if destination == "haut":
    move_dest = carte[joueur1.position][HAUT]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction) 
    move_player(move_dest)   
  elif destination == "gauche":
    move_dest = carte[joueur1.position][GAUCHE]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction)
    move_player(move_dest)
  elif destination == "droite":
    move_dest = carte[joueur1.position][DROITE]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction)
    move_player(move_dest)
  elif destination == "bas":
    move_dest = carte[joueur1.position][BAS]
    if move_dest == "ravin" or move_dest == "océan":
      print("tu va dans le mur")
      print("choisi un autre chemin.")
      move(myAction)
    move_player(move_dest)
  else:
    print("Je ne comprend pas, essaye haut, bas, gauche, ou droite.\n")
    move(myAction)

def move_player(move_dest):
	joueur1.position = move_dest
	print_location()

###########################################################################
# fonction de l'action ou item :


def Event():
  DeChoix = De10()
  if DeChoix <= 5:
        Combat()
  else:
        Item()

def Combat():
      First = FirstBlood()
      DeAtt = De10()


def FirstBlood():
      DeFirst = De10()
      if DeFirst <= 5:
            print("\nVous attaquez en premier")
            return True
      else:
            print("\nCe monstre est rapide, il a devancé ton attaque")
            return False

def Item():
  print("TODO Item")

def master():
  print("master")

def De10():
  return randint(1,10)  

###########################################################################
# intro :

def Pseudo():
  Nom = str(input(">"))
  print("\nBienvenu", Nom)
  return Nom

def choixpays():
    print("\njapon, tapez 1")
    print("chine, tapez 2")
    print("indonésie, tapez 3\n")
    Pays = int(input(">"))
    if Pays == 1:
        print("\nhistoire pays 1") # depart A1
        print(carte["petit village de pecheur"][DESCRIPTION])
        return "petit village de pecheur"
    elif Pays == 2:
        print("\nhistoire pays 2") # depart B13
        print(carte["Grand village de Pêcheur"][DESCRIPTION])
        return "Grand village de Pêcheur"
    elif Pays == 3:
        print("\nhistoire pays 3") # depart C16
        print(carte["Village de Pêcheur abandonné"][DESCRIPTION])
        return "Village de Pêcheur abandonné"
    else:
          print("\nTu n'a pas compris la question ????")
          print("\nJe t'ai demander d'ou tu viens !!!!")
          choixpays()

def Title():
    print("                    __     __      _____ _     _          ____                  _")   
    print("                    \ \   / /     / ____| |   (_)        / __ \                | |")  
    print("                     \ \_/ /_ _  | (___ | |__  _ _ __   | |  | |_   _  ___  ___| |_") 
    print("                      \   / _` |  \___ \| '_ \| | '_ \  | |  | | | | |/ _ \/ __| __|")
    print("                       | | (_| |  ____) | | | | | | | | | |__| | |_| |  __/\__ \ |_") 
    print("                       |_|\__,_| |_____/|_| |_|_|_| |_|  \___\_\\__,_|\___||___/\__|")
####################################################################################
# Attribut du joueur au depart:

class joueur:
    def __init__(self):
        self.nom = ""
        self.XP = 0
        self.HP = 100
        self.DEFENSE = 0
        self.ATTAQUE = 10
        self.position = ""
        self.INVENTAIRE = []
        self.ARME = []
        self.won = False
joueur1 = joueur()



















Menu()
