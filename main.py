import pygame
from src.model.Cardgame import CardGame
from src.view.View import View

def blackjack():
    deck = CardGame().createDeck()
    deck.shuffle()
    print(deck.cards[0])

    pygame.init()

    maxForce = 0.2

    FPS = 10
    fpsClock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    view = View(1280, 720, fpsClock, font)

    #controller = Controller(screen, model)
    #screen.setController(controller)
    # screen.update()
    running = True
    while (running):
        view.update(deck)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        print(pygame.mouse.get_pos())
        fpsClock.tick(FPS)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    blackjack()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
