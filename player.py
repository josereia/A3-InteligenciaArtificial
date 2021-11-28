from card import Card
import discard

discards = discard.discards
class Player:
    # constructor
    def __init__(self, name, cards, IA):
        self.name = name
        self.cards = cards
        self.IA = IA

    def get_cards(self):
        return self.cards

    def showLastCardOnDiscards(self): #Exibe a ultima carta do baralho de descartadas
        global discards
        print("A ultima carta do baralho é: " + str(discards[-1].value)+ "-" + str(discards[-1].color))

    def returnLastCardOnDiscards(self): #return the last card on discard
        global discards
        return discards[-1]

    def play(self): #Esse métoto é onde a IA irá jogar
        global discards
        lastCardOnDiscarted = self.returnLastCardOnDiscards()
        contador = 0
        list = []
        for card in self.cards:
            if (card.color == lastCardOnDiscarted.color):
                print("É igual")
            else:
                print("Não é igual")
            contador += 1
        
        
    def discardCard(self, value):
        global discards
        print("Voce discartou a carta de valor " + str(self.cards[value].color) + "-" +  str(self.cards[value].color))
        discards.append(self.cards.pop(value))

    # fisher method
    def toFish(self):
        print(" O " + str(self.name) + "vai pescar ")

    def showHand(self):
        contador = 0
        print("-----------------------------")
        print("Digite o valor referente a à carta que deseja selecionar: ")
        print("-----------------------------")
        print("Your hand:")
        for card in self.cards:
            print( "[" + str(contador) + "] " +str(card.value) + "-" + str(card.color))
            contador += 1
        print("-----------------------------")
    
