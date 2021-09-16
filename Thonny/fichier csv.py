import csv
with open('', "r") as fichier:
    table = csv.DictReader(fichier)
    tab=[]
    
    for ligne in table:
        tab.append(dict(ligne))
        
    print(tab[len(tab)-1])