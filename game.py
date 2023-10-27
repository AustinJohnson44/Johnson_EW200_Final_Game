import pygame
import sys
import random
import safe_house
import bank
from building import Building, city
from settings import *

pygame.init()  # tells pygame to look/listen for inputs and events

screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))
pygame.display.set_caption("Cops and Robbers")

plain_grass = pygame.image.load("assets/tiles/plain_grass.png").convert()
plain_grass.set_colorkey((0, 0, 0))
textured_grass = pygame.image.load("assets/tiles/textured_grass.png").convert()
textured_grass.set_colorkey((0, 0, 0))

# create safe house in bottom left corner
my_safe_house = safe_house.SafeHouse(CITY_LEFT, CITY_BOTTOM)
# create a bank in the top right corner
my_bank = bank.Bank(CITY_RIGHT, CITY_TOP)
# create city buildings
# for b in range(NUM_BUILDINGS):
    # city.add(Building(random.randint(CITY_LEFT + TILE_SIZE, CITY_RIGHT - TILE_SIZE),
                      # random.randint(CITY_TOP + TILE_SIZE, CITY_BOTTOM - TILE_SIZE)))
for h in range(CITY_TOP // TILE_SIZE, CITY_BOTTOM // TILE_SIZE, 7):
    for i in range((CITY_LEFT // TILE_SIZE) + 4, (CITY_RIGHT // TILE_SIZE), 7):  # // to give quotient and not a float
        city.add(Building(TILE_SIZE * i, TILE_SIZE * h))


background = screen.copy()  # makes a second copy of the screen/canvas
clock = pygame.time.Clock()


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

    my_safe_house.draw(screen)
    my_bank.draw(screen)

    city.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # locks game to 60fps
