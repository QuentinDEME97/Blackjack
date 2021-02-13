class Card:

    def __init__(self, imgPath, value, color):
        self.imgPath = imgPath
        self.value = value
        self.color = color
        self.translate = {"clubs" : "trèfle","Diamonds":"carreau","Hearts":"coeur","Spades":"pique"}

    def getName(self):
        val = self.value
        if self.value == "K": val = "Roi"
        if self.value == "J": val = "Valet"
        if self.value == "Q": val = "Dame"
        if self.value == "A": val = "As"

        return val + " de " + self.translate[self.color]

    def __repr__(self):
        return self.getName()