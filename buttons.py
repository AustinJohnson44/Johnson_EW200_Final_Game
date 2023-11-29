import pygame
from settings import *


class Buttons(pygame.sprite.Sprite):
    def __init__(self, name, text_color, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.font = pygame.font.Font("assets/fonts/game_font.ttf", TITLE_SIZE)
        self.text = name
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
