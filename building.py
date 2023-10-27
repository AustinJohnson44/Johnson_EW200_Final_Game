import pygame
from settings import *


class Building(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=SCALE):
        super().__init__()
        img = pygame.image.load("assets/tiles/silver_building.png").convert()
        self.image = pygame.transform.scale(img,
                                            (img.get_width() * scale, img.get_height() * scale))
        self.image.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, screen):
        screen.blit(self.image, self.rect)


city = pygame.sprite.Group()
