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
# map :

NOMZONE = ""
DESCRIPTION = ""


Menu()