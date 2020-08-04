import pygame

class ShotAlien(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shotAlien.png")
        self.image = pygame.transform.scale(self.image, [5, 15])
        self.rect = self.image.get_rect()

        self.speed = 10


    def update(self, *args):

        self.rect.y += self.speed

        if self.rect.top > 900:
            self.kill()
