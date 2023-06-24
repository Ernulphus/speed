from pile import Pile

deck = Pile()

p1Deck = Pile(deck.getCards(0,26))
p2Deck = deck

p2Deck.makePublic()
p1Deck.makePublic()

print(p1Deck)
print(p2Deck)