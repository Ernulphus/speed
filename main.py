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
p1HandRender = [font.render(str(p1Hand.readCard(i)), True, "black", "white") for i in range(len(p1Hand))]
p1textRect = [p1HandRender[i].get_rect() for i in range(len(p1HandRender))]
for i in range(len(p1textRect)):
    p1textRect[i].center = ((X // 4) + (i * 60), (Y // 2) + 200)

p2HandRender = [font.render(str(p2Hand.readCard(i)), True, "black", "white") for i in range(len(p2Hand))]
p2textRect = [p2HandRender[i].get_rect() for i in range(len(p2HandRender))]
for i in range(len(p1textRect)):
    p2textRect[i].center = ((X // 4) + (i * 60), (Y // 2) - 200)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lightgray")
    for i in range(len(p1HandRender)):
        screen.blit(p1HandRender[i], p1textRect[i])

    for i in range(len(p2HandRender)):
        screen.blit(p2HandRender[i], p2textRect[i])

    pygame.display.update()

print("P2 Hand", p2Hand)
print("P2 Deck:", len(p2Deck), "cards")
print("\t", dutch1.top(), dutch2.top())
print("P1 Deck:", len(p1Deck), "cards")
print("P1 Hand", p1Hand)