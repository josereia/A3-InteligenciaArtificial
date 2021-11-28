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
        lastCardOnDiscarted = self.returnLastCardOnDiscards() #Chama a carta que está por cima do discards
        contador = 0
        list = []

        if ( len(self.cards) == 0  ): #Verifica se o Player tem cartas ainda
            print("Acabou as cartas")
        else:
            print("Ainda há cartas")
            """
            for card in self.cards:
                if (card.color == lastCardOnDiscarted.color):
                    print("É igual")
                else:
                    print("Não é igual")
                contador += 1
            """

    def discardCard(self, value):
        global discards
        
        if (self.cards[value].weight == discards[-1].weight):
            if (self.cards[value].color == discards[-1].color):
                print("É da mesma cor")
                discards.append(self.cards.pop(value))
            elif (self.cards[value].color == discards[-1].color):
                print("É do mesmo valor")
                discards.append(self.cards.pop(value))
            else:
                print(" ----> Ops, essa carta não pode ser jogada")
        else:
            print("----->   Carta de tipos diferentes")

        print("Voce discartou a carta de valor: " + str(self.cards[value].color) + "-" +  str(self.cards[value].value))
        

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
