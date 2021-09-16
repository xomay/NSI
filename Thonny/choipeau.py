import csv
def recup_donnees(f: str) -> list:
   """
   Fonction qui récupère les données d'un fichier csv dans une liste
   composé de dictionnaires
   :param f: nom du fichier csv
   :return: liste des données
   """
   tab = []
   with open(f, 'r') as fich:
       f = csv.DictReader(fich)

       for ligne in f:
           tab.append(dict(ligne))

   return tab


def fonction_mystere(eleves: list) -> dict:
    """
    fonction qui prend une liste d'élèves et renvoie la liste du nombre d'élèves de chaque maison
    :param eleves: liste de tous les élèves 
    :return: liste des maisons avec le nombre d'élèves par maison
    """
    nombre_eleves = {}
    for nom_maison in eleves:
        maison = nom_maison['Maison']
        if maison in nombre_eleves.keys():
            nombre_eleves[maison] += 1
        else:
            nombre_eleves[maison] = 1
    return nombre_eleves

print(recup_donnees("choixpeauMagique.csv"))
print(fonction_mystere(recup_donnees("choixpeauMagique.csv")))