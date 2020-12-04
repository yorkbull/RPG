####################################################
# Fonctions du menu :

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
joueur1 = joueur()

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
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A3": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A4": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A5": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A6": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A7": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A8": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A9": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A10": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A11": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A12": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A13": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A14": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A15": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "A16": {
              NOMZONE : "",
              DESCRIPTION : "",
              HAUT : "",
              BAS : "",
              GAUCHE : "",
              DROITE : "",
          },
          "B1": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B2": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B3": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "3",
            DROITE : "",
          },
          "B4": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B5": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B6": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "1",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B7": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B8": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B9": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B10": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B11": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B12": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B13": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B14": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B15": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "B16": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "C1": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "Port Temple",
            BAS : "C5",
            GAUCHE : "Port B",
            DROITE : "C2",
          },
          "C2": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "C6",
            GAUCHE : "C1",
            DROITE : "C3",
          },
          "C3": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "C7",
            GAUCHE : "C2",
            DROITE : "C4",
          },
          "C4": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "C8",
            GAUCHE : "C3",
            DROITE : "",
          },
          "C5": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C1",
            BAS : "C9",
            GAUCHE : "",
            DROITE : "C6",
          },
          "C6": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C2",
            BAS : "C10",
            GAUCHE : "C5",
            DROITE : "C7",
          },
          "C7": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C3",
            BAS : "C11",
            GAUCHE : "C6",
            DROITE : "C8",
          },
          "C8": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C4",
            BAS : "C12",
            GAUCHE : "C7",
            DROITE : "",
          },
          "C9": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C5",
            BAS : "C13",
            GAUCHE : "",
            DROITE : "C10",
          },
          "C10": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C6",
            BAS : "C14",
            GAUCHE : "C9",
            DROITE : "C11",
          },
          "C11": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C7",
            BAS : "C15",
            GAUCHE : "C10",
            DROITE : "C12",
          },
          "C12": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C8",
            BAS : "C16",
            GAUCHE : "C11",
            DROITE : "",
          },
          "C13": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C9",
            BAS : "",
            GAUCHE : "",
            DROITE : "C14",
          },
          "C14": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C10",
            BAS : "",
            GAUCHE : "C13",
            DROITE : "C15",
          },
          "C15": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "C11",
            BAS : "",
            GAUCHE : "C14",
            DROITE : "C16",
          },
          "C16": {
            NOMZONE : "",
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
            GAUCHE : "",
            DROITE : "",
          },
          "P2": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "P3": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "P4": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "Temple": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          "Boss": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "",
            BAS : "",
            GAUCHE : "",
            DROITE : "",
          },
          

}

















Menu()