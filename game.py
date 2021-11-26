import player
import deck

playerTurn = 0 #turno
playDirection = 1 #
playing = True

discards = []

players = [player.Player("João", deck.drawCards(7)), player.Player("Guilherme", deck.drawCards(7))]
discards.append(deck.unoDeck.pop(0))
print( players[0].toFish() )