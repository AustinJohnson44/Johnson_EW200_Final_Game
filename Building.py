import pygame
from settings import *


class Building(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.wood_wall = pygame.image.load("assets/tiles/wood.png").convert()
        self.wood_wall.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.wood_wall.get_width(), self.wood_wall.get_height())

    def construct_building(self):
        # draw a building onto the screen


    def draw(self, screen):
