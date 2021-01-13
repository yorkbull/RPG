###########################################################
#Monstre

NOM = "NOM"
DESCRIPTIF = "DESCRIPTIF"
HP = "HP"
ATT = "ATT"
DEF = "DEF"
RECOMPENSE = []

#MONSTRES JAPONAIS

monstre = { 
            "Les Plaines d'Izuhara": { #A2
                NOM : "Ronin",
                DESCRIPTIF : "Ce guerrier sans maître expert en Katana, défi quiconque foule les plaines d'Izuhara",
                HP : 50,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : ["Katana de ronin", 0, 0, 0, 20] 
            },

            "Okuno-in" : { #A3
                NOM : "Kasha",
                DESCRIPTIF : "être malveillant qui se rend aux cérémonies funèbres pour dérober les corps des défunts avant la crémation",
                HP : 15,
                ATT : 5,
                DEF : 10,
                RECOMPENSE : ["XP", 100, 0, 0, 0] 
            },
            
            "La Fôret Aokigahara" : { #A4
                NOM : "Le Yurei",
                DESCRIPTIF:"Fantômes de personnes qui se sont données la mort dans cette fôret ne pouvant trouver le chemin vers l'au-delà, \n espères trouver leur salut en volant l'ames des personnes s'aventurant dans celle-ci",
                HP : 50,
                ATT : 5,
                DEF : 25,
                RECOMPENSE : ["Potion HP", 0, 50, 0, 0]
            },
                       
            "Le fleuve Shinano-Gawa" : { #A5
                NOM : "Le Kappa",
                DESCRIPTIF:"l'Enfant de la rivière connu sous le nom de Kappa attire tout personnes proche du fleuve pour ensuite les noyer et les mangers.",
                HP : 25,
                ATT : 5,
                DEF : 0,
                RECOMPENSE : ["XP", 100, 0, 0, 0] 
            },

            "Le donjon HIkone" : { #A6
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None,
            },    

            "Les Onsen" : { #A7
                 NOM : "Jiraya",
                 DESCRIPTIF:"Maitre des grenouilles",
                 HP : 0,
                 ATT : 0,
                 DEF : 0,
                 RECOMPENSE : ["Armure d'expérience", 100, 0, 20, 0]
            },

            "Sanctuaire Shinto" : { # A8
                NOM : "Le Otoroshi", 
                DESCRIPTIF:"Le Otoroshi monstre recouvert de poil dont on voit seulement ces longues dents et ces griffes, gardien du sanctuaire vous laissera t-il y entrer ? ",
                HP : 90,
                ATT : 20,
                DEF : 90,
                RECOMPENSE : ["Fourrure de l'Otoroshi", 0, 0, 100, 0]
            },

            "Les chutes de Fukuroda" : { #A9
                NOM : "Le Nure-Onna",
                DESCRIPTIF:"La femme serpent humide",
                HP : 100,
                ATT : 30,
                DEF : 50,
                RECOMPENSE : ["Arme yumi serpent blanc", 0, 0, 50, 15]
            },

            "La fôret de Sagano" : { #Maitre  A10
                NOM : "Le Kodama",
                DESCRIPTIF:"Le Kodama esprit de la Fôret saura te guider dans ta quête du Dieu Yashin",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Armure spirituel de la foret de Bamboo", 0, 0, 50, 0]
            },
            
            "Le Mont Fuji" : { #A11
                NOM: "Kitsune",
                DESCRIPTIF:"Kitsune le fameux renard à 9 queues se cache pret du mont fuji et prend sa force de cette célèbre montagne",
                HP : 100,
                ATT : 40,
                DEF : 0,
                RECOMPENSE : ["La yari", 100, 0, 0, 25]

            },

            "Les mines d'or de Sado" : { #A12
                NOM : "Le Rokurokubi",
                DESCRIPTIF: "Têtes volante dévorant les êtres humains qui se perde dans leur mine",
                HP : 100,
                ATT : 25,
                DEF : 100,
                RECOMPENSE : ["xp", 100, 0, 0, 0]
            },
            
            "Le Dojo" : { #A13
                NOM : "Miyamamoto Musashi",
                DESCRIPTIF: "Miyamoto Musashi, de son vrai nom Shinmen Bennosuke \n est le plus grand de tout les combattants au corps a corps avec son sabre, \n il t'apprendra tout les rudiment du combat pour ne jamais perdre (ou presque) ",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["le Nodashi", 100, 0, 0, 40]
            },

            


#MONSTRES CHINOIS Beaucoup de Masters
            "les Collines de Yangshuo" : { #B1
                NOM :"Jin Chan",
                DESCRIPTIF: "Posé sur son nénuphare le crapaud d'or attend avec impatience de donner bonne fortune à un jeune guerrier... ",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["lotus d'expérience", 200, 0, 0, 5]
            },

            "La Vieille Ville de Fenghuang" : { # B2
                NOM : "Le Fenghuang",
                DESCRIPTIF: "Le Phoenix à 9 têtes autrement appelé la machine diabolique protège la ville de Fenghuang qui ose y entrer l'oiseau apparaît ",
                HP : 100,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : ["Boost de feu", 0, 50, 0, 0] 
            },

            "La Fôret de Xueling" : { #B3
                NOM : "Wukong",
                DESCRIPTIF: "Pour une Fôret de légende il faut un êtres qui la garde aussi légendaire.Inutile de le présenter...",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Baton de l'être divin wukong", 0, 0, 0, 25]
            },

            "Plage de Qingdao" : { #B4
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
            },

             "Les Chutes d'Eau Huangguoshu" : { #B5
                NOM : "Mogwai",
                DESCRIPTIF: "Le Mogwai être maléfique détestant l'être humain...vous savez quoi faire... ",
                HP : 90,
                ATT : 15,
                DEF : 10,
                RECOMPENSE : ["Dao", 100, 0, 0, 15]
            },

            "Le désert de Gobi" : { #B6
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
            },

            "La Vallée de Jiuzhaigou" : { #B7
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
            },

            "Les Montagnes du Tiashan" : { #B8
                NOM : "Long",
                DESCRIPTIF: "dans le fond de la Montagne du Tiashan se cache un dragon attention si vous le réveillé",
                HP : 25,
                ATT : 10,
                DEF : 100,
                RECOMPENSE : ["armure en écaille de dragons", 0, 0, 50, 0] 
            },

            "Fleuve du Yangzi Jiang" : { #B9
                NOM : "Baku",
                DESCRIPTIF: "Le léopard blanc Baku surveille quiconque ose regarder son fleuve et le mange tout cru",
                HP : 75,
                ATT : 15,
                DEF : 0,
                RECOMPENSE : ["Regard du délin", 0, 0, 0, 10]
            },

            "La Cité Interdite" : { #B10
                NOM : "Shi",
                DESCRIPTIF:"Shi est le lion de pierre qui garde la cité interdite prend vie si quiconque essaie d'entrer dans celle-ci",
                HP : 95,
                ATT : 2,
                DEF : 100,
                RECOMPENSE : ["Arme Fu", 100, 0, 0, 30]
            },

            "La Grande Muraille" : { #B11
                NOM : "Le dernier guerrier d'argile",
                DESCRIPTIF: "",
                HP : 15,
                ATT : 5,
                DEF : 20,
                RECOMPENSE : ["Lance du guerrier le Qiang", 0, 0, 0, 15]
            },
            
            "Temple du Ciel Shaoline" : { #B12 Maître
                NOM : "Moine Shaolin",
                DESCRIPTIF:"Un Maître Shaoline t'invite dans la 36ème Chambre pour t'inculqué les rudiments du combat des Moines Shaoline",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["baton de Shaoline", 100, 0, 20, 10] 
            },

            "Le Palais du Potala" : { #B14
                NOM : "Dalai lama",
                DESCRIPTIF: "En personne le Dalai Lama t'accueil, chef spirituel et temporel pour tout les tibétains.Tais-toi et médite",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Repos spirituel", 100, 20, 0, 0] 
            },

            "Monastère des 10000 Bouddhas" : { #B15
                NOM : "Guanyin",
                DESCRIPTIF: "La statue aux milles mains...attention aux baffes si tu ne répond pas bien...",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None,# réponse à une des enigmes ? 
    },
            "Les Falaises de Xuankong" : { #B16
                NOM : "Golem",
                DESCRIPTIF:"Géant de Pierre tel un Moaï sortant de sa falaise prêt à écraser tout les intrus  ",
                HP : 80,
                ATT : 5,
                DEF : 80,
                RECOMPENSE : ["Coeur du Golem", 50, 10, 0, 0]
    },

    ##### MOnstres et maitres indonesien

            "Plage de Raja Ampat" : { #C1
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
    },    

            "La Jungle de Kawah Ijen" : { #C2
                NOM : "Rangda",
                DESCRIPTIF: "LA reine des sorcières , \nmangeuse d'enfants attend qu'une chose est de tuer Barong, lui en empechera tu ?",
                HP : 100,
                ATT : 25,
                DEF : 50,
                RECOMPENSE : None, 
    },

            "La Cité des Singes" : { #C3
                NOM : "hanuman",
                DESCRIPTIF: "Diviné le dieu-singe, patron des lutteurs et des acrobates,\n des arts martiaux mais aussi dieu de la sagesse et de la méditation",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, #Maitre
    },

            "Le Chateau des Démons" : { #C4
                NOM : "Ravana",
                DESCRIPTIF: "Roi des démons et autrement appelé Dosomuko (démons a 10 têtes)\npossède dans son Kriss l'ame de ceux qu'il tue",
                HP : 75,
                ATT : 15,
                DEF : 35,
                RECOMPENSE : ["Kriss", 0, 0, 0, 15]
    },
            "Le Sanctuaire de Candi Mendut" : { #C5
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
    },

            "Les Grottes de Leang-Leang" : { #C6
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
    },
            "Les plaines du Dragon de Komodo" : { #C7
                NOM : "King Komodo",
                DESCRIPTIF: "King komodo le plus puissant , le plus grand de tout les dragons de komodo \n il a faim et il veut manger..de l'humain...",
                HP : 100,
                ATT : 20,
                DEF : 0,
                RECOMPENSE : None, 
    },

            "Les Ruines du Borobudur" : { #C8
                NOM : "Louis l'auran-outan",
                DESCRIPTIF: "Autrefois roi de ce temple il reste ici et garde son trésor, son reve etre un jour un homme",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Pendang en or", 0, 10, 10, 20] 
    },

            "Les Montagnes de Bromo" : { #C9
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
    },

            "Volcan du Krakatoa" : { #C10
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
    },

            "Les bassins d'eaux Sacrées de Pura Tirta Empul" : { #C11
                NOM : "Tigre de Sumatra",
                DESCRIPTIF: "Le gardien des bassins sacrées ne tolère pas qu'un être humain se baigne dans ce lieu...tu va en payer de ta vie.",
                HP : 30,
                ATT : 30,
                DEF : 0,
                RECOMPENSE : ["Griffe de tigre", 100, 10, 0, 0] 
    },

            "La Fôret de Kalimantan" : { #C12 maitre
                NOM : "Barong",
                DESCRIPTIF: "Ressemblant à un lion. Il est le seigneur de la forêt,\n chef des forces du bien et ennemi de Rangda..",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Esprit du Barong", 100, 10, 20, 0] 
    },

            "Les Valées du Baliem" : { #C13
                NOM : "Jatayu",
                DESCRIPTIF: "L'oiseau mystique veillant sur sa vallée ne te laissera pas y entrer sans permission...prepare toi...",
                HP : 50,
                ATT : 5,
                DEF : 50,
                RECOMPENSE : None, 
    },

            "Le Village de Sulawesi" : { #C14
                NOM : "Champion du village",
                DESCRIPTIF: "Le champion du village te défi à main nu dans ces montagne l'air manque,\n parviendra tu à le battre ?",
                HP : 25,
                ATT : 10,
                DEF : 25,
                RECOMPENSE : ["Karambit", 50, 0, 0, 10]
    },

            "Les Rizières de Jatiluwih" : { #C15
                NOM : "Agriculteur de riz",
                DESCRIPTIF: "l'agriculteur n'a rien sauf son bien le plus chere...son riz",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : ["Portion de riz", 0, 5, 0, 5]
    },

            "Village de Pêcheur abandonné" : { #C16
                NOM : "",
                DESCRIPTIF: "",
                HP : 0,
                ATT : 0,
                DEF : 0,
                RECOMPENSE : None, 
    },



}
       
