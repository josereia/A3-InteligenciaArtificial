class BehaverTree:
    def __init__(self, cards, discardCard):
        self.cards = cards
        self.discardCard = discardCard
        self.optionList = []

    def getCards(self):
        return self.cards

    def getDiscardCard(self):
        return self.discardCard

    def getOptionList(self):
        return self.optionList

    def AddOptionList(self, value):
        self.optionList.append(value)

    # Função que define a melhor jogada
    def decision(self):
        self.optionList.clear()
        for card in self.cards:
            if (card.getValue() == "Curinga" or card.getValue() == "+4"):
                self.AddOptionList(card)
            elif (self.getDiscardCard().getValue() == card.value or self.getDiscardCard().getColor() == card.color):
                self.AddOptionList(card)
        
        '''
        print("Possibilidades de cartas da IA jogar: " + str(len(self.optionList)))
        print("São elas: ")
        for card in self.optionList:
            card.showCard()

        print("A carta escolhida será: ")
        self.optionList[0].showCard()
        '''
        return self.getOptionList()[0]