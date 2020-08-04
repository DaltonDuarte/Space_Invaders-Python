import pygame

posi = 0
vezes = 0
numero = 0
class Wall(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global posi, vezes, numero

        self.image = pygame.image.load("data/wall.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 700, 100, 100)


        vezes += 1
        posi += 170
        numero += 1

        self.rect.x = posi
        self.ID = numero
        self.vida = 10

        if vezes == 4:
            posi = 0
            vezes = 0
            numero = 0


