class CompteBancaire:
    """
    Une classe pour gérer un compte bancaire
    """

    def __init__(self, nom = "Dupont", solde = 1000):
        self.__nom = nom
        self.__solde = solde
        print("Création d'un compte bancaire au nom de {}, et avec un solde de {}"
              .format(self.__nom, self.__solde))

    def getNom(self) -> str:
        return "Le propriétaire est {}".format(self.__nom)

    def getSolde(self) -> str:
        return "Le solde est de {} euro(s)".format(self.__solde)

    def setNom(self, nom:str) -> None:
        self.__nom = nom

    def setSolde(self, solde:int) -> None:
        self.__solde = solde

    def depot(self, somme:int) -> None:
        self.__solde += somme

    def retrait(self, somme: int) -> None:
        self.__solde -= somme


    def affiche(self) -> str:
        return "Le compte est au nom de {}, et possède un solde de {} euros".format(self.__nom, self.__solde)