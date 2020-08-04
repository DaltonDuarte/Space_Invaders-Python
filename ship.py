import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        #player = pygame.sprite.Sprite(drawGrup)
        self.image = pygame.image.load("data/ship.png")
        self.image = pygame.transform.scale(self.image, [50, 25])
        self.rect = pygame.Rect(475, 875, 50, 50)
        self.speed = 0


    def update(self, *args):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rect.x -= 5

        if key[pygame.K_d]:
            self.rect.x += 5

        if self.rect.x < 50:
            self.rect.x = 50

        if self.rect.x > 800:
            self.rect.x = 800