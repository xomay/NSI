class Chrono:

    """Une classe pour représenter un temps en
    heure(s), minutes(s), secondes(s)
    """

    def __init__(self, h:int, m:int, s:int) -> None:
        self.__heures = h
        self.__minutes = m
        self.__secondes = s
        print("création d'un nouvel horaire {}:{}:{}"
              .format(self.__heures, self.__minutes, self.__secondes))

    def getHeure(self) -> int:
        return self.__heures

    def setHeure(self, h:int) -> None:
        self.__heures = h

    def affiche(self) -> str:
        """Affiche le chrono sous la forme hh:mm:ss

        Returns :
            str: renvoie une chaine de caractères
        """
        return "le chrono indique {}:{}:{}".format(self.__heures, self.__minutes, self.__secondes)

    def __str__(self) -> str :
        return "le chrono indique {}:{}:{}".format(self.__heures, self.__minutes, self.__secondes)

    def avance(self, val:int) -> None:
        """Méthode pour ajouter du temps au chrono
        Args:
            val (int): ajout en secondes
        """
        self.__secondes += val
        self.__minutes += self.__secondes // 60
        self.__secondes = self.__secondes % 60
        self.__heures += self.__minutes // 60
        self.__minutes = self.__minutes % 60