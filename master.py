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
  print("TODO Lancer le jeu")
  NomJoueur = Pseudo()
  while JeuxPasFini() :
    Description("essai")
    CibleMouvement = Mouvement()
    Event(CibleMouvement)

def ChargerPartie():
  print("TODO LoadGame")
  LancerLeJeux()

def Credits():
  print("TODO about")
  Menu()

def Quitter():
  print("TODO exit")


# Fonction de l'exploration :

def JeuxPasFini():
  print("TODO tester si le jeu est gagné ou perdu")
  return True

def Pseudo():
  Nom = str(input())
  print(Nom)
  return Nom

def Description(Lieu):
  print("TODO Afficher une description de où est le player")

def Mouvement():
  print("TODO Faire le deplacement du player")
  Lieu = "Lieu test"
  return Lieu

def Event(Lieu):
  print("TODO Combat ou Item qui se passe quand on se deplace")
  Combat()
  Item()

def Combat():
  print("TODO Combat")

def Item():
  print("TODO Item")


Menu()