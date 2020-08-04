import pygame

class ShotShip(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shotShip.png")
        self.image = pygame.transform.scale(self.image, [3, 15])
        self.rect = self.image.get_rect()

        self.speed = 17


    def update(self, *args):

        self.rect.y -= self.speed

        if self.rect.top < 0:
            self.kill()
