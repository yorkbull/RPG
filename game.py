####################################################
# Fonctions du menu :

def Menu():
  print("                                                     --------------------------------")
  print("                                                           1: Nouvelle partie")
  print("                                                           2: Charger partie")
  print("                                                           3: Credits")
  print("                                                           4: Quitter")
  print("                                                      -------------------------------")
  Choix = int(input())
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
  NomJoueur = Pseudo()
  print("Tu a une tête bizarre , Tu viens d'ou ?")
  Depart = choixpays()
  print(Depart)

def ChargerPartie():
  print("TODO chargerpartir")
  LancerLeJeux()

def Credits():
  print("TODO credits")
  Menu()

def Quitter():
  print("TODO quitter")

###########################################################################
# Fonction de l'exploration :

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
  Nom = str(input())
  print("Bienvenu",Nom)
  return Nom

def choixpays():
    print("japon, tapez 1")
    print("chine, tapez 2")
    print("indonésie, tapez 3")
    Pays = int(input())
    if Pays == 1:
        print("histoire pays 1") # depart A1
        return Pays
    elif Pays == 2:
        print("histoire pays 2") # depart B13
        return Pays
    elif Pays == 3:
        print("histoire pays 3") # depart C16
        return Pays
    else:
          print("Tu n'a pas compris la question ????")
          print("Je t'ai demander d'ou tu viens !!!!")
          choixpays()


####################################################################################
# Attribut du joueur au depart:

class player:
    def __init__(self):
        self.name = ''
        self.HP = 100
        self.DEFENSE = 0
        self.ATTAQUE = 10
        self.position = ""
        self.INVENTAIRE = []
        self.ARME = []
        self.won = False
player1 = player()

######################################################################################
# carte :

NOMZONE = ""
DESCRIPTION = ""
HAUT = "haut", "up", "1"
BAS = "bas", "down", "2"
GAUCHE = "gauche", "left", "3"
DROITE = "droite", "right", "4"

carte = {
          "A1": {
            NOMZONE = "petit vilage de pecheur"
            DESCRIPTION = ""
            HAUT = ""
            BAS = "A5"
            GAUCHE = ""
            DROITE = "A2"
          }
          "A2": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A3": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A4": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A5": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A6": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A7": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A8": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A9": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A10": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A11": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A12": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A13": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A14": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A15": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "A16": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B1": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B2": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B3": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B4": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B5": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B6": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B7": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B8": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B9": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B10": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B11": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B12": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B13": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B14": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B15": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "B16": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C1": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C2": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C3": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C4": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C5": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C6": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
          "C7": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C8": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C9": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C10": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C11": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C12": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C13": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C14": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C15": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"C16": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"P1": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"P2": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"P3": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"P4": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"Temple": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }"Boss": {
            NOMZONE = ""
            DESCRIPTION = ""
            HAUT = "haut", "up", "1"
            BAS = "bas", "down", "2"
            GAUCHE = "gauche", "left", "3"
            DROITE = "droite", "right", "4"
          }
}

















Menu()