class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.playerTurn = 0
        self.playDirection = 0
        self.playing = True
        self.discards = []

    def discard(self, card):
        self.discards.append(card)

    def getDiscardCard(self):
        return self.discards[-1]

    def showDiscardCard(self):
        print("")
        print("------- Descarte -------")
        self.getDiscardCard().showCard()
        print("-------------------------")

    # Método que imprime as cartas do jogador
    def playTurn(self, player):
        self.showDiscardCard()
        print("-------------------------------------------------------")
        print("--> Sua vez {}".format(player.getName()))
        player.showHand()

    def canPlay(self, playerHand):
        for card in playerHand:
            if (card.getValue() == "Curinga" or card.getValue() == "+4"):
                return True
            elif (self.getDiscardCard().getValue() == card.value or self.getDiscardCard().getColor() == card.color):
                return True
        return False

    # Método que define a cor das cartas curingas
    def chooseColor(self): 
        i = 1
        print("-----Escolha uma cor-----")
        for color in self.deck.getColors():
            print("{}) Cor: {}".format(i, color))
            i += 1
        print("-------------------------")
        colorChosen = int(input("Qual cor você quer? "))
        self.getDiscardCard().color = self.deck.getColors()[colorChosen-1]
        print("-------------------------")

    # verifica se a primeira carta virada é um curinga +4
    def firstDiscard(self):
        card = self.deck.drawCards(1)[0]
        while (card.getValue() == "+4"):
            self.deck.insertCard(card)
            card = self.deck.drawCards(1)[0]
        self.discard(card)

    def setPlayerTurn(self):
        if (self.playerTurn == 0):
            self.playerTurn = 1
        else:
            self.playerTurn = 0

    def start(self):
        # primeira carta do jogo
        self.firstDiscard()

        # jogo
        while (self.playing == True):
            # pega o obj do jogador da vez
            player = self.players[self.playerTurn]

            player.sortCard()

            # exibe informações do jogador da vez
            self.playTurn(player)
            # verifica se o jogador da vez possui alguma carta que possa ser jogada
            if(self.canPlay(player.getCards())):
                cardChosen = int(input("Qual carta você quer jogar? "))

                # verifica se a carta escolhida pode ser jogada
                while self.canPlay([player.getCards()[cardChosen-1]]) == False:
                    # caso não, pede pro jogador da vez escolher outra carta
                    print("-------------------------")
                    print("Que pena! Você não pode jogar essa.")
                    cardChosen = int(input("Qual carta você quer jogar? "))
                    print("-------------------------")

                # descarta a carta escolhida pelo jogador da vez
                self.discard(player.discard(cardChosen))

                # Verifica as cartas especiais
                if (self.getDiscardCard().getValue() == "Curinga"):
                    self.chooseColor()
                elif (self.getDiscardCard().getValue() == "+4"):
                    self.setPlayerTurn()
                    self.players[self.playerTurn].toFish(
                        self.deck.drawCards(4))
                    self.chooseColor()
                elif (self.getDiscardCard().getValue() == "+2"):
                    self.setPlayerTurn()
                    self.players[self.playerTurn].toFish(
                        self.deck.drawCards(2))
                elif (self.getDiscardCard().getValue() == "Inverter"):
                    self.players.reverse()
                elif (self.getDiscardCard().getValue() == "Pular"):
                    self.setPlayerTurn()
            else:
                # compra uma carta e pula a vez
                print("Você não pode jogar. Terá que comprar uma carta e passar a vez!")
                player.toFish(self.deck.drawCards(1))
                print("-------------------------------------------------------")

            if(len(player.getCards()) == 0):
                self.playing = False
                print("-------------------------------------------------------")
                print("Você ganhou!")
                print(player.getName())
                print("-------------------------------------------------------")

            # define de quem é a vez
            self.setPlayerTurn()
