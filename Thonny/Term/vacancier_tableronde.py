from random import randint

players = [0*i for i in range(1,13)]
PlusDe2 = []

play = 0
players[11] = 13
while play > 0:
    for i in range(len(players)):
        if players[i] >=2:
            PlusDe2.append(i)
    select = randint(0, len(PlusDe2)) #prend l'indice ds le tab plusde2 du joueur devant donner 
    give = PlusDe2[select] #prend l'indice du jouer dans le tab players qui doit donner
    if give + 1 > 11:
        players[give-1] += 1
        players[0] += 1
    else:
        players[give+1] += 1
        players[give-1] += 1
    print(players)    
