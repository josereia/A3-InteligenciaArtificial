class Player:
    #constructor
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    #fisher method
    def toFish(self):
        return "O jogador vai pescar"