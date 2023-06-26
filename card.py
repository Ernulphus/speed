import pygame

class Card:

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self.visibility = "hidden"
        self.zone = "deck"
        self.vis = ["hidden","public","player1","player2"]

    def moveZone(self, destination):
        if type(destination) == type(" "):
            self.zone = destination
    
    def setVisibility(self, v):
        if v in self.vis:
            self.visibility = v
            return self
        else: print("invalid visibility")

    def __str__(self) -> str:
        if self.visibility == "hidden": return "||"

        s = ""
        if self.rank == 11: s += "J"
        elif self.rank == 12: s += "Q"
        elif self.rank == 13: s += "K"
        elif self.rank == 1: s += "A"
        elif self.rank == 10: s += "X"
        elif self.rank > 1 and self.rank < 11: s += str(self.rank)
        else: s += "||"

        if self.suit == "spades": s += "♠"
        if self.suit == "hearts": s += "♥"
        if self.suit == "clubs" : s += "♣"
        if self.suit == "diamonds": s += "♦"
    
        return s
    
