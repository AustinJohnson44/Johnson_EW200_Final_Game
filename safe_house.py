import pygame
from settings import *


class SafeHouse(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.safe_house_image = pygame.image.load("assets/tiles/safe_house.png").convert()
        self.safe_house_image.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.safe_house_image.get_width(), self.safe_house_image.get_height())

    def draw(self, screen):
        screen.blit(self.safe_house_image, (self.rect.x, self.rect.y))
