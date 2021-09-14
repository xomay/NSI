import random
import domino


class JeuDeDomino:
    """classe définissant un jeu de domino caractérisé par :
    - son premier côté 
    - son deuxième côté"""

    def __createDomino(self):
        """méthode privée pour créer le jeu de domino
        par valeur, donc non classé"""
        monPaquet = []
        for a in range(7):
          for i in range(a, 7):
            val1 = a
            val2 = i
            newDomino = domino.Domino(val1, val2)
            monPaquet.append(newDomino)

        return monPaquet

    def __init__(self, nb):
        """constructeur de la classe jeuDeDomino"""
        self.__nbDomino = nb
        self.__paquet = self.__createDomino()

    def getNbDomino(self):
        """renvoie le nombre de domino dans le jeu"""
        return self.__nbDomino

    def getPaquet(self, nbPlayer):
        """renvoie le paquet de domino"""
        self.melangerJeu()
        if nbPlayer == 2:
          player1 = self.__paquet[:7]
          player2 = self.__paquet[8:14]
          pioche = self.__paquet[15:28]
          self.__paquet = [player1, player2, pioche]
        elif nbPlayer == 3:
          player1 = self.__paquet[:6]
          player2 = self.__paquet[7:13]
          player3 = self.__paquet[14:20]
          pioche = self.__paquet[21:]
          self.__paquet = [player1, player2, player3, pioche]
        elif nbPlayer > 3:
          print("Vous ne pouvez pas jouer à plus de 3 :/ ")

        return self.__paquet

    def melangerJeu(self):
        """mélange aléatoirement le paquet de cartes"""
        return random.shuffle(self.__paquet)


def showDominos(currentPlayer):
  if len(paquetPlayers[currentPlayer]) > 0:
    print("\nVoici maintenant votre jeu :\n")
    for a in paquetPlayers[currentPlayer]:
      a.affiche()


def getAvailableDominos(player, lastDomino):
  availableDominos = []
  paquet = paquetPlayers[player]
  valueLastDomino = lastDomino.getValeur()
  for i in paquet:
    values = i.getValeur()
    if values[0] == valueLastDomino[0] or values[1] == valueLastDomino[1]:
      availableDominos.append(i)

  return availableDominos


def playDomino(currentPlayer, availableDominos, playedDominos):
  if len(availableDominos) == 1:
    print("Vous avez joué.")
    playedDominos.append(availableDominos[0])
    paquetPlayers[currentPlayer].remove(availableDominos[0])

  elif len(availableDominos) > 1:
    choice = int(input("\nQuelle choix voulez vous prendre : "))
    availableDominos[choice-1].affiche()
    playedDominos.append(availableDominos[choice-1])
    paquetPlayers[currentPlayer].remove(availableDominos[choice-1])

  showDominos(currentPlayer)


def piocher(currentPlayer):
  print("\nVous ne pouvez pas jouer, vous devez donc piocher.")
  paquetPlayers[currentPlayer].append(pioche[0])
  pioche[0].affiche()
  pioche.pop(0)
  print("Vous avez pioché ce domino\n")
  showDominos(currentPlayer)

  print(f"Il n'y a plus que {len(pioche)} dominos dans la pioche")


def newRound(currentPlayer, domino, pioche, playedDominos):
  availableDominos = getAvailableDominos(currentPlayer, domino)
  if len(availableDominos) > 0:
    print("\nVoici les dominos que vous pouvez jouer :")
    dominos = 0
    for a in availableDominos:
      dominos += 1
      print(f"Choix n°{dominos}")
      a.affiche()
    action = input("\nVoulez vous piocher ou jouer ? ")
    if action == "piocher":
      piocher(currentPlayer)

    if action == "jouer":
      playDomino(currentPlayer, availableDominos, playedDominos)
  else:
    piocher(currentPlayer)


monJeu = JeuDeDomino(28)
players = int(input("A combien de joueur voulez vous jouer (2-3) ? "))
if players == 2:
  Paquet = monJeu.getPaquet(players)
  player1 = Paquet[0]
  player2 = Paquet[1]
  pioche = Paquet[2]
  paquetPlayers = [player1, player2]
elif players == 3:
  Paquet = monJeu.getPaquet(players)
  player1 = Paquet[0]
  player2 = Paquet[1]
  player3 = Paquet[2]
  pioche = Paquet[3]
  paquetPlayers = [player1, player2, player3]

for i in range(players):
  print("==============")
  print(f"Dominos du joueur {i+1}")
  print("==============")

  for a in paquetPlayers[i]:
    a.affiche()

print("==============")
print(f"pioche")
print("==============")

for a in pioche:
  a.affiche()

waitForConfirm = input("continue (Y/n) : ")

if waitForConfirm == "y" or waitForConfirm == "Y":
  def getRandomDomino(paquet):
    randomDomino = paquet
    return randomDomino

  played = []
  firstDomino = getRandomDomino(pioche)
  firstDomino = firstDomino[0]
  pioche.pop(0)
  played.append(firstDomino)
  currentPlayer = 0
  rounds = 1

  print("\nVoici le plateau de jeu pour l'instant il n'y a qu'un domino, a vous de le completer !\n")
  print(f"\n Tour du joueur n°{currentPlayer+1}")
  print("════════════════════════════════════════════════")
  for a in played:
    a.affiche()
  print("════════════════════════════════════════════════")
  newRound(currentPlayer, firstDomino, pioche, played)
  rounds += 1

  if players == 3:
    while len(paquetPlayers[currentPlayer]) > 0 or len(pioche) > 0:
      if currentPlayer == 2:
        currentPlayer = 0
      else:
        currentPlayer += 1

      lastDomino = played[-1]
      input("Voulez vous passer au prochain tour : ")
      print(f"\n Tour du joueur n°{currentPlayer+1} / Tour n°{rounds}")
      print("\n════════════════════════════════════════════════")
      for a in played:
        a.affiche()
      print(
          f"\nle paquet du joueur {currentPlayer+1} contient {len(paquetPlayers[currentPlayer])} dominos")
      print("════════════════════════════════════════════════")

      newRound(currentPlayer, lastDomino, pioche, played)
      rounds += 1
      if len(pioche) == 0:
        print("\n════════════════════════════════════════════════")
        print("le jeu est fini il n'y a plus de carte dans la pioche")
      elif len(paquetPlayers[currentPlayer]) == 0:
        print("\n════════════════════════════════════════════════")
        print(
            f"Bravo au joueur {currentPlayer+1} qui a gagné cette partie en {rounds} tours")
        break
  elif players == 2:
    while len(paquetPlayers[currentPlayer]) > 0 or len(pioche) != 0:
      if currentPlayer == 1:
        currentPlayer = 0
      else:
        currentPlayer += 1

      lastDomino = played[-1]
      input("Voulez vous passer au prochain tour : ")
      print(f"\n Tour du joueur n°{currentPlayer+1} / Tour n°{rounds}")
      print("\n════════════════════════════════════════════════")
      for a in played:
        a.affiche()
      print(
          f"\nle paquet du joueur {currentPlayer+1} contient {len(paquetPlayers[currentPlayer])} dominos")
      print("════════════════════════════════════════════════")

      newRound(currentPlayer, lastDomino, pioche, played)
      rounds += 1
      if len(pioche) == 0:
        print("\n════════════════════════════════════════════════")
        print("le jeu est fini il n'y a plus de carte dans la pioche")
      elif len(paquetPlayers[currentPlayer]) == 0:
        print("\n════════════════════════════════════════════════")
        print(
            f"Bravo au joueur {currentPlayer+1} qui a gagné cette partie en {rounds} tours")
        break
else:
  print("Vous avez arreté le jeu.")
