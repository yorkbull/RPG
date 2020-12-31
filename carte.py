######################################################################################
# carte :

DESCRIPTION = "description"
HAUT = "haut", "up", "z"
BAS = "bas", "down", "s"
GAUCHE = "gauche", "left", "q"
DROITE = "droite", "right", "d"
ACTION = "action"



carte = {
          "petit village de pecheur": { #A1
              DESCRIPTION : "Bienvenue au pays du soleil levant jeune guerrier,est-tu prêt à affronter le pire de tout les dieux ? \n avant cela de nombreux combats et rencontres t'attendent... \n que ton nindo t'apporte la force nécessaire dans cette aventure",
              HAUT : "ravin",
              BAS : "Le fleuve Shinano-Gawa",
              GAUCHE : "ravin",
              DROITE : "Les Plaines d'Izuhara",
              ACTION : "None"
          },
          "Les Plaines d'Izuhara": { #A2
              DESCRIPTION : "blablabla",
              HAUT : "ravin",
              BAS : "Le donjon HIkone",
              GAUCHE : "petit village de pecheur",
              DROITE : "Okuno-in",
              ACTION : "combat" #
          },
          "Okuno-in": { #A3
              DESCRIPTION : "Te voici dans le plus grand cimetière japonais ",
              HAUT : "ravin",
              BAS : "Les Onsen",
              GAUCHE : "Les Plaines d'Izuhara",
              DROITE : "La Fôret Aokigahara",
              ACTION : "None"
          },
          "La Fôret Aokigahara": { #A4
              DESCRIPTION : "La Fôret des suicides où les esprits des gens morts ne passe pas l'au-delà",
              HAUT : "ravin",
              BAS : "Sanctuaire Shinto",
              GAUCHE : "Okuno-in",
              DROITE : "océan",
              ACTION : "combat"  # les yurei
          },
          "Le fleuve Shinano-Gawa": { #A5
              DESCRIPTION : "blabla",
              HAUT : "petit village de pecheur",
              BAS : "Les chutes de Fukuroda",
              GAUCHE : "ravin",
              DROITE : "Le donjon HIkone",
              ACTION : "combat"  # Le Kappa 
          },
          "Le donjon HIkone": { #A6
              DESCRIPTION : "En suivant le fleuve vous voici face au Donjour Hikone",
              HAUT : "Les Plaines d'Izuhara",
              BAS : "La fôret de Sagano",
              GAUCHE : "Le fleuve Shinano-Gawa",
              DROITE : "Les Onsen",
              ACTION : "None"
          },
          "Les Onsen": { #A7
              DESCRIPTION : "Te voici aux sources chaudes prenez un bain thermal pour récupérer de vos combats",
              HAUT : "Okuno-in",
              BAS : "Le Mont Fuji",
              GAUCHE : "Le donjon HIkone",
              DROITE : "Sanctuaire Shinto",
              ACTION : "maitre"  #redonne de l'HP max if HP max ALORS XP by Sensei Jiraya
          },
          "Sanctuaire Shinto": { #A8
              DESCRIPTION : "",
              HAUT : "La Fôret Aokigahara",
              BAS : "Les mines d'or de Sado",
              GAUCHE : "Les Onsen",
              DROITE : "océan",
              ACTION : "None"
          },
          "Les chutes de Fukuroda": { #A9
              DESCRIPTION : "",
              HAUT : "Le fleuve Shinano-Gawa",
              BAS : "Le Dojo",
              GAUCHE : "ravin",
              DROITE : "La fôret de Sagano",
              ACTION : "None"
          },
          "La fôret de Sagano": { #A10
              DESCRIPTION : "Tu entre dans la dense Fôret de Bambou où le seul moyen de la traverser est un sentier de briques éclairé par la lumière du jours",
              HAUT : "Le donjon HIkone",
              BAS : "La cité Milléniale",
              GAUCHE : "Les chutes de Fukuroda",
              DROITE : "Le Mont Fuji",
              ACTION : "None"
          },
          "Le Mont Fuji": { #A11
              DESCRIPTION : "",
              HAUT : "Les Onsen",
              BAS : "Le Lac Ashi",
              GAUCHE : "La fôret de Sagano",
              DROITE : "Les mines d'or de Sado",
              ACTION : "None"
          },
          "Les mines d'or de Sado": { #A12
              DESCRIPTION : "",
              HAUT : "Sanctuaire Shinto",
              BAS : "PLage de Shirahama",
              GAUCHE : "Le Mont Fuji",
              DROITE : "océan",
              ACTION : "None"
          },
          "Le Dojo": { #A13
              DESCRIPTION : "Bienvenue dans le Dojo où le maître Miyamoto Musashi vous attend avec impatience",
              HAUT : "Les chutes de Fukuroda",
              BAS : "océan",
              GAUCHE : "ravin",
              DROITE : "La cité Milléniale",
              ACTION : "None"
             #Miyamoto Musashi Xp + arme 
          },
          "La cité Milléniale": { #A14
              DESCRIPTION : "",
              HAUT : "La fôret de Sagano",
              BAS : "océan",
              GAUCHE : "Le Dojo",
              DROITE : "Le Lac Ashi",
              ACTION : "None"
          },
          "Le Lac Ashi": { #A15
              DESCRIPTION : "",
              HAUT : "Le Mont Fuji",
              BAS : "océan",
              GAUCHE : "La cité Milléniale",
              DROITE : "PLage de Shirahama",
              ACTION : "None"
          },
          "PLage de Shirahama": { #A16
              DESCRIPTION : "",
              HAUT : "Les mines d'or de Sado",
              BAS : "P2",
              GAUCHE : "Le Lac Ashi",
              DROITE : "P1",
              ACTION : "None"
          },
          "les Collines de Yangshuo": { #B1
            DESCRIPTION : "Vous voici entre les collines de Yangshuo plus communémant appelé les collines de la Lune",
            HAUT : "océan",
            BAS : "Les Chutes d'Eau Huangguoshu",
            GAUCHE : "ravin",
            DROITE : "La Vieille Ville sur l'eau de Fenghuang",
            ACTION : "None"
          },
          "La Vieille Ville sur l'eau de Fenghuang": { #B2
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "Le désert de Gobi",
            GAUCHE : "les Collines de Yangshuo",
            DROITE : "La Fôret de Xueling",
            ACTION : "None"
          },
          "La Fôret de Xueling": { #B3
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "La Vallée de Jiuzhaigou",
            GAUCHE : "La Vieille Ville sur l'eau de Fenghuang",
            DROITE : "Plage de Qingdao",
            ACTION : "None"
          },
          "Plage de Qingdao": { #B4
            DESCRIPTION : "",
            HAUT : "P2",
            BAS : "Les Montagnes du Tiashan",
            GAUCHE : "La Fôret de Xueling",
            DROITE : "P3",
            ACTION : "None"
          },
          "Les Chutes d'Eau Huangguoshu": { #B5
            DESCRIPTION : "",
            HAUT : "les Collines de Yangshuo",
            BAS : "Fleuve du Yangzi Jiang",
            GAUCHE : "ravin",
            DROITE : "Le désert de Gobi",
            ACTION : "None"
          },
          "Le désert de Gobi": { #B6
            DESCRIPTION : "",
            HAUT : "La Vieille Ville sur l'eau de Fenghuang",
            BAS : "La Cité Interdite",
            GAUCHE : "Les Chutes d'Eau Huangguoshu",
            DROITE : "La Vallée de Jiuzhaigou",
            ACTION : "None"
          },
          "La Vallée de Jiuzhaigou": { #B7
            DESCRIPTION : "",
            HAUT : "La Fôret de Xueling",
            BAS : "La Grande Muraille",
            GAUCHE : "Le désert de Gobi",
            DROITE : "Les Montagnes du Tiashan",
            ACTION : "None"
          },
          "Les Montagnes du Tiashan": { #B8
            DESCRIPTION : "",
            HAUT : "Plage de Qingdao",
            BAS : "Temple du Ciel Shaoline",
            GAUCHE : "La Vallée de Jiuzhaigou",
            DROITE : "océan",
            ACTION : "None"
          },
          "Fleuve du Yangzi Jiang": { #B9
            DESCRIPTION : "",
            HAUT : "Les Chutes d'Eau Huangguoshu",
            BAS : "Grand village de Pêcheur",
            GAUCHE : "ravin",
            DROITE : "La Cité Interdite",
            ACTION : "None"
          },
          "La Cité Interdite": { #B10
            DESCRIPTION : "",
            HAUT : "Le désert de Gobi",
            BAS : "Le Palais du Potala",
            GAUCHE : "Fleuve du Yangzi Jiang",
            DROITE : "La Grande Muraille",
            ACTION : "None"
          },
          "La Grande Muraille": { #B11
            DESCRIPTION : "",
            HAUT : "La Vallée de Jiuzhaigou",
            BAS : "Monastère des 10000 Bouddhas",
            GAUCHE : "La Cité Interdite",
            DROITE : "Temple du Ciel Shaoline",
            ACTION : "None"
          },
          "Temple du Ciel Shaoline": { #B12
            DESCRIPTION : "",
            HAUT : "Les Montagnes du Tiashan",
            BAS : "Les Falaises de Xuankong",
            GAUCHE : "La Grande Muraille",
            DROITE : "océan",
            ACTION : "None"
          },
          "Grand village de Pêcheur": { #B13
            DESCRIPTION : "",
            HAUT : "Fleuve du Yangzi Jiang",
            BAS : "ravin",
            GAUCHE : "ravin",
            DROITE : "Le Palais du Potala",
            ACTION : "None"
          },
          "Le Palais du Potala": { #B14
            DESCRIPTION : "",
            HAUT : "La Cité Interdite",
            BAS : "ravin",
            GAUCHE : "Grand village de Pêcheur",
            DROITE : "Monastère des 10000 Bouddhas",
            ACTION : "None"
          },
          "Monastère des 10000 Bouddhas": { #B15
            DESCRIPTION : "",
            HAUT : "La Grande Muraille",
            BAS : "ravin",
            GAUCHE : "Le Palais du Potala",
            DROITE : "Les Falaises de Xuankong",
            ACTION : "None"
          },
          "Les Falaises de Xuankong": { #B16
            DESCRIPTION : "",
            HAUT : "Temple du Ciel Shaoline",
            BAS : "ravin",
            GAUCHE : "Monastère des 10000 Bouddhas",
            DROITE : "océan",
            ACTION : "None"
          },
          "Plage de Raja Ampat": { #C1
            DESCRIPTION : "Plage de Raja Ampat",
            HAUT : "Port de Gili trawangan",
            BAS : "Le Sanctuaire de Candi Mendut",
            GAUCHE : "P3",
            DROITE : "La Jungle de Kawah Ijen",
            ACTION : "None"
          },
          "La Jungle de Kawah Ijen": { #C2
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "Les Grottes de Leang-Leang",
            GAUCHE : "Plage de Raja Ampat",
            DROITE : "La Cité des Singes",
            ACTION : "None"
          },
          "La Cité des Singes": { #C3
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "Les plaines du Dragon de Komodo",
            GAUCHE : "La Jungle de Kawah Ijen",
            DROITE : "Le Chateau des Démons",
            ACTION : "None"
          },
          "Le Chateau des Démons": { #C4
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "Les Ruines du Borobudur",
            GAUCHE : "La Cité des Singes",
            DROITE : "ravin",
            ACTION : "None"
          },
          "Le Sanctuaire de Candi Mendut": { #C5
            DESCRIPTION : "",
            HAUT : "Plage de Raja Ampat",
            BAS : "Les Montagnes de Bromo",
            GAUCHE : "océan",
            DROITE : "Les Grottes de Leang-Leang",
            ACTION : "None"
          },
          "Les Grottes de Leang-Leang": { #C6
            DESCRIPTION : "",
            HAUT : "La Jungle de Kawah Ijen",
            BAS : "Volcan du Krakatoa",
            GAUCHE : "Le Sanctuaire de Candi Mendut",
            DROITE : "Les plaines du Dragon de Komodo",
            ACTION : "None"
          },
          "Les plaines du Dragon de Komodo": { #C7
            DESCRIPTION : "",
            HAUT : "La Cité des Singes",
            BAS : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            GAUCHE : "Les Grottes de Leang-Leang",
            DROITE : "Les Ruines du Borobudur",
            ACTION : "None"
          },
          "Les Ruines du Borobudur": { #C8
            DESCRIPTION : "",
            HAUT : "Le Chateau des Démons",
            BAS : "La Fôret de Kalimantan",
            GAUCHE : "Les plaines du Dragon de Komodo",
            DROITE : "ravin",
            ACTION : "None"
          },
          "Les Montagnes de Bromo": { #C9
            DESCRIPTION : "",
            HAUT : "Le Sanctuaire de Candi Mendut",
            BAS : "Les Valées du Baliem",
            GAUCHE : "océan",
            DROITE : "Volcan du Krakatoa",
            ACTION : "None"
          },
          "Volcan du Krakatoa": { #C10
            DESCRIPTION : "",
            HAUT : "Les Grottes de Leang-Leang",
            BAS : "Le Village de Sulawesi",
            GAUCHE : "Les Montagnes de Bromo",
            DROITE : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            ACTION : "None"
          },
          "Les bassins d'eaux Sacrées de Pura Tirta Empul": { #C11
            DESCRIPTION : "",
            HAUT : "Les plaines du Dragon de Komodo",
            BAS : "Les Rizières de Jatiluwih",
            GAUCHE : "Volcan du Krakatoa",
            DROITE : "La Fôret de Kalimantan",
            ACTION : "None"
          },
          "La Fôret de Kalimantan": { #C12
            DESCRIPTION : "",
            HAUT : "Les Ruines du Borobudur",
            BAS : "Village de Pêcheur abandonné",
            GAUCHE : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            DROITE : "ravin",
            ACTION : "None"
          },
          "Les Valées du Baliem": { #C13
            DESCRIPTION : "",
            HAUT : "Les Montagnes de Bromo",
            BAS : "ravin",
            GAUCHE : "océan",
            DROITE : "Le Village de Sulawesi",
            ACTION : "None"
          },
          "Le Village de Sulawesi": { #C14
            DESCRIPTION : "",
            HAUT : "Volcan du Krakatoa",
            BAS : "ravin",
            GAUCHE : "Les Valées du Baliem",
            DROITE : "Les Rizières de Jatiluwih",
            ACTION : "None"
          },
          "Les Rizières de Jatiluwih": { #C15
            DESCRIPTION : "",
            HAUT : "Les bassins d'eaux Sacrées de Pura Tirta Empul",
            BAS : "ravin",
            GAUCHE : "Le Village de Sulawesi",
            DROITE : "Village de Pêcheur abandonné",
            ACTION : "None"
          },
          "Village de Pêcheur abandonné": { #C16
            DESCRIPTION : "",
            HAUT : "La Fôret de Kalimantan",
            BAS : "ravin",
            GAUCHE : "Les Rizières de Jatiluwih",
            DROITE : "ravin",
            ACTION : "None"
          },
          "P1": {
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "océan",
            GAUCHE : "PLage de Shirahama",
            DROITE : "Le Dernier Temple du Savoir",
            ACTION : "None"
          },
          "P2": {
            DESCRIPTION : "",
            HAUT : "PLage de Shirahama",
            BAS : "Plage de Qingdao",
            GAUCHE : "océan",
            DROITE : "océan",
            ACTION : "None"
          },
          "P3": {
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "océan",
            GAUCHE : "Plage de Qingdao",
            DROITE : "Plage de Raja Ampat",
            ACTION : "None"
          },
          "Port de Gili trawangan": { #P4
            DESCRIPTION : "",
            HAUT : "Le Dernier Temple du Savoir",
            BAS : "Plage de Raja Ampat",
            GAUCHE : "océan",
            DROITE : "océan",
            ACTION : "None"
          },
          "Le Dernier Temple du Savoir": { #Temple
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "Port de Gili trawangan",
            GAUCHE : "P1",
            DROITE : "Boss",
            ACTION : "None"
          },
          "Boss": {
            DESCRIPTION : "",
            HAUT : "océan",
            BAS : "océan",
            GAUCHE : "Temple",
            DROITE : "océan",
            ACTION : "None"
          },
}