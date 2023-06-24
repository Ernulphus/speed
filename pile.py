from card import Card

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
    
    def makePublic(self):
        for c in self.deck:
            c.setVisibility("public")

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