import player
import deck

playerTurn = 0
playDirection = 1
playing = True

discards = []

players = [player.Player("João", deck.drawCards(7)), player.Player("Guilherme", deck.drawCards(7))]
discards.append(deck.unoDeck.pop(0))

while playing:
    players[playerTurn].showHand()
    print("Carta descartada: {}".format(discards[-1]))