# Aqui é onde será a classe de carta
class Card:
    def __init__(self, color, value):
        self.key = 0
        self.color = color
        self.value = value
        self.weight = self.defineWeight()

    def defineWeight (self):
        if (self.value == "Reverse"):
            return 2
        elif (self.value == "Skip"):
            return 3
        elif (self.value == "+2"):
            return 4
        elif (self.value == "Wild"):
            return 5
        elif (self.value == "+4"):
            return 6
        else:
            return 1
        