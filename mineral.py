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
    
    def __init__(self, nom:str, formule_chimique:str, couleur:CouleurRGB, eclat:str, radioactivite:bool, durete:int, masse_volumique:float):
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


    def get_nom(self) -> str:
        '''Getter sur le nom'''
        return self.__nom
    
    def get_radioactivite(self) -> bool:
        '''Getter sur la radioactivite'''
        return self.__radioactivite
    
    def description_durete(self) -> str:
        '''Fabrique une description textuelle de la dureté du minéral'''
        if self.__durete < 2:
            return "très mou"
        if self.__durete < 5:
            return "mou"
        if self.__durete < 7:
            return "moyen"
        if self.__durete < 10:
            return "dur"
        return "très dur"

    def description(self) -> str:
        '''Fabrique une description textuelle du minéral'''
        radioactivite = ", RADIOACTIF" if self.__radioactivite else ""
        return (f"{self.__nom}  [{self.__symbole}] " +
                f"Couleur : {self.__couleur.description()}, " +
                f"Éclat : {self.__eclat}, " +
                f"Dureté : {self.__durete} ({self.description_durete()}), " +
                f"Éclat : {self.__eclat}, " +
                f"Masse Volumique : {self.__masse_volumique} g/cm³"+
                radioactivite)
    
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
        elif not a.__radioactivite and b.__radioactivite:
            return b
        elif a.__masse_volumique > b.__masse_volumique:
            return a
        elif a.__masse_volumique < b.__masse_volumique:
            return b
        else:
            return a if a.__durete >= b.__durete else b
    
    
    def masse_vers_volume(self, masse:float)-> float:
        '''calcule le volume du minéral pour une masse'''
        return masse / self.__masse_volumique 
    
    def volume_vers_masse(self, volume:float) -> float:
        '''calcule la masse du minéral pour un volume'''
        return self.__masse_volumique * volume