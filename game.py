import player
import deck

playerTurn = 0 #turno
playDirection = 1 #
playing = True

discards = []

players = [player.Player("João", deck.drawCards(7)), player.Player("Guilherme", deck.drawCards(7))]
discards.append(deck.deck.pop())

print( str(discards[0].value) )

players[0].play() #realizar jogada de João
#print(deck.showDeck())