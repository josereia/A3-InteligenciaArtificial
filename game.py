import os
import player
import deck
import discard
import playing

cleanerterminal = 'cls'
os.system(cleanerterminal)

playerTurn = 0 #turno
playDirection = 1 #



players = [
    player.Player(input("Insira seu nome: "), deck.drawCards(7), False),
    player.Player("IA", deck.drawCards(7), True)
]
discard.discards.append(deck.unoDeck.pop())

while (playing.playing == True):
    
    
    #Vez do jogador zero
    if (playerTurn == 0):
        
        # Ordena as cartas do jogador
        def get_key_weight(v):
            return v.weight
        players[0].cards.sort(key=get_key_weight)

        print("* Quantidade de cartas já discartadas : " + str(len(discard.discards)) + " *" + "\n" + ("-----------------------------") + "\n" )
        lista = []
        for card in discard.discards:
            data = str(card.value) + "-" +  str(card.color)
            print(data)
        print("-----------------------------")

        players[0].showLastCardOnDiscards()
        print("  --> Sua vez " + str(players[0].name) + ", escolha uma das cartas: " + "\n")
        
        
        players[0].showHand()
        selectedValue = input("Digite aqui: ")
        players[0].discardCard(int(selectedValue))
        
        if ( len(players[0].cards) == 0): #Verifica se o jogador não possui mais cartas
            playing.playing == False
            print("------------ FIM DO JOGO -----------------")
            break

    elif (playerTurn == 1):
        
        print("* Quantidade de cartas já discartadas : " + str(len(discard.discards)) + " *" + "\n" + "-----------------------------" + "\n" )
        lista = []
        for card in discard.discards:
            data = str(card.value) + "-" +  str(card.color)
            print(data)
        print("-------------")

        players[1].showLastCardOnDiscards()
        print("  --> Sua vez " + str(players[1].name) + ", escolha uma das cartas: " + "\n")

        players[1].showHand()
        selectedValue = input("Digite aqui: ")
        players[1].discardCard(int(selectedValue))
        playerTurn = 0
        

 #Pega a ultima carta do discards
"""
print(len(discard.discards)) #Exibe a quantidade de cartas dentro do discrads
players[0].showLastCardOnDiscards()

#players[0].cards.sort()
players[0].showHand()
print("-----------")
players[0].play()
print("-----------")



print(len(discard.discards))
players[0].showLastCardOnDiscards()

#print(deck.showDeck())
"""