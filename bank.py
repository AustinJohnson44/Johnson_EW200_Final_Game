import pygame
from settings import *


class Bank(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.bank_image = pygame.image.load("assets/tiles/bank.png").convert()
        self.bank_image.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.bank_image.get_width(), self.bank_image.get_height())

    def draw(self, screen):
        screen.blit(self.bank_image, (self.rect.x, self.rect.y))
