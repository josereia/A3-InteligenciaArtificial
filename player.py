class Player:
    # constructor
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    # fisher method
    def toFish(self):
        return "O jogador vai pescar"

    def showHand(self):
        print("-----------------------------")
        print("Player {}".format(self.name))
        print("-----------------------------")
        print("Your hand:")
        for card in self.cards:
            print(card)
        print("-----------------------------")
