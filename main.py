from mineral import Mineral
from collection import Collection
from couleur_rgb import CouleurRGB
import re




def batir_collection():
    '''Crée une collection de minéraux hard-codée'''
    #Ces minéraux ont été décrits par ChatGPT
    mineraux = [
        Mineral(nom="Quartz", formule_chimique="SiO2", couleur=CouleurRGB(r=220, g=220, b=220), eclat="Vitreux", radioactivite=False, durete=7, masse_volumique=2.65),
        Mineral("Feldspath", "KAlSi3O8", CouleurRGB(255, 255, 255), "Nacré à vitreux", False, 6, 2.56),
        Mineral("Gypse", "CaSO4·2H2O", CouleurRGB(255, 255, 200), "Soyeux", False, 2, 2.32),
        Mineral("Calcite", "CaCO3", CouleurRGB(255, 255, 150), "Vitreux", False, 3, 2.71),
        Mineral("Halite", "NaCl", CouleurRGB(255, 255, 0), "Vitreux", False, 2.5, 2.16),
        Mineral("Magnétite", "Fe3O4", CouleurRGB(0, 0, 0), "Métallique", False, 5.5, 5.18),
        Mineral("Pyrite", "FeS2", CouleurRGB(255, 200, 50), "Métallique", False, 6, 5.02),
        Mineral("Fluorite", "CaF2", CouleurRGB(140, 255, 170), "Vitreux", False, 4, 3.18),
        Mineral("Hématite", "Fe2O3", CouleurRGB(150, 0, 0), "Métallique", False, 5.5, 5.26),
        Mineral("Biotite", "K(Fe, Mg)3AlSi3O10(OH, F)2", CouleurRGB(0, 0, 0), "Vitreux", False, 2.5, 3.04),
        Mineral("Talc", "Mg3Si4O10(OH)2", CouleurRGB(200, 200, 255), "Cireux", False, 1, 2.75),
        Mineral("Orthoclase", "KAlSi3O8", CouleurRGB(255, 200, 100), "Vitreux", False, 6, 2.56),
        Mineral("Sphalérite", "ZnS", CouleurRGB(0, 0, 0), "Adamantine", False, 3.5, 4.02),
        Mineral("Muscovite", "KAl2(AlSi3O10)(F, OH)2", CouleurRGB(255, 255, 200), "Vitreux", False, 2.5, 2.88),
        Mineral("Grenat", "X3Y2(SiO4)3", CouleurRGB(200, 0, 0), "Vitreux", False, 7, 4.32),
        Mineral("Cassitérite", "SnO2", CouleurRGB(0, 0, 0), "Adamantine", False, 6.5, 7.05),
        Mineral("Barytine", "BaSO4", CouleurRGB(255, 255, 200), "Vitreux", False, 3, 4.48),
        Mineral("Azurite", "Cu3(CO3)2(OH)2", CouleurRGB(0, 0, 255), "Vitreux", False, 4, 3.77),
        Mineral("Malachite", "Cu2CO3(OH)2", CouleurRGB(0, 150, 0), "Vitreux", False, 4, 4.03),
        Mineral("Apatite", "Ca5(PO4, CO3)6(F, Cl, OH)2", CouleurRGB(255, 200, 150), "Vitreux", False, 5, 3.18),
        Mineral("Uraninite", "UO2", CouleurRGB(0, 0, 0), "Métallique", True, 6, 0.63),
        Mineral("Torbernite", "Cu(UO2)2(PO4)2·8H2O", CouleurRGB(0, 255, 0), "Radiant", True, 2, 3.18),
        Mineral("Pechblende", "U3O8", CouleurRGB(0, 0, 0), "Sub-métallique à huileux", True, 6, 0.63),
        Mineral("Thorite", "ThSiO4", CouleurRGB(255, 0, 0), "Transparent à translucide", True, 4, 4.44),
        Mineral("Carnotite", "K2(UO2)2(VO4)2·3H2O", CouleurRGB(255, 200, 0), "Terreux", True, 2.5, 4.9)
    ]
    collection = Collection("Ma collection", "Reb")
    for m in mineraux:
        collection.ajouter_mineral(m)
    return collection


def choix_mineral(collection, description = ''):
    print("Voici la collection : ")
    mineraux = collection.get_mineraux()
    choix_valide = False
    while not choix_valide:
        i = 0
        for m in mineraux:
            print(f"{i}: {m.nom}")
            i += 1
        print(f"Entrez le numéro du minéral {description}")
        try :
            choix = int(input()) 
            choix_valide = choix >= 0 and choix < len(mineraux)
        except: 
            print("Invalide")
    return mineraux[choix]
    

def afficher_collection(collection):
    print("Voici la collection : ")
    print(collection.description())
    print("Son meilleur minéral est : ")
    print(collection.gagnant().description())


def lire_float_positif():
    valide = False
    while not valide:
        try :
            choix = float(input()) 
            valide = choix > 0
        except: 
            print("Invalide")
    return choix

def combat_entre_deux_mineraux(collection):
    m1 =  choix_mineral(collection, "Premier minéral")
    m2 =  choix_mineral(collection, "Deuxième minéral")
    print(Mineral.combat(m1, m2).description())

if __name__ == "__main__":
    collection = batir_collection()

    print("Description d'un minéral :")
    print(choix_mineral(collection).description())

    print("Combat entre deux minéraux :")
    combat_entre_deux_mineraux(collection)

    print(f"Il y a eu {Mineral.nb_combats} combats")

    courriel = "\\b([a-z]|[0-9])+@[a-z]([a-z]|[0-9])*\\.[a-z]([a-z]|[0-9])*\\b"
    print(re.search(courriel, "0h0@df.f"))


    # Minerai(dictionnaire de poids et minéraux)
    # fondre recoit une température et retourne un minerai, retire les minéraux fondus
    # Un mineral peut fondre (vrai ou faux, plus print A FONDU) 
    # Un minerai est une roche suffisamment riche en mineraux pour être exploitable
    # (a au moins 10% de masse précieuse)
    # Dessinez la table dynamique