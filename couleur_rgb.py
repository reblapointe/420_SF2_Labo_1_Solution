class CouleurRGB:
    '''Décrit une couleur selon sa valeur rouge-vert-bleu'''

    def __init__(self, r:int, g:int, b:int):
        self.__r = r
        self.__g = g
        self.__b = b
        if self.__r > 255 or self.__g > 255 or self.__b > 255 or self.__r < 0 or self.__g < 0 or self.__b < 0:
            raise ValueError(f"La couleur doit se situer entre 0 et 255")
        
    def description(self) -> str:
        return (f"({self.__r}, {self.__g}, {self.__b})")
    
