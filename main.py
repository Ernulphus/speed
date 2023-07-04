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

discard = Pile([])

p1Hand.makePublic()

font = pygame.font.SysFont('couriernew', 45)

cardSelect = ['a', 's', 'd', 'f', 'w', 'e', 'r']
PLAYDUTCH1, PLAYDUTCH2 = 'j', 'k'
DRAW = ' '
CLEAR = ';'
selectedIndex = -1
AIspeed = 2500
AImoveCounter = AIspeed
stuck = False

def adjacent(rank1, rank2):
    return (rank1 - rank2) % 13 == 12 or (rank1 - rank2) % 13 == 1

def hasPlayableCard(pile):
    for i in range(len(pile)):
        if adjacent(pile.readCardRank(i), dutch1.readCardRank()):
            return True
        if adjacent(pile.readCardRank(i), dutch2.readCardRank()):
            return True
    return False

def gameEnd():
    if len(p1Deck) + len(p1Hand) < 1:
        print("Player 1 wins!")
        return True
    if len(p2Deck) + len(p2Hand) < 1:
        print("Player 2 wins!")
        return True
    if stuck and len(p1Deck) < 1 and len(p2Deck) < 1:
        if len(p1Hand) > len(p2Hand):
            print("Player 2 wins!")
            return True
        else:
            print("Player 1 wins!")
            return True
    return False

while running and not gameEnd():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode in cardSelect:
                selectedIndex = cardSelect.index(event.unicode)
                if selectedIndex >= len(p1Hand):
                    selectedIndex = len(p1Hand) - 1 # Cap selection to last card in hand
            
            elif event.unicode == PLAYDUTCH1 and selectedIndex > -1:
                if adjacent(p1Hand.readCardRank(selectedIndex), dutch1.readCardRank()):
                    # Move selected card to top of dutch pile
                    dutch1.push(p1Hand.pop(selectedIndex).setVisibility("public"))
                    selectedIndex -= 1
            elif event.unicode == PLAYDUTCH2 and selectedIndex > -1:
                if adjacent(p1Hand.readCardRank(selectedIndex), dutch2.readCardRank()):
                    # Move selected card to top of dutch pile
                    dutch2.push(p1Hand.pop(selectedIndex).setVisibility("public"))
                    selectedIndex -= 1
            
            elif event.unicode == DRAW and len(p1Hand) < 7:
                if len(p1Deck) > 0:
                    p1Hand.push(p1Deck.pop().setVisibility("player1"))

            elif event.unicode == CLEAR and stuck:
                discard = discard + dutch1.getCards() + dutch2.getCards
                if len(p1Deck) > 0:
                    dutch1.push(p1Deck.pop().setVisibility("public"))
                else:
                    dutch1.push(p2Deck.pop().setVisibility("public"))
                if len(p2Deck) > 0:
                    dutch2.push(p2Deck.pop().setVisibility("public"))
                else:
                    dutch2.push(p1Deck.pop().setVisibility("public"))
                


    # AI player
    if AImoveCounter > 0:
        AImoveCounter -= 1
    else:
        if not hasPlayableCard(p2Hand) and len(p2Hand) < 7 and len(p2Deck) > 0:
            p2Hand.push(p2Deck.pop().setVisibility("player2"))
        for card in range(len(p2Hand)):
            if adjacent(p2Hand.readCardRank(card), dutch1.readCardRank()):
                dutch1.push(p2Hand.pop(card).setVisibility("public"))
                break
            elif adjacent(p2Hand.readCardRank(card), dutch2.readCardRank()):
                dutch2.push(p2Hand.pop(card).setVisibility("public"))
                break
        AImoveCounter = AIspeed

    if hasPlayableCard(p1Hand) or hasPlayableCard(p2Hand):
        stuck = False
    else:
        stuck = True

    # Hand loading
    p1HandRender = [font.render(str(p1Hand.readCard(i)), True, "black", "white") for i in range(len(p1Hand))]
    p1textRect = [p1HandRender[i].get_rect() for i in range(len(p1HandRender))]
    for i in range(len(p1textRect)):
        p1textRect[i].center = ((X // 4) + (i * 100), (Y // 2) + 200)

    p2HandRender = [font.render(str(p2Hand.readCard(i)), True, "black", "white") for i in range(len(p2Hand))]
    p2textRect = [p2HandRender[i].get_rect() for i in range(len(p2HandRender))]
    for i in range(len(p2textRect)):
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

    if stuck:
        stuckText = font.render("Stuck.", True, "black", "lightgray")
        stuckTextRect = stuckText.get_rect()
        stuckTextRect.center = (X // 10, Y // 7)
        screen.blit(stuckText, stuckTextRect)
    

    # Card selector rectangle
    if selectedIndex > -1:
        selectorCornerNWx, selectorCornerNWy = (X // 4) - 30 + (selectedIndex * 100), (Y // 2) + 170
        pygame.draw.rect(screen, "lightgreen", pygame.Rect(selectorCornerNWx, selectorCornerNWy, 60, 60), 5)
        pygame.display.flip()

    pygame.display.update()