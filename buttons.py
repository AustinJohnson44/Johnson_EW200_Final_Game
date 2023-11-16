import pygame
from settings import *


class Buttons(pygame.sprite.Sprite):
    def __init__(self, name, color):
        super().__init__()
        self.font = pygame.font.Font("assets/fonts/game_font.ttf", TITLE_SIZE)
        self.text = self.font.render(name, True, color)


