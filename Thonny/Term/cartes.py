class Carte:
    """Une carte d'un jeu de 32 ou 52 cartes caractérisée par :
    - sa valeur
    - sa couleur
    - sa figure"""
    def __init__(self, val, coul):
        """constructeur de la classe Carte"""
        self.__valeur = val
        self.__couleur = coul
        if val == 11:
            self.__figure = "Valet"
        else:
            if val == 12:
                self.__figure = "Dame"
            else:
                if val == 13:
                    self.__figure ="Roi"
                else:
                    self.__figure = "Aucune"

    def getAttributs(self):
        """renvoie la valeur et la couleur d'une carte"""
        return (self.__valeur, self.__couleur)

    def getValeur(self):
        """renvoie la valeur d'une carte"""
        return self.__valeur

    def getCouleur(self):
        """renvoie la couleur d'une carte"""
        return self.__couleur

    def getFigure(self):
        """renvoie la figure d'une carte"""
        return self.__figure

    def setValeur(self, val):
        """renvoie Vrai si la valeur de la carte a été modifié par val
        et Faux sinon (valeur non comprise dans l'intervalle [2:14])"""
        if 2 <= val <= 14:
            self.__valeur = val
            self.__setFigure(val)
            return True
        else:
            return False

    def setCouleur(self, coul):
        """renvoie Vrai si la couleur de la carte a été modifié par coul
        et Faux sinon (valeur non comprise dans le domaine des couleurs)"""
        lstCouleurs = ["Trèfle", "Carreau", "Coeur", "Pique"]
        if coul in lstCouleurs:
            self.__couleur = coul
            return True
        else:
            return False

    def __setFigure(self, val):
        """méthode privée pour changer la figure en fonction de la
        nouvelle valeur val"""
        if val == 11:
            self.__figure = "Valet"
        else:
            if val == 12:
                self.__figure = "Dame"
            else:
                if val == 13:
                    self.__figure = "Roi"
                else:
                    self.__figure = "Aucune"