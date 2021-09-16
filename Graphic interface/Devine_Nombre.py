from tkinter import *
import random

nmb=random.randint(0,30)
mini=0
maxi=30


def verif(rep):
    while not(rep.isdigit()):
        rep = input("Veillez à ne saisir que des chiffres ")
    return int(rep)

def afficher(event):
    global nmb
    reponse=verif(entree.get())
    if reponse==nmb:
        chaine.configure(text="Le résultat était = " + str(verif(entree.get())))
    else:
        if reponse < nmb:
            borne_min.configure(text="Compris entre : " + str(reponse))
        if reponse > nmb:
            borne_max.configure(text="Et : " + str(reponse))


fenetre = Tk()
entree = Entry(fenetre,width=20)
entree.pack()
entree.bind("<Return>", afficher)
chaine = Label(fenetre, text = "Resultat = " )
chaine.pack()
find=Label(fenetre, text= "Trouver "+ str(nmb))
find.pack()
borne_min=Label(fenetre, text= "Compris entre : "+ str(mini))
borne_min.pack(side=LEFT)
borne_max=Label(fenetre, text= "et : "+ str(maxi))
borne_max.pack(side=RIGHT)



fenetre.mainloop()