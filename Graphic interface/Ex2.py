from tkinter import *
from math import *

# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
def evaluer(event):
    chaine.configure(text = "Résultat = " + str(eval(entree.get())))
# ----- Programme principal : ----
fenetre = Tk()
entree = Entry(fenetre,width=20)
entree.pack()
entree.bind("<Return>", evaluer)
chaine = Label(fenetre, text = "Resultat =" + str(eval))
chaine.pack()

fenetre.mainloop()