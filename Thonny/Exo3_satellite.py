class Satellite:
    """
    Une classe qui permet qui permette d’instancier
    des objets simulant des satellites artificiels
    lancés dans l’espace, autour de la terre.
    """

    def __init__(self, nom: str, masse = 100, vitesse = 0):
        self.__nom = nom
        self.__masse = masse
        self.__vitesse = vitesse
        print("Création d'un satellite au nom de {} ayant une masse de {}kg et une vitesse de {}km/h"
              .format(self.__nom, self.__masse, self.__vitesse))

    def afficheVitesse(self) -> str:
        return "Le satellite se nomme {}, a une masse de {}kg et une vitesse de {}km/h".format(self.__nom, self.__masse, self.__vitesse)

    def impulsion(self, force, duree) -> None:
        variation = (force * duree / self.__masse)
        self.__vitesse += variation

    def energie(self) -> str:
        nrj = (self.__masse * self.__vitesse * self.__vitesse) / 2
        return "La valeur de l'énergie cinetique est de {}".format(nrj)
