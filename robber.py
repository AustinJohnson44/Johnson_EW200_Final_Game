import pygame
from settings import *


class Robber(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.right_image = pygame.image.load("assets/tiles/robber.png").convert()
        self.right_image.set_colorkey((0, 0, 0))

        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))

        self.image = self.right_image

        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.image = self.left_image
            self.rect.x -= CHARACTER_SPEED
        elif self.moving_right:
            self.image = self.right_image
            self.rect.x += CHARACTER_SPEED
        if self.moving_up:
            self.rect.y -= CHARACTER_SPEED
        elif self.moving_down:
            self.rect.y += CHARACTER_SPEED
        # make robber stay on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


robber = pygame.sprite.Group()

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
            self.rect.left = player.rect.centerx
            self.rect.bottom = player.rect.centery
