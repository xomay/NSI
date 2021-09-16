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