class Player:
    # constructor
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def play(self):
        print(" O " + str(self.name) + "vai realizar a próxima jogada ")

    # fisher method
    def toFish(self):
        print(" O " + str(self.name) + "vai pescar ")

    def showHand(self):
        print("-----------------------------")
        print("Player {}".format(self.name))
        print("-----------------------------")
        print("Your hand:")
        for card in self.cards:
            print( str(card.value) + "-" + str(card.color))
        print("-----------------------------")
    
