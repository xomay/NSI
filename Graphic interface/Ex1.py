from tkinter import *
compteur=0

def plus(event):
    global compteur
    compteur +=1
    score.configure(text="Nombre de clics :"+ str(compteur))

def moins(event):
    global compteur
    compteur -=1
    score.configure(text="Nombre de clics :"+ str(compteur))

fen1 = Tk()
# On dimensionne la fenetre
fen1.geometry("600x200")
# On lui donne un titre
fen1.title("tk")
titre_haut= Label(fen1, text="Pour augmenter ou diminuer le compteur:Clic droit et gauche, les touches a et z, les flèches haut et bas")
titre_haut.pack()
score=Label(fen1, text="Nombre de clics :"+ str(compteur))
score.pack(side = LEFT)
bouton_clic=Button(fen1, text="clic")
bouton_clic.pack()
bouton_clic.bind("<Button-1>",plus)
bouton_clic.bind("<Button-3>",moins)

fen1.bind("<Up>",plus)
fen1.bind("<Down>",moins)
fen1.bind("<KeyPress-a>",plus)
fen1.bind("<KeyPress-z>",moins)

bt_quit=Button(fen1, text="Quitter", command=fen1.destroy)
bt_quit.pack(side = RIGHT)
fen1.mainloop()