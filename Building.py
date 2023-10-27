import pygame
from settings import *


class Building(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()


        self.rect = pygame.rect.Rect(x, y, self.safe_house.get_width(), self.safe_house.get_height())


