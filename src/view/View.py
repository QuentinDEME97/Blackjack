import pygame
from src.model.Deck import Deck

class View:

    def __init__(self, width, height, fpsClock, font):
        self.title = "Blackjack"
        self.width = width
        self.height = height
        self.clock = fpsClock
        self.font = font
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill("white")
        self.tablePath = "assets/tabletop.png"

    def update(self, deck):
        pygame.display.set_caption(self.title)
        self.screen.fill("white")
        img = pygame.image.load(self.tablePath)
        img = pygame.transform.scale(img, (self.width, self.height))
        rect = img.get_rect()
        rect = rect.move(0,0)
        self.screen.blit(img, rect)

        self.drawCards(deck)

        pygame.draw.line(self.screen,(255,0,0),(640,0),(640,720))

        fps = self.font.render(str(int(self.clock.get_fps())), True, (255, 255, 255), (0, 0, 0))
        self.screen.blit(fps, (0, 0))
        pygame.display.flip()

    def drawCards(self,deck):
        # 470, 500 ==> 810
        size = (47,64)
        #size = (140,190)
        middle = self.width/2
        n = 5
        shift = 10
        f = middle - (size[0])*(n/2) - (shift*(n//2))
        print("info",f,middle)
        acc = 0
        for i in range(n):
            cardImg = pygame.image.load("assets/boardgamepack/PNG/cards/"+deck.cards[i].imgPath+".png")
            cardImg = pygame.transform.scale(cardImg, size)
            self.screen.blit(cardImg,(f + ((size[0]*i) + shift*i),500 - size[1]))
            acc = i+1

        # Bank
        nn = 2
        fb = middle - (size[0]) * (nn / 2) - (shift * (nn // 2))
        for i in range(nn):
            cardImg = pygame.image.load("assets/boardgamepack/PNG/cards/"+deck.cards[i+acc].imgPath+".png")
            cardImg = pygame.transform.scale(cardImg, size)
            self.screen.blit(cardImg,(fb + ((size[0]*i) + shift*i),210 + size[1]))

        # Deck
        cardBackImg = pygame.image.load("assets/boardgamepack/PNG/cards/cardBack_red3.png")
        cardBackImg = pygame.transform.scale(cardBackImg, size)
        surf = pygame.transform.rotate(cardBackImg, 0)
        self.screen.blit(surf, (770,210))
        #self.screen.blit(cardBackImg, (f,200))
