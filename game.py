import os
import player
import deck
import discard

cleanerterminal = 'cls'
os.system(cleanerterminal)

playerTurn = 0 #turno
playDirection = 1 #
playing = True


players = [
    player.Player(input("Insira seu nome: "), deck.drawCards(7), False),
    player.Player("IA", deck.drawCards(7), True)
]
discard.discards.append(deck.unoDeck.pop())

while (playing == True):
    
    
    #Vez do jogador zero
    if (playerTurn == 0):
        print("* Quantidade de cartas já discartadas : " + str(len(discard.discards)) + " *" + "\n" + "-----------------------------" + "\n" )
        lista = []
        for card in discard.discards:
            data = str(card.value) + "-" +  str(card.color)
            print(data)
        print("-------------")

        players[0].showLastCardOnDiscards()
        print("  --> Sua vez " + str(players[0].name) + ", escolha uma das cartas: " + "\n")

        players[0].showHand()
        selectedValue = input("Digite aqui: ")
        players[0].discardCard(int(selectedValue))
        playerTurn = 1
    elif (playerTurn == 1):
        print("Vez da IA")
        players[1].play()
        
            
        playing = False
        

 #Pega a ultima carta do discards
"""
print(len(discard.discards)) #Exibe a quantidade de cartas dentro do discrads
players[0].showLastCardOnDiscards()

players[0].showHand()
print("-----------")
players[0].play()
print("-----------")



print(len(discard.discards))
players[0].showLastCardOnDiscards()

#print(deck.showDeck())
"""