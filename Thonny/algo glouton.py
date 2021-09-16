table_1 = [
    {'nom' : 'objet A', 'poids' : 15, 'valeur' : 500},
    {'nom' : 'objet B', 'poids' : 24, 'valeur' : 400},
    {'nom' : 'objet C', 'poids' : 9,  'valeur' : 350},
    {'nom' : 'objet D', 'poids' : 25, 'valeur' : 750},
    {'nom' : 'objet E', 'poids' : 5,  'valeur' : 400},
    {'nom' : 'objet F', 'poids' : 12, 'valeur' : 800},
    {'nom' : 'objet G', 'poids' : 2,  'valeur' : 1400},
    {'nom' : 'objet H', 'poids' : 18, 'valeur' : 550}
]


table_2 = [
    {'nom' : 'video A', 'poids' : 4.5,   'valeur' : 114},
    {'nom' : 'video B', 'poids' : 0.63,  'valeur' : 85},
    {'nom' : 'video C', 'poids' : 3.35,  'valeur' : 40},
    {'nom' : 'video D', 'poids' : 0.085, 'valeur' : 4},
    {'nom' : 'video E', 'poids' : 2.15,  'valeur' : 18},
    {'nom' : 'video F', 'poids' : 2.71,  'valeur' : 80},
    {'nom' : 'video G', 'poids' : 0.32,  'valeur' : 5},
    {'nom' : 'video H', 'poids' : 3.7,   'valeur' : 86},
    {'nom' : 'video I', 'poids' : 2.4,   'valeur' : 64},
    {'nom' : 'video J', 'poids' : 6.4,   'valeur' : 12}
]    

def tri(tab: list) -> list:
    tab_trie=sorted(tab, key=lambda x: x['valeur'] / x['poids'], reverse=True)
    return tab_trie

def selection(trier: list, limite: int) -> list:
    poids=0
    valeur=0
    poids_max=limite
    selec=[]
    for i in range(len(trier)):
        if trier[i]['poids'] < poids_max-poids:
            poids+=trier[i]['poids']
            valeur+=trier[i]['valeur']
            selec.append(trier[i])
    return selec, poids, valeur

selec1,poids1,valeur1=selection(tri(table_1),40)
selec2,poids2,valeur2=selection(tri(table_2),8)
print("Poids pour le voleur = {}, valeur = {}".format(poids1,valeur1))
print(selec1)
print("Poids pour le voleur = {}, valeur = {}".format(poids2,valeur2))
print(selec2)
            