import discard

discards = discard.discards
class Player:
    # constructor
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

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
        for card in self.cards:
            print(str(card.value) + "-" + str(card.color) + " peso: " + str(card.weight))
            #verifica se cartas do jogador tem o mesmo peso da ultima carta de descartados
            if (card.weight <= 4):

                if (card.color == lastCardOnDiscarted.color):
                    print("  --> É da mesma cor! " + str(card.color) + "-" + str(card.value))
                    #print(str(self.cards[contador].color) )
                    discards.append(self.cards.pop(contador))
                    print(" O " + str(self.name) + " Jogou uma carta ")
                    break
                
                elif (card.value == lastCardOnDiscarted.value):
                    print("  --> As cartas são do mesmo valor")
                    discards.append(self.cards.pop(contador))
                    print(" O " + str(self.name) + " Jogou uma carta ")
                    break
                    
            elif (card.weight == 5):
                print(" O " + str(self.name) + " mudou de cor ")
                discards.append(self.cards.pop(contador))
            
            elif (card.weight == 6):
                print(" O " + str(self.name) + " jogou um +4")
                discards.append(self.cards.pop(contador))
                
            contador += 1

            
        
        
    

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
    
