import sys
import os
from random import randint
from carte import *
from monstre import *
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
  jeupasfini()

def ChargerPartie():
  print("TODO chargerpartir")


def Credits():
  print("dadadada")
  Menu()

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
        
def combatWin():
      print("")
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
      print("Que veux-tu faire?\n")
      print("aller")
      print("save")
      action = input("\n> ")
      acceptable_actions = ["aller", "combat", "parler" ,"fuir", "save", "quit"]
      while action.lower() not in acceptable_actions:
        print("Action inconnue, Essaye encore.\n")
        action = input("> ")
      if action.lower() in ["aller"]:
        move(action.lower())
      elif action.lower() in ["save"] or action.lower() in ["quit"]:
        save()
        Menu()

def save():
  print("save")

def AffichageAction ():
      if carte[joueur1.position][ACTION] == "combat":
            print("\n", monstre[joueur1.position][NOM], "vient d'apparaitre devant toi!")
            print("Il a", monstre[joueur1.position][HP], "de vie.\n")
            print("combat")
            print("fuir")
            print("save")
      elif carte[joueur1.position][ACTION] == "maitre":
            print("\nUn homme mysterieu s'avance devant toi.\n")
            print("parler")
            print("aller")
            print("save")
      else:
            print("aller")
            print("save")  
      
def GameOver():
      print("GAME OVER !")
      Menu()
###########################################################################
# Fonction de l'exploration :

def print_location():
    	# info de la position du joueur
    print("\n" + ("#" * (4 +len(joueur1.position))))
    print("# " + joueur1.position.upper() + " #")
    print("#" * (4 +len(joueur1.position)))
    print("\n" + (carte[joueur1.position][DESCRIPTION]))
    jeupasfini()

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
  if DeChoix <= 7:
        choixItem()
        Combat()
  else:
        Item()

def Combat():
      hpm = monstre[joueur1.position][HP]
      First = FirstBlood()
      i = 1
      while monstre[joueur1.position][HP] > 0:
            if First == True:
                  print("\nTour",i)
                  DeDeff = De10()
                  if DeDeff >= 7:
                        print(monstre[joueur1.position][NOM], "a esquivé votre attaque.")
                  else:
                        monstre[joueur1.position][HP] = (monstre[joueur1.position][HP] + monstre[joueur1.position][ATT]) - joueur1.ATTAQUE
                        print(monstre[joueur1.position][NOM],"a subi",joueur1.ATTAQUE, "de dégâts.")
                  DeDeff = De10()
                  if DeDeff >= 6:
                        print("Vous avez esquivé l'attaque.")
                  else:
                        joueur1.HP = (joueur1.HP + joueur1.DEFENSE) - monstre[joueur1.position][ATT]
                        print("Vous avez subi", monstre[joueur1.position][ATT], "de dégâts.")
                  print("Il te reste", joueur1.HP, "de vie.")
                  print("Il reste", monstre[joueur1.position][HP], "au", monstre[joueur1.position][NOM])
                  if monstre[joueur1.position][HP] == 0:
                        monstre[joueur1.position][HP] = hpm
                        Win()
                        combatWin()
                  elif joueur1.HP == 0:
                        GameOver()
            else:
                  print("\nTour",i)
                  DeDeff = De10()
                  if DeDeff >= 6:
                        print("Vous avez esquivé l'attaque.")
                  else:
                        joueur1.HP = (joueur1.HP + joueur1.DEFENSE) - monstre[joueur1.position][ATT]
                        print("Vous avez subi", monstre[joueur1.position][ATT], "de dégâts.")
                  DeDeff = De10()
                  if DeDeff >= 7:
                        print(monstre[joueur1.position][NOM], "a esquivé votre attaque.")
                  else:
                        monstre[joueur1.position][HP] = (monstre[joueur1.position][HP] + monstre[joueur1.position][ATT]) - joueur1.ATTAQUE
                        print(monstre[joueur1.position][NOM],"a subi",joueur1.ATTAQUE, "de dégâts.")
                  print("Il te reste", joueur1.HP, "de vie.")
                  print("Il reste", monstre[joueur1.position][HP], "au", monstre[joueur1.position][NOM])
                  if monstre[joueur1.position][HP] == 0:
                        monstre[joueur1.position][HP] = hpm
                        Win()
                        combatWin()
                  elif joueur1.HP == 0:
                        GameOver()
            i = i + 1                                                            

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
  DeItem = De10()
  if DeItem <= 5:
        if len(joueur1.INVENTAIRE[0]) >= 2:
              print("Tu n'a plus de place pour ce type de Bonus!")
              combatWin()
        else:   
              print("Tu a gagné un bonus d'attaque.")
              joueur1.INVENTAIRE[0].append("Bonus d'Attaque")
  else:
        if len(joueur1.INVENTAIRE[1]) >= 2:
              print("Tu n'a plus de place pour ce type de Bonus!")
              combatWin()
        else:
              print("Tu a gagné un bonus de Defense.")
              joueur1.INVENTAIRE[1].append("Bonus de Defense")
  combatWin()

def choixItem():
  print("\nUtilisez un Bonus pour le combat ?")
  print("\n oui / non ")
  choixI = str(input("> "))
  if choixI == "oui" or choixI == "o":
        print("Tu a", len(joueur1.INVENTAIRE[0]), "Bonus d'Attaque.")
        print("Tu a", len(joueur1.INVENTAIRE[1]), "Bonus de Defense.")
        Combat()
  elif choixI == "non" or choixI == "n":
        Combat()
  else:
        print("Je n'ai pas compris, recommence")
        choixI = str(input())



def master():
  print("maitre")
  

def De10():
  return randint(1,10)

def Win():
  print("\ngagné\n")
  print("TODO recompense")  

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
        print("\nFils Unique du plus grand de tout les samouraïs, \n cherche à devenir plus fort que son père et seul \n la quête vers le dieu yashin lui permettra d'y parvenir...") # depart A1
        print(carte["petit village de pecheur"][DESCRIPTION])
        return "petit village de pecheur"
    elif Pays == 2:
        print("\nEnfant orphelin de l'empire céleste,\n te voilà décidé à retrouver celui qui tua tes parents et toutes ta famille \n après des années d'entrainement te voilà pret avec un seul mot en bouche VENGEANCE")# depart B13
        print(carte["Grand village de Pêcheur"][DESCRIPTION])
        return "Grand village de Pêcheur"
    elif Pays == 3:
        print("\nLa seule chose que tu sais en te réveillant au beau milieu de ce village abndonné,\n n'est que ton nom et une voix te disant 'trouve Yashin et tu le saura' ") # depart C16
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
        self.INVENTAIRE = [[],[]]
        self.ARME = []
        self.won = False
joueur1 = joueur()



















Menu()


















Menu()
