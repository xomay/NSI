class Domino:
    """Un domino d'un jeu de 28 caractérisé par :
    - sa valeur
    """
    def __init__(self, val1 = 0, val2 = 0):
        """constructeur de la classe Carte"""
        self.__valeur1 = val1
        self.__valeur2 = val2

    def getValeur(self):
        """renvoie la valeur et la couleur d'une carte"""
        return (self.__valeur1, self.__valeur2)

    def double(self):
        """renvoie true si la domino est double ou false si il ne l'est pas"""
        if self.__valeur1 == self.__valeur2:
          return True
        else:
          return False
    
    def blanc(self):
        """renvoie true si le domino est blanc ou false s'il ne l'est pas"""
        if self.__valeur1 == 0:
          return True
        if self.__valeur2 == 0:
          return True
        else:
          return False

    def points(self) -> str:
        """renvoie le nombre de points d'un domino"""
        val = self.__valeur1 + self.__valeur2
        return "le domino a {} points".format(val)
    
    def affiche(self) -> None:
        if self.__valeur1 == self.__valeur2:
          print("╔═══╗")
          print("║ {} ║".format(self.__valeur1))
          print("╠═══╣")
          print("║ {} ║".format(self.__valeur2))
          print("╚═══╝")
          
        else:
          print("╔═══╦═══╗")
          print(f"║ {self.__valeur1} ║ {self.__valeur2} ║")
          print("╚═══╩═══╝")