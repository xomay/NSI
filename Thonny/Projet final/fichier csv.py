# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt

def recup_donnees(f: str) -> list:
   """
   Fonction qui récupère les données d'un fichier csv dans une liste
   composé de dictionnaires
   :param f: nom du fichier csv
   :return: liste des données
   """
   tab = []
   global entete
   with open(f, 'r') as fich:
       f = csv.reader(fich)


       for ligne in f:
           tab.append(ligne)

       entete=tab[0]

       donnee=[]
       for i in range(0, len(tab)):
           donnee.append(tab[i])

   return donnee

def temperature(data: list):
    global degree

    for i in range(1,len(data)):
        degree.append(int(data[i][0]))

def temps(data: list):
    global time

    for i in range(1, len(data)):
        time.append(int(data[i][1]))


def graph(temperature: list, temps: list, entete: list):
    plt.clf()
    plt.plot(temps, temperature, 'r,-', linewidth=1, label='température')
   # plt.plot(temps, humidite, 'b,-', linewidth=1, label='humidité')
    plt.xlabel(entete[1])
    plt.ylabel(entete[0])
    plt.title('Température')
    plt.grid()
    plt.show()

entete=[]
degree = []
hum = []
time = []
print(recup_donnees("Data.csv"))
temperature(recup_donnees("Data.csv"))
temps(recup_donnees("Data.csv"))
print(entete)
print(degree)
#print(hum)
print(time)
graph(degree, time, entete)

