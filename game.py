import pygame
import sys
import random
from settings import *

pygame.init()  # tells pygame to look/listen for inputs and events

screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))  # collapsed variables inside parenthesis
background = screen.copy()  # makes a second copy of the screen/canvas
clock = pygame.time.Clock()

plain_grass = pygame.image.load("assets/tiles/plain_grass.png").convert()
plain_grass.set_colorkey((0, 0, 0))
textured_grass = pygame.image.load("assets/tiles/textured_grass.png").convert()
textured_grass.set_colorkey((0, 0, 0))
dirt = pygame.image.load("assets/tiles/dirt.png").convert()
dirt.set_colorkey((0, 0, 0))


def draw_background():
    background.fill((0, 0, 0))
    # make a grass bottom
    for h in range(SCREEN_HEIGHT // TILE_SIZE):
        for i in range(SCREEN_WIDTH // TILE_SIZE):  # // to give quotient and not a float
            background.blit(plain_grass, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE*(h + 1)))
        # add textured grass
        for i in range(random.randint(0, SCREEN_WIDTH // TILE_SIZE)):
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT - TILE_SIZE*(h + 1)
            background.blit(textured_grass, (x, y))


draw_background()

while True:

    # listen for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            pygame.quit()  # stops process that pygame.init started
            sys.exit()  # uber break - breaks out of everything

    # draw game screen
    screen.blit(background, (0, 0))

    pygame.display.flip()
    clock.tick(60)  # locks game to 60fps

