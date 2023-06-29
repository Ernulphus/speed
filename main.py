from pile import Pile
import pygame


pygame.init()
X, Y = 1280, 720
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True
dt = 0

deck = Pile()
deck.shuff()

p1Deck = Pile(deck.getCards(0,26))
p2Deck = deck

p1Hand = Pile(p1Deck.getCards(-8, -1))
p2Hand = Pile(p2Deck.getCards(-8, -1))

dutch1 = Pile([p1Deck.pop().setVisibility("public")])
dutch2 = Pile([p2Deck.pop().setVisibility("public")])

p1Hand.makePublic()

font = pygame.font.SysFont('couriernew', 45)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hand loading
    p1HandRender = [font.render(str(p1Hand.readCard(i)), True, "black", "white") for i in range(len(p1Hand))]
    p1textRect = [p1HandRender[i].get_rect() for i in range(len(p1HandRender))]
    for i in range(len(p1textRect)):
        p1textRect[i].center = ((X // 4) + (i * 100), (Y // 2) + 200)

    p2HandRender = [font.render(str(p2Hand.readCard(i)), True, "black", "white") for i in range(len(p2Hand))]
    p2textRect = [p2HandRender[i].get_rect() for i in range(len(p2HandRender))]
    for i in range(len(p1textRect)):
        p2textRect[i].center = ((X // 4) + (i * 100), (Y // 2) - 200)

    # Dutch piles loading
    # Note to self: when putting card onto dutch pile, remember to make it publicly visible!
    dutch1Render = font.render(str(dutch1.readCard()), True, "black", "white")
    dutch1Rect = dutch1Render.get_rect()
    dutch1Rect.center = (X // 2 - 100, Y // 2)
    dutch2Render = font.render(str(dutch2.readCard()), True, "black", "white")
    dutch2Rect = dutch2Render.get_rect()
    dutch2Rect.center = (X // 2 + 100, Y // 2)

    # Decks and deck number loading
    p1DeckRender = font.render(str(p1Deck.readCard()) + str(len(p1Deck)), True, "black", "white")
    p1DeckRect = p1DeckRender.get_rect()
    p1DeckRect.center = (X // 2 + 230, Y // 2) 
    p2DeckRender = font.render(str(len(p2Deck)) + str(p2Deck.readCard()), True, "black", "white")
    p2DeckRect = p2DeckRender.get_rect()
    p2DeckRect.center = (X // 2 - 230, Y // 2)

    # Render all
    screen.fill("lightgray")
    for i in range(len(p1HandRender)):
        screen.blit(p1HandRender[i], p1textRect[i])

    for i in range(len(p2HandRender)):
        screen.blit(p2HandRender[i], p2textRect[i])

    screen.blit(dutch1Render, dutch1Rect)
    screen.blit(dutch2Render, dutch2Rect)
    screen.blit(p1DeckRender, p1DeckRect)
    screen.blit(p2DeckRender, p2DeckRect)

    pygame.display.update()

print("P2 Hand", p2Hand)
print("P2 Deck:", len(p2Deck), "cards")
print("\t", dutch1.top(), dutch2.top())
print("P1 Deck:", len(p1Deck), "cards")
print("P1 Hand", p1Hand)