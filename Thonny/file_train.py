from random import randint
# fich=open("scores.txt","r")
# nom=fich.readline()
# nom=nom.rstrip()
# date=fich.readline()
# date=date.rstrip()
# score=fich.read()
# score=score.rstrip()
# print("Bonjour ",nom,",le ",date,", vous avez trouvé le bon nombre en ",score,"essais")
# fich.close()

# with open("mots.txt","r") as fich:
#     elements=fich.readlines()
#     nmb=len(elements)
#     print(nmb)
    
# with open("mots.txt","r") as fich:
#     compteur=0
#     for ligne in fich:
#         mot=ligne
#         mot=mot.rstrip()
#         if len(mot)==7:
#             compteur+=1
#     print(compteur)
    
with open("mots.txt","r") as fich:
    elements=fich.readlines()
    nmb=len(elements)
    print(elements[randint(0,nmb-1)])