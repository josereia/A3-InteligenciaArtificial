import random
import card

deck = []

def buildDeck():
    
    colors = ["Red", "Blue", "Yellow", "Green"]
    values = [0,1,2,3,4,5,6,7,8,9, "Reverse", "Skip", "+2"]
    wilds = ["Wild", "+4"]

    for color in colors: #Percorre a lista de colols
        
        for value in values: # Dentro de cada cor, obtem um valor da lista de values
            deck.append( card.Card(color,value))

            if value !=0: # Adiciana mais uma carta de cada cor, difere de zero
                deck.append(card.Card(color,value))
            
    # Adiciona as cartas especiais    
    for i in range(4):
        deck.append( card.Card("wild",wilds[0]) )
        deck.append( card.Card("wild",wilds[1]) )
        
    #retorna baralho randomizado
    return random.sample(deck, 107)
"""
Essa função distribui as cartas
remove a carta do bolo de cartas
E adiciona na variavel cardsDrawn
"""
def drawCards(numCards):
    cardsDrawn = [] # Armazena as cartas distribuidas
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

def showDeck(): # Mostra todas as cartas do baralho
    list = []
    for x in range(0,len(deck)):
        apelidoCarta = deck[x].color + "-" + str(deck[x].value)
        list.append(apelidoCarta)
    return list

# Instancia a função
unoDeck = buildDeck()


