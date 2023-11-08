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


class SafeHouse(pygame.sprite.Sprite):

    def __init__(self, x, y, scale=SCALE):
        super().__init__()
        img = pygame.image.load("assets/tiles/safe_house.png").convert()
        self.safe_house_image = pygame.transform.scale(img,
                                                       (img.get_width() * scale, img.get_height() * scale))
        self.safe_house_image.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(x, y, self.safe_house_image.get_width(), self.safe_house_image.get_height())

    def draw(self, screen):
        screen.blit(self.safe_house_image, (self.rect.x, self.rect.y))

