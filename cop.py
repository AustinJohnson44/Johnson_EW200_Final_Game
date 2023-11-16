import pygame
import math
from settings import *


class Cop(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.right_image = pygame.image.load("assets/tiles/police_officer.png").convert()
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
        elif self.moving_right:
            self.image = self.right_image
        # make robber stay on screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.moving_left = False
            self.moving_right = True
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.moving_right = False
            self.moving_left = True
        if self.rect.top < 0:
            self.rect.top = 0
            self.moving_up = False
            self.moving_down = True
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.moving_down = False
            self.moving_up = True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def chase_player(self, player):
        # if coin_collected:
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        angle = math.atan2(dy, dx)
        speed = 3 * CHARACTER_SPEED/4  # Set the cop's speed here
        if math.cos(angle) > 0:
            self.moving_left = False
            self.moving_right = True
        if math.cos(angle) < 0:
            self.moving_right = False
            self.moving_left = True
        if math.sin(angle) > 0:
            self.moving_up = False
            self.moving_down = True
        if math.sin(angle) < 0:
            self.moving_down = False
            self.moving_up = True
        self.rect.x += speed * math.cos(angle)
        self.rect.y += speed * math.sin(angle)


police = pygame.sprite.Group()
