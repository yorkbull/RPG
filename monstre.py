###########################################################
#Monstre

NOM = "NOM"
DESCRIPTIF = "DESCRIPTIF"
HP = "HP"
ATT = "ATT"
DEF = "DEF"
RECOMPENSE = "RECOMPENSE"

#MONSTRES JAPONAIS

monstre = { 
            "Les Plaines d'Izuhara": { #A2
                NOM : "Ronin",
                DESCRIPTIF : "Ce guerrier sans maître expert en Katana, défi quiconque foule les plaines d'Izuhara",
                HP : 50,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : None, # Katana de Ronin 
            },
            "La Fôret Aokigahara" : { #A4
                NOM : "Le Yurei",
                DESCRIPTIF:"Fantômes de personnes qui se sont données la mort dans cette fôret ne pouvant trouver le chemin vers l'au-delà, \n espères trouver leur salut en volant l'ames des personnes s'aventurant dans celle-ci",
                HP : 50,
                ATT : 5,
                DEF : 25,
                RECOMPENSE : None, #potion de + 50 hp
            },
            
            "Okuno-in" : { #A3
                NOM : "Kasha",
                DESCRIPTIF : "être malveillant qui se rend aux cérémonies funèbres pour dérober les corps des défunts avant la crémation",
                HP : 15,
                ATT : 5,
                DEF : 10,
                RECOMPENSE : None,# Xp 
            },
            
            "Le fleuve Shinano-Gawa" : { #A5
                NOM : "Le Kappa",
                DESCRIPTIF:"l'Enfant de la rivière connu sous le nom de Kappa attire tout personnes proche du fleuve pour ensuite les noyer et les mangers.",
                HP : 25,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : None, #XP 
            },

            "La fôret de Sagano" : { #Maitre  A10
                NOM : "Le Kodama",
                DESCRIPTIF:"Le Kodama esprit de la Fôret saura te guider dans ta quête du Dieu Yashin",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, #Armure spirituel de la foret de Bamboo +50
            },
            "Sanctuaire Shinto" : { # A8
                NOM : "Le Otoroshi", 
                DESCRIPTIF:"Le Otoroshi monstre recouvert de poil dont on voit seulement ces longues dents et ces griffes, gardien du sanctuaire vous laissera t-il y entrer ? ",
                HP : 90,
                ATT : 20,
                DEF : 90,
                RECOMPENSE : None, # Fourrure de l'Otoroshi + 100 d'armure
            },

            "Les chutes de Fukuroda" : { #A9
                NOM : "Le Nure-Onna",
                DESCRIPTIF:"La femme serpent humide",
                HP : 100,
                ATT : 30,
                DEF : 50,
                RECOMPENSE : None, #XP + Arme yumi (arc) + Armure du serpent blanc
            },

            "Le Mont Fuji" : { #A11
                NOM: "Kitsune",
                DESCRIPTIF:"Kitsune le fameux renard à 9 queues se cache pret du mont fuji et prend sa force de cette célèbre montagne",
                HP : 100,
                ATT : 40,
                DEF : 0,
                RECOMPENSE : None, #XP + arme La yari + 25 dégats

            },

            "Les Onsen" : { #A7
                 NOM : "Jiraya",
                 DESCRIPTIF:"Maitre des grenouilles",
                 HP : 0,
                 ATT : 0,
                 DEF : 0,
                 RECOMPENSE : None, #XP + remises HP a 100 ou armure
            },

            "Le Dojo" : { #A13
                NOM : "Miyamamoto Musashi",
                DESCRIPTIF: "Miyamoto Musashi, de son vrai nom Shinmen Bennosuke \n est le plus grand de tout les combattants au corps a corps avec son sabre, \n il t'apprendra tout les rudiment du combat pour ne jamais perdre (ou presque) ",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None,#Arme le Nodashi + 40 dégats arme à 2 mains XP + Def Esquive 10
            },

            "Les mines d'or de Sado" : { #A12
                NOM : "Le Rokurokubi",
                DESCRIPTIF: "Têtes volante dévorant les êtres humains qui se perde dans leur mine",
                HP : 100,
                ATT : 25,
                DEF : 100,
                RECOMPENSE : None,
            },


#MONSTRES CHINOIS Beaucoup de Masters

            "La Cité Interdite" : { #B10
                NOM : "Shi",
                DESCRIPTIF:"Shi est le lion de pierre qui garde la cité interdite prend vie si quiconque essaie d'entrer dans celle-ci",
                HP : 95,
                ATT : 20,
                DEF : 100,
                RECOMPENSE : None, # XP + Arme Fu (Hache)
            },

            "Fleuve du Yangzi Jiang" : { #B9
                NOM : "Baku",
                DESCRIPTIF: "Le léopard blanc Baku surveille quiconque ose regarder son fleuve et le mange tout cru",
                HP : 75,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : None,# Boost de dégats de +Nu15

            },

            "Les Montagnes du Tiashan" : { #B8
                NOM : "Long",
                DESCRIPTIF: "dans le fond de la Montagne du Tiashan se cache un dragon attention si vous le réveillé",
                HP : 25,
                ATT : 10,
                DEF : 100,
                RECOMPENSE : None, # armure en écaille de dragons 
            },    

            "La Vieille Ville de Fenghuang" : { # B2
                NOM : "Le Fenghuang",
                DESCRIPTIF: "Le Phoenix à 9 têtes autrement appelé la machine diabolique protège la ville de Fenghuang qui ose y entrer l'oiseau apparaît ",
                HP : 100,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : None, # Objet Boost de feu 100 hp en plus pendant 1 combat 
    },

            "Temple du Ciel Shaoline" : { #B12 Maître
                NOM : "Moine Shaolin",
                DESCRIPTIF:"Un Maître Shaoline t'invite dans la 36ème Chambre pour t'inculqué les rudiments du combat des Moines Shaoline",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, #Arme : baton de Shaoline + XP , +Boost DEF endurcissement de la peau 
    },

            "Les Falaises de Xuankong" : { #B16
                NOM : "Golem",
                DESCRIPTIF:"Géant de Pierre tel un Moaï sortant de sa falaise prêt à écraser tout les intrus  ",
                HP : 80,
                ATT : 5,
                DEF : 80,
                RECOMPENSE : None,
    },

            "Monastère des 10000 Bouddhas" : { #B15
                NOM : "Guanyin",
                DESCRIPTIF: "La statue aux milles mains...attention aux baffes si tu ne répond pas bien...",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None,# réponse à une des enigmes ? 
    },

            "La Fôret de Xueling" : { #B3
                NOM : "Wukong",
                DESCRIPTIF: "Pour une Fôret de légende il faut un êtres qui la garde aussi légendaire.Inutile de le présenter...",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, #Arme Baton de l'être divin wukong dégât +25
    },

            "La Grande Muraille" : { #B11
                NOM : "Le dernier guerrier d'argile",
                DESCRIPTIF: "",
                HP : 15,
                ATT : 5,
                DEF : 20,
                RECOMPENSE : None, #Lance du guerrier le Qiang +10 de dégâts
    },    

            "Les Chutes d'Eau Huangguoshu" : { #B5
                NOM : "Mogwai",
                DESCRIPTIF: "Le Mogwai être maléfique détestant l'être humain...vous savez quoi faire... ",
                HP : 90,
                ATT : 15,
                DEF : 10,
                RECOMPENSE : None, #
       },               
}
       
