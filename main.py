import os
import platform
from player import Player
from deck import Deck
from game import Game

"""
Identifica o sistema operacional
para dar o comando correto de 
limpar o terminal.
"""
if (platform.system() == "Windows"):
    os.system("cls")
else:
    os.system("clear")


"""
Instancia a classe Deck.
Define o nome do jogador e IA.
Intancia a classe Game e inicia
o jogo.
"""
deck = Deck()

playerName = str(input("Insira seu nome: "))
players = [
    Player(playerName, deck.drawCards(7)),
    Player("IA", deck.drawCards(7))
]

Game(deck, players).start()