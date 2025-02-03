class CouleurRGB:
    '''Décrit une couleur selon sa valeur rouge-vert-bleu'''

    def __init__(self, r:int, g:int, b:int):
        self._r = r
        self._g = g
        self._b = b
        if self._r > 255 or self._g > 255 or self._b > 255 or self._r < 0 or self._g < 0 or self._b < 0:
            raise ValueError(f"La couleur doit se situer entre 0 et 255")
        
    def description(self):
        return (f"({self._r}, {self._g}, {self._b})")
    
