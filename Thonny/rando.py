import csv
import matplotlib.pyplot as plt

def lecture_fichier(donne: str) -> list:
    """
    fonction qui récupère un fichier et qui renvoie une liste avec les entetes et une liste avec les données
    :param donne: fichier de données
    :return: liste d'entetes et liste de données
    """
    with open(donne, "r") as fichier:
        table=csv.reader(fichier)
        tab=[]
        
        for ligne in table:
            tab.append(ligne)
            
        liste_entetes=[]
        for i in range(2):
            liste_entetes.append(tab[0][i])
        parcours=[]
        for i in range(1,len(tab)):
            parcours.append((tab[i]))
            
        return liste_entetes, parcours
    
def separation_donnees(parcours: list) -> list:
    altitudes=[]
    distances=[]
    for i in range(len(parcours)):
        altitudes.append(int(parcours[i][0]))
        distances.append(float(parcours[i][1]))
        
    return altitudes, distances
        
def denivele(altitudes: list) -> float:
    deniv_positif=0
    deniv_negatif=0
    for i in range(0,len(altitudes)-1):
        if altitudes[i+1]-altitudes[i]>0:
            deniv_positif += altitudes[i+1]-altitudes[i]
        elif altitudes[i+1]-altitudes[i]<0:
            deniv_negatif += altitudes[i+1]-altitudes[i]
            
    return deniv_positif, deniv_negatif
            
def cumul_distance(distances: list) -> list:
    metre=0
    distance_parcourue=[]
    for i in range(len(distances)):
        metre+=distances[i]
        distance_parcourue.append(round(metre,2))
    return distance_parcourue, metre

def visualisation_denivele(altitudes: list, distance_parcourue: float, entetes: list):
    plt.clf()
    plt.plot(distance_parcourue, altitudes, 'k,-', linewidth=1, label='y = f(x)')
    plt.xlabel(entetes[1])
    plt.ylabel(entetes[0])
    plt.title('Altitude et topographie')
    plt.grid()
    plt.show()

fich1, fich2 = lecture_fichier("rando.csv")
altitudes, distances=separation_donnees(fich2)
deniv_positif, deniv_negatif=denivele(altitudes)
distance_parcourue, metre=cumul_distance(distances)
print(distance_parcourue, metre)
print("le dénivelé positif est de : ",deniv_positif,", et le négatif de : ",deniv_negatif)
print("la distance totale de la rando est {:.2f} mètres".format(metre))
visualisation_denivele(altitudes, distance_parcourue, fich1)
