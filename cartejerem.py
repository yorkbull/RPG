######################################################################################
# carte :

NOMZONE = ""
DESCRIPTION = ""
HAUT = "haut", "up", "z"
BAS = "bas", "down", "s"
GAUCHE = "gauche", "left", "q"
DROITE = "droite", "right", "d"
MAITRE = ""
COMBAT = ""
DIALOGUE = ""
RECOMPENSE = ""

carte = {
          "A1": {
              NOMZONE : "petit vilage de pecheur",
              DESCRIPTION : "Bienvenue au pays du soleil levant jeune guerrier,est-tu prêt à affronter le pire de tout les dieux ? avant sela de nombreux combats et rencontres t'attendent...que ton nindo t'apporte la force nécessaire dans cette aventure",
              HAUT : "False",
              BAS : "A5",
              GAUCHE : "False",
              DROITE : "A2",
              MAITRE : "",
              COMBAT : "",
          },
          "A2": {
              NOMZONE : "Les Plaines d'Izuhara",
              DESCRIPTION : "",
              HAUT : "False",
              BAS : "A6",
              GAUCHE : "False",
              DROITE : "A3",
              MAITRE : "",
              COMBAT : "",
          },
          "A3": {
              NOMZONE : "Okuno-in",
              DESCRIPTION : "Te voici dans le plus grand cimetière japonais ",
              HAUT : "False",
              BAS : "A7",
              GAUCHE : "False",
              DROITE : "A4",
              MAITRE : "",
              COMBAT : "",
          },
          "A4": {
              NOMZONE : "La Fôret Aokigahara",
              DESCRIPTION : "La Fôret des suicides où les esprits des gens morts ne passe pas l'au-delà",
              HAUT : "False",
              BAS : "A8",
              GAUCHE : "A3",
              DROITE : "False",
              MAITRE : "",
              COMBAT : "true", #les yurei
          },
          "A5": {
              NOMZONE : "Le fleuve Shinano-Gawa",
              DESCRIPTION : "",
              HAUT : "A1",
              BAS : "A9",
              GAUCHE : "False",
              DROITE : "A6",
              COMBAT : "true", # Le Kappa 
          },
          "A6": {
              NOMZONE : "Le donjon HIkone",
              DESCRIPTION : "En suivant le fleuve vous voici face au Donjour Hikone",
              HAUT : "A2",
              BAS : "A10",
              GAUCHE : "A5",
              DROITE : "A7",
              MAITRE : "",
              COMBAT : "" ,
          },
          "A7": {
              NOMZONE : "Les Onsen",
              DESCRIPTION : "Te voici aux sources chaudes prenez un bain thermal pour récupérer de vos combats",
              HAUT : "A3",
              BAS : "A11",
              GAUCHE : "A6",
              DROITE : "A8",
              MAITRE : "True", #redonne de l'HP max if HP max ALORS XP by Sensei Jiraya
              DIALOGUE : "",
          },
          "A8": {
              NOMZONE : "Sanctuaire Shinto",
              DESCRIPTION : "",
              HAUT : "A4",
              BAS : "A12",
              GAUCHE : "A7",
              DROITE : "False",
              MAITRE : "",
              COMBAT : "",
          },
          "A9": {
              NOMZONE : "Les chutes de Fukuroda",
              DESCRIPTION : "",
              HAUT : "A5",
              BAS : "A13",
              GAUCHE : "False",
              DROITE : "A10",
              MAITRE : "",
              COMBAT : "",
          },
          "A10": {
              NOMZONE : "La fôret de Sagano",
              DESCRIPTION : "Tu entre dans la dense Fôret de Bambou où le seul moyen de la traverser est un sentier de briques éclairé par la lumière du jours",
              HAUT : "A6",
              BAS : "A14",
              GAUCHE : "A9",
              DROITE : "A10",
              MAITRE : "",
              COMBAT : "",
          },
          "A11": {
              NOMZONE : "Le Mont Fuji",
              DESCRIPTION : "",
              HAUT : "A7",
              BAS : "A15",
              GAUCHE : "A10",
              DROITE : "A12",
              MAITRE : "",
              COMBAT : "",
          },
          "A12": {
              NOMZONE : "Les mines d'or de Sado",
              DESCRIPTION : "",
              HAUT : "A8",
              BAS : "A16",
              GAUCHE : "A11",
              DROITE : "False",
              MAITRE : "",
              COMBAT : "",
          },
          "A13": {
              NOMZONE : "Le Dojo",
              DESCRIPTION : "Bienvenue dans le Dojo où le maître Miyamoto Musashi vous attend avec impatience",
              HAUT : "A9",
              BAS : "False",
              GAUCHE : "False",
              DROITE : "A14",
              MAITRE : "True" , #Miyamoto Musashi Xp + arme 
              DIALOGUE : "",
          },
          "A14": {
              NOMZONE : "La cité Milléniale ",
              DESCRIPTION : "",
              HAUT : "A10",
              BAS : "False",
              GAUCHE : "A13",
              DROITE : "A15",
              MAITRE : "",
              COMBAT : "",
          },
          "A15": {
              NOMZONE : "Le Lac Ashi",
              DESCRIPTION : "",
              HAUT : "A11",
              BAS : "False",
              GAUCHE : "A14",
              DROITE : "A16",
              MAITRE : "",
              COMBAT : "",
          },
          "A16": {
              NOMZONE : "PLage de Shirahama",
              DESCRIPTION : "",
              HAUT : "A12",
              BAS : "P2",
              GAUCHE : "A15",
              DROITE : "P1",
              MAITRE : "",
              COMBAT : "",
          },
          "B1": {
            NOMZONE : "les Collines de Yangshuo",
            DESCRIPTION : "Vous voici entre les collines de Yangshuo plus communémant appelé les collines de la Lune",
            HAUT : "False",
            BAS : "B5",
            GAUCHE : "False",
            DROITE : "B2",
            MAITRE : "",
            COMBAT : "",
          },
          "B2": {
            NOMZONE : "La Vieille Ville sur l'eau de Fenghuang",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "B6",
            GAUCHE : "B1",
            DROITE : "B3",
            MAITRE : "",
            COMBAT : "",
          },
          "B3": {
            NOMZONE : "La Fôret de Xueling",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "B7",
            GAUCHE : "B2",
            DROITE : "B4",
            MAITRE : "",
            COMBAT : "",
          },
          "B4": {
            NOMZONE : "Plage de Qingdao",
            DESCRIPTION : "",
            HAUT : "P2",
            BAS : "B8",
            GAUCHE : "B3",
            DROITE : "P3",
            MAITRE : "",
            COMBAT : "",
          },
          "B5": {
            NOMZONE : "Les Chutes d'Eau Huangguoshu",
            DESCRIPTION : "",
            HAUT : "B1",
            BAS : "B9",
            GAUCHE : "False",
            DROITE : "B6",
            MAITRE : "",
            COMBAT : "",
          },
          "B6": {
            NOMZONE : "Le désert de Gobi",
            DESCRIPTION : "",
            HAUT : "B2",
            BAS : "B10",
            GAUCHE : "B5",
            DROITE : "B7",
            MAITRE : "",
            COMBAT : "",
          },
          "B7": {
            NOMZONE : "La Vallée de Jiuzhaigou",
            DESCRIPTION : "",
            HAUT : "B3",
            BAS : "B11",
            GAUCHE : "B6",
            DROITE : "B8",
            MAITRE : "",
            COMBAT : "",
          },
          "B8": {
            NOMZONE : "Les Montagnes du Tiashan",
            DESCRIPTION : "",
            HAUT : "B4",
            BAS : "B12",
            GAUCHE : "B7",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "B9": {
            NOMZONE : "Fleuve du Yangzi Jiang",
            DESCRIPTION : "",
            HAUT : "B5",
            BAS : "B13",
            GAUCHE : "False",
            DROITE : "B10",
            MAITRE : "",
            COMBAT : "",
          },
          "B10": {
            NOMZONE : "La Cité Interdite",
            DESCRIPTION : "",
            HAUT : "B6",
            BAS : "B14",
            GAUCHE : "B9",
            DROITE : "B11",
            MAITRE : "",
            COMBAT : "",
          },
          "B11": {
            NOMZONE : "La Grande Muraille",
            DESCRIPTION : "",
            HAUT : "B7",
            BAS : "B15",
            GAUCHE : "B10",
            DROITE : "B12",
            MAITRE : "",
            COMBAT : "",
          },
          "B12": {
            NOMZONE : "Temple du Ciel Shaoline",
            DESCRIPTION : "",
            HAUT : "B8",
            BAS : "B16",
            GAUCHE : "B11",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "B13": {
            NOMZONE : "Village de Pêcheur",
            DESCRIPTION : "",
            HAUT : "B9",
            BAS : "False",
            GAUCHE : "False",
            DROITE : "B14",
            MAITRE : "",
            COMBAT : "",
          },
          "B14": {
            NOMZONE : "Le Palais du Potala",
            DESCRIPTION : "",
            HAUT : "B10",
            BAS : "False",
            GAUCHE : "B13",
            DROITE : "B15",
            MAITRE : "",
            COMBAT : "",
          },
          "B15": {
            NOMZONE : "Monastère des 10000 Bouddhas",
            DESCRIPTION : "",
            HAUT : "B11",
            BAS : "False",
            GAUCHE : "B14",
            DROITE : "B16",
            MAITRE : "",
            COMBAT : "",
          },
          "B16": {
            NOMZONE : "Les Falaises de Xuankong",
            DESCRIPTION : "",
            HAUT : "B12",
            BAS : "False",
            GAUCHE : "B15",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "C1": {
            NOMZONE : "",
            DESCRIPTION : "Plage de Raja Ampat",
            HAUT : "P4",
            BAS : "C5",
            GAUCHE : "P3",
            DROITE : "C2",
            MAITRE : "",
            COMBAT : "",
          },
          "C2": {
            NOMZONE : "La Jungle de Kawah Ijen",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "C6",
            GAUCHE : "C1",
            DROITE : "C3",
            MAITRE : "",
            COMBAT : "",
          },
          "C3": {
            NOMZONE : "",
            DESCRIPTION : "La Cité des Singes",
            HAUT : "False",
            BAS : "C7",
            GAUCHE : "C2",
            DROITE : "C4",
            MAITRE : "",
            COMBAT : "",
          },
          "C4": {
            NOMZONE : "Le Chateau des Démons",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "C8",
            GAUCHE : "C3",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "C5": {
            NOMZONE : "Le Sanctuaire de Candi Mendut",
            DESCRIPTION : "",
            HAUT : "C1",
            BAS : "C9",
            GAUCHE : "False",
            DROITE : "C6",
            MAITRE : "",
            COMBAT : "",
          },
          "C6": {
            NOMZONE : "Les Grottes de Leang-Leang",
            DESCRIPTION : "",
            HAUT : "C2",
            BAS : "C10",
            GAUCHE : "C5",
            DROITE : "C7",
            MAITRE : "",
            COMBAT : "",
          },
          "C7": {
            NOMZONE : "Les plaines du Dragon de Komodo",
            DESCRIPTION : "",
            HAUT : "C3",
            BAS : "C11",
            GAUCHE : "C6",
            DROITE : "C8",
            MAITRE : "",
            COMBAT : "",
          },
          "C8": {
            NOMZONE : "Les Ruines du Borobudur",
            DESCRIPTION : "",
            HAUT : "C4",
            BAS : "C12",
            GAUCHE : "C7",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "C9": {
            NOMZONE : "Les Montagnes de Bromo",
            DESCRIPTION : "",
            HAUT : "C5",
            BAS : "C13",
            GAUCHE : "False",
            DROITE : "C10",
            MAITRE : "",
            COMBAT : "",
          },
          "C10": {
            NOMZONE : "Volcan du Krakatoa",
            DESCRIPTION : "",
            HAUT : "C6",
            BAS : "C14",
            GAUCHE : "C9",
            DROITE : "C11",
            MAITRE : "",
            COMBAT : "",
          },
          "C11": {
            NOMZONE : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            DESCRIPTION : "",
            HAUT : "C7",
            BAS : "C15",
            GAUCHE : "C10",
            DROITE : "C12",
            MAITRE : "",
            COMBAT : "",
          },
          "C12": {
            NOMZONE : "La Fôret de Kalimantan",
            DESCRIPTION : "",
            HAUT : "C8",
            BAS : "C16",
            GAUCHE : "C11",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "C13": {
            NOMZONE : "Les Valées du Baliem",
            DESCRIPTION : "",
            HAUT : "C9",
            BAS : "False",
            GAUCHE : "False",
            DROITE : "C14",
            MAITRE : "",
            COMBAT : "",
          },
          "C14": {
            NOMZONE : "Le Village de Sulawesi",
            DESCRIPTION : "",
            HAUT : "C10",
            BAS : "False",
            GAUCHE : "C13",
            DROITE : "C15",
            MAITRE : "",
            COMBAT : "",
          },
          "C15": {
            NOMZONE : "Les Rizières de Jatiluwih",
            DESCRIPTION : "",
            HAUT : "C11",
            BAS : "False",
            GAUCHE : "C14",
            DROITE : "C16",
            MAITRE : "",
            COMBAT : "",
          },
          "C16": {
            NOMZONE : "Village de Pêcheur abandonné",
            DESCRIPTION : "",
            HAUT : "C12",
            BAS : "False",
            GAUCHE : "C15",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "P1": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "False",
            GAUCHE : "A16",
            DROITE : "Temple",
            MAITRE : "",
            COMBAT : "",
          },
          "P2": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "A16",
            BAS : "B4",
            GAUCHE : "False",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "P3": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "False",
            GAUCHE : "B4",
            DROITE : "C1",
            MAITRE : "",
            COMBAT : "",
          },
          "P4": {
            NOMZONE : "Port de Gili trawangan",
            DESCRIPTION : "",
            HAUT : "Temple",
            BAS : "C1",
            GAUCHE : "False",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "Temple": {
            NOMZONE : "Le Dernier Temple du Savoir",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "P4",
            GAUCHE : "P1",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          "Boss": {
            NOMZONE : "",
            DESCRIPTION : "",
            HAUT : "False",
            BAS : "False",
            GAUCHE : "Temple",
            DROITE : "False",
            MAITRE : "",
            COMBAT : "",
          },
          

}