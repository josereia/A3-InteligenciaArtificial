import player
import deck
import game

players = []

numPlayers = int(input("Quantos jogadores? "))
print("----------------------------")
for i in range(numPlayers):
    playerName = str(input("Qual o nome do " + str(i+1) + "º jogador? "))
    players.append(player.Player(playerName, deck.drawCards(7)))

newGame = game.Game(players)
newGame.start()