import cmd
import textwrap
import sys
import os
import time
import random
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
    Quitter()

def LancerLeJeux():
  print("")
  print("Qu'elle est ton nom jeune guerrier ?")
  joueur1.nom = Pseudo()
  print("Tu a une tête bizarre , Tu viens d'ou ?")
  joueur1.position = choixpays()
  main_game_loop()

def ChargerPartie():
  print("TODO chargerpartir")
  LancerLeJeux()

def Credits():
  print("TODO credits")
  Menu()

def Quitter():
  print("TODO quitter")

def main_game_loop():
  joueur1.Boss == False
  while joueur1.won is False:
    #print_location()
    prompt()

def prompt():
  if joueur1.Boss == False:
    print("Something in the world seems to have changed. Hmm...")
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("What would you like to do?")
  action = input("> ")
  acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit']
  #Forces the player to write an acceptable sign, as this is essential to solving a puzzle later.
  while action.lower() not in acceptable_actions:
    print("Unknown action command, please try again.\n")
    action = input("> ")
  if action.lower() == quitgame:
    sys.exit()
  elif action.lower() in ['move', 'go', 'travel', 'walk']:
    move(action.lower())
  

###########################################################################
# Fonction de l'exploration :

def print_location():
    	# info de la position du joueur
	print('\n' + ('#' * (4 +len(joueur1.position))))
	print('# ' + joueur1.position.upper() + ' #')
	print('#' * (4 +len(joueur1.position)))
	print('\n' + (carte[joueur1.position][DESCRIPTION]))

def move(myAction):
  askString = "Where would you like to "+myAction+" to?\n> "
  destination = input(askString)
  if destination == 'haut':
    move_dest = carte[joueur1.position][HAUT] 
    move_player(move_dest)
  elif destination == 'gauche':
    move_dest = carte[joueur1.position][GAUCHE]
    move_player(move_dest)
  elif destination == 'droite':
    move_dest = carte[joueur1.position][DROITE]
    move_player(move_dest)
  elif destination == 'bas':
    move_dest = carte[joueur1.position][BAS]
    move_player(move_dest)
  else:
    print("Invalid direction command, try using forward, back, left, or right.\n")
    move(myAction)

def move_player(move_dest):
	print("\nYou have moved to the " + move_dest + ".")
	joueur1.position = move_dest
	print_location()


###########################################################################
# fonction de l'action ou item :

def Event(Lieu):
  print("TODO Combat ou Item qui se passe quand on se deplace")
  Combat()
  Item()

def Combat():
  print("TODO Combat")

def Item():
  print("TODO Item")

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
        return "A2"
    elif Pays == 3:
        print("histoire pays 3") # depart C16
        return "A3"
    else:
          print("Tu n'a pas compris la question ????")
          print("Je t'ai demander d'ou tu viens !!!!")
          choixpays()


####################################################################################
# Attribut du joueur au depart:

class joueur:
    def __init__(self):
        self.nom = ''
        self.HP = 100
        self.DEFENSE = 0
        self.ATTAQUE = 10
        self.position = ""
        self.INVENTAIRE = []
        self.ARME = []
        self.won = False
        self.Boss = False
joueur1 = joueur()

######################################################################################
# carte :

NOMZONE = ""
DESCRIPTION = ""
HAUT = "haut", "up", "z"
BAS = "bas", "down", "s"
GAUCHE = "gauche", "left", "q"
DROITE = "droite", "right", "d"
# Chine l'eau avec ces fleuves et cascades 
#Indonésie le Feu avec ces Volcans
#Japon air ? terre ? 
carte = {
          "A1": {
              NOMZONE : "petit vilage de pecheur",
              DESCRIPTION : "bla bla bla bla bla",
              HAUT : "",
              BAS : "A5",
              GAUCHE : "",
              DROITE : "A2",
          },
          "A2": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "A6",
              GAUCHE : "",
              DROITE : "A3",
          },
          "A3": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "A7",
              GAUCHE : "",
              DROITE : "A4",
          },
          "A4": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "A8",
              GAUCHE : "A3",
              DROITE : "",
          },
          "A5": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A1",
              BAS : "A9",
              GAUCHE : "",
              DROITE : "A6",
          },
          "A6": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A2",
              BAS : "A10",
              GAUCHE : "A5",
              DROITE : "A7",
          },
          "A7": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A3",
              BAS : "A11",
              GAUCHE : "A6",
              DROITE : "A8",
          },
          "A8": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A4",
              BAS : "A12",
              GAUCHE : "A7",
              DROITE : "",
          },
          "A9": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A5",
              BAS : "A13",
              GAUCHE : "",
              DROITE : "A10",
          },
          "A10": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A6",
              BAS : "A14",
              GAUCHE : "A9",
              DROITE : "A10",
          },
          "A11": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A7",
              BAS : "A15",
              GAUCHE : "A10",
              DROITE : "A12",
          },
          "A12": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A8",
              BAS : "A16",
              GAUCHE : "A11",
              DROITE : "",
          },
          "A13": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A9",
              BAS : "",
              GAUCHE : "",
              DROITE : "A14",
          },
          "A14": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A10",
              BAS : "",
              GAUCHE : "A13",
              DROITE : "A15",
          },
          "A15": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A11",
              BAS : "",
              GAUCHE : "A14",
              DROITE : "A16",
          },
          "A16": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "A12",
              BAS : "P2",
              GAUCHE : "A15",
              DROITE : "P1",
          },
          "B1": {
            NOMZONE : "les Collines de Yangshuo",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "B5",
            GAUCHE : "",
            DROITE : "B2",
          },
          "B2": {
            NOMZONE : "La Vieille Ville sur l'eau de Fenghuang",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "B6",
            GAUCHE : "B1",
            DROITE : "B3",
          },
          "B3": {
            NOMZONE : "La Fôret de Xueling",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "B7",
            GAUCHE : "B2",
            DROITE : "B4",
          },
          "B4": {
            NOMZONE : "Plage de Qingdao",
            DESCRIPTION : "",
            HAUT : "P2",
            BAS : "B8",
            GAUCHE : "B3",
            DROITE : "P3",
          },
          "B5": {
            NOMZONE : "Les Chutes d'Eau Huangguoshu",
            DESCRIPTION : "",
            HAUT : "B1",
            BAS : "B9",
            GAUCHE : "",
            DROITE : "B6",
          },
          "B6": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "B2",
            BAS : "B10",
            GAUCHE : "B5",
            DROITE : "B7",
          },
          "B7": {
            NOMZONE : "La Vallée de Jiuzhaigou",
            DESCRIPTION : "",
            HAUT : "B3",
            BAS : "B11",
            GAUCHE : "B6",
            DROITE : "B8",
          },
          "B8": {
            NOMZONE : "Les Montagnes du Tiashan",
            DESCRIPTION : "",
            HAUT : "B4",
            BAS : "B12",
            GAUCHE : "B7",
            DROITE : "",
          },
          "B9": {
            NOMZONE : "Fleuve du Yangzi Jiang",
            DESCRIPTION : "",
            HAUT : "B5",
            BAS : "B13",
            GAUCHE : "",
            DROITE : "B10",
          },
          "B10": {
            NOMZONE : "La Cité Interdite",
            DESCRIPTION : "",
            HAUT : "B6",
            BAS : "B14",
            GAUCHE : "B9",
            DROITE : "B11",
          },
          "B11": {
            NOMZONE : "La Grande Muraille",
            DESCRIPTION : "",
            HAUT : "B7",
            BAS : "B15",
            GAUCHE : "B10",
            DROITE : "B12",
          },
          "B12": {
            NOMZONE : "Temple du Ciel Shaoline",
            DESCRIPTION : "",
            HAUT : "B8",
            BAS : "B16",
            GAUCHE : "B11",
            DROITE : "",
          },
          "B13": {
            NOMZONE : "Village de Pêcheur",
            DESCRIPTION : "",
            HAUT : "B9",
            BAS : "",
            GAUCHE : "",
            DROITE : "B14",
          },
          "B14": {
            NOMZONE : "Le Palais du Potala ",
            DESCRIPTION : "",
            HAUT : "B10",
            BAS : "",
            GAUCHE : "B13",
            DROITE : "B15",
          },
          "B15": {
            NOMZONE : "Monastère des 10000 Bouddhas",
            DESCRIPTION : "",
            HAUT : "B11",
            BAS : "",
            GAUCHE : "B14",
            DROITE : "B16",
          },
          "B16": {
            NOMZONE : "Les Falaises de Xuankong",
            DESCRIPTION : "",
            HAUT : "B12",
            BAS : "",
            GAUCHE : "B15",
            DROITE : "",
          },
          "C1": {
            NOMZONE : "Plage de Raja Ampat",
            DESCRIPTION : "",
            HAUT : "P4",
            BAS : "C5",
            GAUCHE : "P3",
            DROITE : "C2",
          },
          "C2": {
            NOMZONE : "La Jungle de Kawah Ijen",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "C6",
            GAUCHE : "C1",
            DROITE : "C3",
          },
          "C3": {
            NOMZONE : "La Cité des Singes",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "C7",
            GAUCHE : "C2",
            DROITE : "C4",
          },
          "C4": {
            NOMZONE : "Le Chateau des Démons",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "C8",
            GAUCHE : "C3",
            DROITE : "",
          },
          "C5": {
            NOMZONE : "Le Sanctuaire de Candi Mendut",
            DESCRIPTION : "",
            HAUT : "C1",
            BAS : "C9",
            GAUCHE : "",
            DROITE : "C6",
          },
          "C6": {
            NOMZONE : "Les Grottes de Leang-Leang",
            DESCRIPTION : "",
            HAUT : "C2",
            BAS : "C10",
            GAUCHE : "C5",
            DROITE : "C7",
          },
          "C7": {
            NOMZONE : "Les plaines du Dragon de Komodo",
            DESCRIPTION : "",
            HAUT : "C3",
            BAS : "C11",
            GAUCHE : "C6",
            DROITE : "C8",
          },
          "C8": {
            NOMZONE : "Les Ruines du Borobudur",
            DESCRIPTION : "",
            HAUT : "C4",
            BAS : "C12",
            GAUCHE : "C7",
            DROITE : "",
          },
          "C9": {
            NOMZONE : "Les Montagnes de Bromo",
            DESCRIPTION : "",
            HAUT : "C5",
            BAS : "C13",
            GAUCHE : "",
            DROITE : "C10",
          },
          "C10": {
            NOMZONE : "Volcan du Krakatoa",
            DESCRIPTION : "",
            HAUT : "C6",
            BAS : "C14",
            GAUCHE : "C9",
            DROITE : "C11",
          },
          "C11": {
            NOMZONE : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            DESCRIPTION : "",
            HAUT : "C7",
            BAS : "C15",
            GAUCHE : "C10",
            DROITE : "C12",
          },
          "C12": {
            NOMZONE : "La Fôret de Kalimantan",
            DESCRIPTION : "",
            HAUT : "C8",
            BAS : "C16",
            GAUCHE : "C11",
            DROITE : "",
          },
          "C13": {
            NOMZONE : "Les Valées du Baliem",
            DESCRIPTION : "",
            HAUT : "C9",
            BAS : "",
            GAUCHE : "",
            DROITE : "C14",
          },
          "C14": {
            NOMZONE : "Le Village de Sulawesi",
            DESCRIPTION : "",
            HAUT : "C10",
            BAS : "",
            GAUCHE : "C13",
            DROITE : "C15",
          },
          "C15": {
            NOMZONE : "Les Rizières de Jatiluwih",
            DESCRIPTION : "",
            HAUT : "C11",
            BAS : "",
            GAUCHE : "C14",
            DROITE : "C16",
          },
          "C16": {
            NOMZONE : "Village de Pêcheur abandonné",
            DESCRIPTION : "",
            HAUT : "C12",
            BAS : "",
            GAUCHE : "C15",
            DROITE : "",
          },
          "P1": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "A16",
            DROITE : "Temple",
          },
          "P2": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "A16",
            BAS : "B4",
            GAUCHE : "",
            DROITE : "",
          },
          "P3": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "B4",
            DROITE : "C1",
          },
          "P4": {
            NOMZONE : "Port de Gili trawangan",
            DESCRIPTION : "",
            HAUT : "Temple",
            BAS : "C1",
            GAUCHE : "",
            DROITE : "",
          },
          "Temple": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "P4",
            GAUCHE : "P1",
            DROITE : "",
          },
          "Boss": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "Temple",
            DROITE : "",
          },
          

}

















Menu()