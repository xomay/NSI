import cartes
import random

class JeuDeCartes:
    """classe définissant un jeu de cartes caractérisé par :
    - son nombre de cartes
    - son paquet de cartes"""

    def __creerPaquet(self):
        """méthode privée pour créer le jeu de cartes classé
        par valeur et couleur, donc non classé"""
        monPaquet = []
        if self.__nbCartes == 32:
            numDebut = 7
        else:
            numDebut = 2
        for coul in ["Trèfle", "Carreau", "Coeur", "Pique"]:
            for i in range(numDebut, 15):
                newCarte = cartes.Carte(i, coul)
                monPaquet.append(newCarte)

        return monPaquet

    def __init__(self, nb):
        """constructeur de la classe jeuDeCartes"""
        self.__nbCartes = nb
        self.__paquet = self.__creerPaquet()

    def getNbCartes(self):
        """renvoie le nombre de cartes dans le jeu"""
        return self.__nbCartes

    def getPaquet(self):
        """renvoie le paquet de cartes"""
        return self.__paquet

    def melangerPaquet(self):
        """mélange aléatoirement le paquet de cartes"""
        random.shuffle(self.__paquet)

    def affiche(self):
        liste = []
        for carte in self.__paquet:
            liste.append(carte.getAttributs())
        return liste

monJeu = JeuDeCartes(32)
monPaquet = monJeu.getPaquet()
for i in range(len(monPaquet)):
    print(monPaquet[i].getValeur(),monPaquet[i].getCouleur(),
    monPaquet[i].getFigure())

monJeu.melangerPaquet()
for i in range(len(monPaquet)):
    print(monPaquet[i].getValeur(),monPaquet[i].getCouleur(),
    monPaquet[i].getFigure())