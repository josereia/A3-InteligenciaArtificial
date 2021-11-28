import deck


class Game:
    def __init__(self, playerss):
        self.players = playerss
        self.numPlayers = len(playerss)
        self.playerTurn = 0  # turno
        self.playDirection = 1
        self.playing = True
        self.discards = []

    def canPlay(self, discartCard, playerHand):
        for card in playerHand:
            if(discartCard.value == "Wild"):
                return True
            elif discartCard.value == card.value or discartCard.color == card.color:
                return True
        return False

    def discard(self, card):
        self.discards.append(card)

    def discardCard(self):
        return self.discards[-1]

    def firstDiscard(self):
        firstDiscardCard = deck.unoDeck.pop()
        while firstDiscardCard.value == "Wild" or firstDiscardCard.value == "+4"

    def start(self):
        # tira a primeira carta do monte/deck
        self.discards.append()

        # jogo em sí
        while self.playing:
            # mostra as cartas do jogador da vez.
            self.players[self.playerTurn].showHand()

            # mostra a carta descartada.
            print("Topo da pilha de descartados: ")
            self.discardCard().showCard()
            print("---------------")

            # verifica se o jogador da vez terá ou não de comprar uma carta
            if(self.canPlay(self.discardCard(), self.players[self.playerTurn].cards)):
                # pede para o jogador escolher uma carta
                cardChosen = int(input("Qual carta você quer jogar? "))
                # verifica se a carta pode ser jogada seguindo as regras
                while not self.canPlay(self.discardCard(), [self.players[self.playerTurn].cards[cardChosen-1]]):
                    print("---------------")
                    print("Que pena! Você não pode jogar essa.")
                    cardChosen = int(input("Qual carta você quer jogar? "))
                    print("---------------")

                # exibe a carta jogada
                print("Você jogou: ")
                self.players[self.playerTurn].cards[cardChosen-1].showCard()
                print("---------------")
                # põe a carta jogada no monte de discarte
                self.discards.append(
                    self.players[self.playerTurn].cards.pop(cardChosen-1))

            else:
                # compra uma carta pro jogador da vez
                print("Você não pode jogar. Terá que comprar uma carta!")
                self.players[self.playerTurn].cards.extend(deck.drawCards(1))

            # verifica a direção do jogo e de quem é a vez
            self.playerTurn += self.playDirection
            if self.playerTurn == self.numPlayers:
                self.playerTurn = 0
            elif self.playerTurn < 0:
                self.playerTurn = self.numPlayers-1
