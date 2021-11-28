class Player:
    # constructor
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def showHand(self):
        print("-----------------------------")
        print("{}'s hand:".format(self.name))
        print("-----------------------------")

        i = 1
        for card in self.cards:
            card.showCard(i)
            i += 1

        print("-----------------------------")

    # fisher method
    def toFish(self):
        return "O " + str(self.name) + "vai pescar"

    def canPlay(self):
        return
