from mineral import Mineral

class Collection:
    '''
    Encapsule une collection de minéraux. Une collection de minéraux a un nom, un propriétaire et une liste de minéraux.
    Il est possible d'ajouter un minéral à la collection ainsi que d'obtenir le meilleur minéral de la collection.
    '''
    def __init__(self, nom:str, proprietaire:str):
        self._nom = nom
        self._proprietaire = proprietaire
        self._mineraux = []

    def get_mineraux(self):
        return self._mineraux.copy()
    
    def ajouter_mineral(self, mineral):
        '''Ajoute un mineral à la collection'''
        self._mineraux.append(mineral)

    def description(self):
        '''Génère une description textuelle de la collection'''
        est_radioactif = False
        d = f"{self._nom}  [{self._proprietaire}] : "
        for m in self._mineraux:
            if m.radioactivite:
                est_radioactif = True
            d += f"   {m.description()},\n" 
        if est_radioactif :
            d += "Attention, cette collection contient un ou des minéraux radioactif(s)"
        return d
    
    def gagnant(self):
        '''Détermine le meilleur minéral parmi la collection'''
        if len(self._mineraux) == 0:
            return None
        gagnant = self._mineraux[0]
        for adversaire in self._mineraux[1:]:
            #print(f"{gagnant.nom} vs {adversaire.nom} : {gagnant.nom}")
            gagnant = Mineral.combat(gagnant, adversaire)
        return gagnant