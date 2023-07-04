from card import Card
from random import shuffle

class Pile:
    def __init__(self, order = []):
        if order == []:
            self.deck = self.fullDeck()
        else:
            self.deck = order

    def getCards(self, start=0, end=-1):
        r = self.deck[start:end]
        self.deck = self.deck[:start] + self.deck[end:]
        return r
    
    def readCard(self, index=-1):
        if index < len(self):
            return str(self.deck[index])
        else: return " "
    
    def readCardRank(self, index=-1):
        return self.deck[index].rank
    
    def shuff(self):
        shuffle(self.deck)
    
    def pop(self, index = -1):
        if len(self.deck) < 1: return None
        return self.deck.pop(index)
    
    def push(self, card):
        self.deck.append(card)

    def top(self):
        return str(self.deck[-1])

    def makePublic(self):
        for c in self.deck:
            c.setVisibility("public")
    
    def hide(self):
        for c in self.deck:
            c.setVisibility("hidden")

    def fullDeck(self):
        deck = []
        for r in range(1,14):
            for s in ["spades", "hearts", "clubs", "diamonds"]:
                deck.append(Card(r, s))
        return deck

    def __str__(self) -> str:
        s = ""
        for c in self.deck:
            s += str(c) + " "
        return s
    
    def __len__(self) -> int:
        return len(self.deck)
    
    def __add__(self, cards):
        self.deck.append(cards)
        return self