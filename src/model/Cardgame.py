from src.model.Deck import Deck
from src.model.Card import Card

class CardGame:

    def __init__(self):
        self.values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.colors = ["clubs","Diamonds","Hearts","Spades"]

    def createDeck(self,n=1):
        deck = Deck()
        for color in self.colors:
            for value in self.values:
                path = "card"+color+value
                deck.addCard(Card(path,value,color))
        return deck
