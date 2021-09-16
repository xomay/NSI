import math

class Angle:
    """
    Une classe pour représenter un angle en degrée
    """

    def __init__(self, angle = 0) -> None:
        if angle<=360:
            self.__angle = angle
        elif angle>360:
            self.__angle = angle % 360

    def affiche(self) -> str:
        return "{} degré(s)".format(self.__angle)

    def ajoute(self, angle: int) -> None:
        if self.__angle + angle > 360:
            self.__angle = (self.__angle + angle) % 360
        else:
            self.__angle = self.__angle + angle

    def cosinus(self) -> str:
        return "Le cosinus est égal à {}".format(math.cos(self.__angle * (math.pi)/180))

    def sinus(self) -> str:
        return "Le sinus est égal à {}".format(math.sin(self.__angle * (math.pi)/180))