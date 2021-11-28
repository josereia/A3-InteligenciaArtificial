# Aqui é onde será a classe de carta
class Card:
    def __init__(self, value, color=None):
        self.value = value
        self.color = color
        self.weight = 0

    def showCard(self, i=None):
        if (i != None):
            if(self.color == None):
                print("{}) Carta: {}".format(i, self.value))
            else:
                print("{}) Carta: {}-{}".format(i, self.value, self.color))
        else:
            if(self.color == None):
                print("Carta: {}".format(self.value))
            else:
                print("Carta: {}-{}".format(self.value, self.color))
