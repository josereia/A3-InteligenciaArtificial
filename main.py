import random
import os
import deck
import player

player1 = player.Player(1, deck.drawCards(7))
player2 = player.Player("Guilherme", deck.drawCards(7))
print(player1.toFish())