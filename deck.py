import random
from card import Card


class Deck:
    def __init__(self):
        self.unoDeck = []
        self.colors = ["Azul", "Verde", "Amarelo", "Vermelho"]
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Inverter", "Pular", "+2"]
        self.wilds = ["Curinga", "+4"]

        for color in self.colors:
            for value in self.values:
                for i in range(2):
                    self.unoDeck.append(Card(value, color))
        for wild in self.wilds:
            for i in range(4):
                self.unoDeck.append(Card(wild))
        self.unoDeck = random.sample(self.unoDeck, 112)

    def getUnoDeck(self):
        return self.unoDeck

    def getColors(self):
        return self.colors

    def insertCard(self, card):
        self.unoDeck.insert(0, card)
        
    def drawCards(self, numCards):
        cardsDrawn = []  # Armazena as cartas distribuidas
        for i in range(numCards):
            cardsDrawn.append(self.unoDeck.pop())
        return cardsDrawn