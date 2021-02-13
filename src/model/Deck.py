import random

class Deck:

    def __init__(self):
        self.cards = []
        self.ingame = []
        self.outgame = []

    def addCard(self, card):
        self.cards.append(card)
        self.ingame.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
