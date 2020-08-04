import pygame

posi = 0
vezes = 0
numero = 0
count = 0
class Alien1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global posi, vezes, numero


        self.image = pygame.image.load("data/alien1.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 100, 50, 50)
        posi += 60
        vezes += 1
        self.rect.x = posi
        self.timer = 0
        self.posi = self.rect.x
        self.valorponto = 30
        numero += 1
        self.ID = numero
        self.turn = True
        if vezes == 11:
            vezes = 0
            posi = 0
            numero = 0

    def update(self, *args):
        # global count
        # count += 1
        # if count % 4 == 0:
        if self.rect.x < self.posi:
            self.turn = True
            #self.timer = 1
            self.rect.y = self.rect.y + 50
            self.rect.x = self.posi + 1

        if self.rect.x > self.posi + 150:
            self.turn = False
            #self.timer = -1
            self.rect.y = self.rect.y + 50
            self.rect.x = self.posi + 149

        self.rect.x += self.timer

        # if count == 61:
        #     count = 0
