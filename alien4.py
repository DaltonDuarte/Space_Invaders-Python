import pygame
import random

class Alien4(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/alien4.png")
        self.image = pygame.transform.scale(self.image, [70, 30])
        self.rect = pygame.Rect(-60, 100, 70, 30)

        self.timer = 3
        self.valorponto = (100 + (random.randint(1,10))*5)



    def update(self, *args):

        if self.rect.x > 900:
            self.kill()

        self.rect.x += self.timer

