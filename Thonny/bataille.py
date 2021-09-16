import JeuDeCartes

player1 = JeuDeCartes.JeuDeCartes(52)
player1.melangerPaquet()
player1 = player1.affiche()
p1Point = 0

player2 = JeuDeCartes.JeuDeCartes(52)
player2.melangerPaquet()
player2 = player2.affiche()
p2Point = 0

for i in range(52):
    if player1[i][0] < player2[i][0]:
        p2Point += 1
        print("Player 2 win {} : {}".format(player1[i][0], player2[i][0]))
    if player1[i][0] > player2[i][0]:
        p1Point += 1
        print("Player 1 win {} : {}".format(player1[i][0], player2[i][0]))
    if player1[i][0] == player2[i][0]:
        print("Egalité {} : {}".format(player1[i][0], player2[i][0]))

if p1Point > p2Point:
    print("Player 1 win !")
elif player2 > player1:
    print("Player 2 win !")
else:
    print("Egalité !!!")