class Player:
    # constructor
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def getName(self):
        return self.name

    def getCards(self):
        return self.cards

    def discard(self, cardChosen):
        card = self.cards[cardChosen-1]
        print("Você jogou: {}-{}".format(card.getValue(), card.getColor()))
        print("-------------------------")
        return self.cards.pop(cardChosen-1)

    def toFish(self, cards):
        self.cards.extend(cards)

    def showHand(self):
        #print("-------------------------------------------------------")
        print("Digite o valor referente a carta que deseja selecionar.")
        print("-------------------------------------------------------")

        i = 1
        for card in self.cards:
            card.showCard(i)
            i += 1

        print("-------------------------------------------------------")
