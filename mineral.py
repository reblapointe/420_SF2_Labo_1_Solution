from couleur_rgb import CouleurRGB

class Mineral:
    '''
    Encapsule les attributs d'un minéral. 
    Un minéral a un nom, une formule chimique, une couleur, un éclat, une radioactivité, une dureté et une masse volumique.
    Deux minéraux peuvent combattre ensemble
    '''
    nb_combats = 0

    MIN_DURETE = 1
    MAX_DURETE = 10
    
    def __init__(self, nom:str, formule_chimique:str, couleur:str, eclat:str, radioactivite:bool, durete:int, masse_volumique:float):
        self.__nom = nom

        if len(formule_chimique) > 0:
            self.__symbole = formule_chimique
        else:
            raise ValueError(f"La formule chimique d'un minéral ne peut pas être vide")
        
        self.__couleur = couleur
        self.__eclat = eclat
        self.__radioactivite = radioactivite

        if masse_volumique > 0:
            self.__masse_volumique = masse_volumique
        else:
            raise ValueError(f"La masse volumique doit être strictement positive")
        
        if Mineral.MIN_DURETE <= durete <= Mineral.MAX_DURETE:
            self.__durete = durete
        else:
            raise ValueError(f"La dureté doit se situer entre {Mineral.MIN_DURETE} et {Mineral.MAX_DURETE}")


    @property
    def nom(self):
        return self.__nom

    @property
    def symbole(self):
        return self.__symbole

    @property
    def couleur(self):
        return self.__couleur

    @property
    def eclat(self):
        return self.__eclat

    @property
    def radioactivite(self):
        return self.__radioactivite

    @property
    def durete(self):
        return self.__durete

    @property
    def masse_volumique(self):
        return self.__masse_volumique

    def description(self):
        '''Fabrique une description textuelle du minéral'''
        return (f"{self.nom}  [{self.symbole}] " +
                f"Couleur : {self.couleur.description()}, " +
                f"Éclat : {self.eclat}, " +
                f"Dureté : {self.durete}, " +
                f"Éclat : {self.eclat}, " +
                f"Masse Volumique : {self.masse_volumique} g/cm³")
    
    def combat(a, b):
        '''
        Combat entre deux minéraux. 
        Un métal radioactif gagne contre un métal non radioactif, 
        sinon, le plus dur l'emporte, 
        sinon, le plus dense l'emporte, 
        sinon, le premier l'emporte.
        '''
        Mineral.nb_combats += 1
        if a.__radioactivite and not b.__radioactivite:
            return a
        elif not a.radioactivite and b.__radioactivite:
            return b
        elif a.masse_volumique > b.masse_volumique:
            return a
        elif a.masse_volumique < b.masse_volumique:
            return b
        else:
            return a if a.durete >= b.durete else b
    
    
    def masse_vers_volume(self, masse):
        '''calcule le volume du minéral pour une masse'''
        return masse / self.masse_volumique 
    
    def volume_vers_masse(self, volume):
        '''calcule la masse du minéral pour un volume'''
        return self.masse_volumique * volume