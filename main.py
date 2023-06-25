from pile import Pile

deck = Pile()
deck.shuff()

p1Deck = Pile(deck.getCards(0,26))
p2Deck = deck

p1Hand = Pile(p1Deck.getCards(-8, -1))
p2Hand = Pile(p2Deck.getCards(-8, -1))

dutch1 = Pile([p1Deck.pop().setVisibility("public")])
dutch2 = Pile([p2Deck.pop().setVisibility("public")])


p1Hand.makePublic()

print("P2 Hand", p2Hand)
print("P2 Deck:", len(p2Deck), "cards")
print("\t", dutch1.top(), dutch2.top())
print("P1 Deck:", len(p1Deck), "cards")
print("P1 Hand", p1Hand)