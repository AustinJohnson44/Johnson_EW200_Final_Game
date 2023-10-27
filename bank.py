import pygame
from settings import *


class Bank(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.bank = pygame.image.load("assets/tiles/bank.png").convert()
        self.bank.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.bank.get_width(), self.bank.get_height())

    def draw(self, screen):
        screen.blit(self.bank, (self.rect.x, self.rect.y))