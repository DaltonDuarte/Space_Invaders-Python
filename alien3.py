import pygame

s = True
posi = 0
vezes = 0
descer = 0
numero = 33
count = 0
class Alien3(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global posi, vezes, s, descer, numero
        self.image = pygame.image.load("data/alien3.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 295, 50, 50)
        if vezes == 22:
            vezes = 0
            posi = 0
            numero = 0
            s = True
            descer = 0
        posi += 60
        vezes += 1
        if vezes > 11 :
            if s or vezes == 23:
                posi = 60
                descer += 65
                s = False
            self.rect.y = self.rect.y + descer
        self.rect.x = posi
        self.timer = 0
        self.posi = self.rect.x
        self.valorponto = 10
        numero += 1
        self.ID = numero
        self.turn = True

    def update(self, *args):
        # global count
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


