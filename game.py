import player
import deck
import discard

playerTurn = 0 #turno
playDirection = 1 #
playing = True


players = [player.Player("João", deck.drawCards(7)), player.Player("Guilherme", deck.drawCards(7))]
discard.discards.append(deck.unoDeck.pop())

players[0].showLastCardOnDiscards() #Pega a ultima carta do discards
print(len(discard.discards)) #Exibe a quantidade de cartas dentro do discrads

print("-----------")
players[0].play()
print("-----------")

print(len(discard.discards))
players[0].showLastCardOnDiscards()
#print(deck.showDeck())