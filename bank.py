import pygame
import robber
from settings import *


class Bank(pygame.sprite.Sprite):

    def __init__(self, x, y, scale=SCALE):
        super().__init__()
        img = pygame.image.load("assets/tiles/bank.png").convert()
        self.bank_image = pygame.transform.scale(img,
                                                 (img.get_width() * scale, img.get_height() * scale))
        self.bank_image.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.bank_image.get_width(), self.bank_image.get_height())

    def draw(self, screen):
        screen.blit(self.bank_image, (self.rect.x, self.rect.y))


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coin_image = pygame.image.load("assets/tiles/Coin.png").convert()
        self.coin_image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(x, y, self.coin_image.get_width(), self.coin_image.get_height())
        self.collected = False

    def draw(self, screen):
        screen.blit(self.coin_image, (self.rect.x, self.rect.y))

    def update(self, player):
        if self.collected:
            self.rect.center = player.rect.center

