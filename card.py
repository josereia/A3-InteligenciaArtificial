# Aqui é onde será a classe de carta
class Card:
    def __init__(self, value, color=None):
        self.value = value
        self.color = color
        self.weight = self.defineWeight()

    def defineWeight(self):
        if (self.value == "Inverter"):
            return 2
        elif (self.value == "Pular"):
            return 3
        elif (self.value == "+2"):
            return 4
        elif (self.value == "Curinga"):
            return 5
        elif (self.value == "+4"):
            return 6
        else:
            return 1

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

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
