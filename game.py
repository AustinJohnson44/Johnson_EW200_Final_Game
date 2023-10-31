import pygame
import sys
import random
import safe_house
import bank
import robber
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
h_road = pygame.image.load("assets/tiles/road3.png").convert()
horizontal_road = pygame.transform.scale(h_road,
                                         (h_road.get_width() * 2, h_road.get_height() * 2))
horizontal_road.set_colorkey((0, 0, 0))
v_road = pygame.image.load("assets/tiles/road8.png").convert()
vertical_road = pygame.transform.scale(v_road,
                                       (v_road.get_width() * 2, v_road.get_height() * 2))
vertical_road.set_colorkey((0, 0, 0))

# create city buildings
for a in range(0, SCREEN_HEIGHT // TILE_SIZE, 7):
    for b in range(0, (SCREEN_WIDTH // TILE_SIZE), 7):
        building = Building(TILE_SIZE * b, TILE_SIZE * a)
        city.add(building)
# create safe house in bottom left corner
my_safe_house = safe_house.SafeHouse(0, SCREEN_HEIGHT - 4 * TILE_SIZE)
# create a bank in the top right corner
my_bank = bank.Bank(SCREEN_WIDTH - 3 * TILE_SIZE, 0)
# create a robber on the screen
my_robber = robber.Robber(4 * TILE_SIZE, SCREEN_HEIGHT - 4 * TILE_SIZE)


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
    # make road system
    # make horizontal roads
    for h in range(4 * TILE_SIZE, SCREEN_HEIGHT, 7 * TILE_SIZE):
        for i in range(0, SCREEN_WIDTH, TILE_SIZE):
            x = i
            y = h
            background.blit(horizontal_road, (x, y))
    # make vertical roads
    for i in range(4 * TILE_SIZE, SCREEN_WIDTH, 7 * TILE_SIZE):
        for h in range(0, SCREEN_HEIGHT, TILE_SIZE):
            x = i
            y = h
            background.blit(vertical_road, (x, y))


draw_background()

while True:

    # listen for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            pygame.quit()  # stops process that pygame.init started
            sys.exit()  # uber break - breaks out of everything

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_robber.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_robber.moving_right = True
            if event.key == pygame.K_UP:
                my_robber.moving_up = True
            if event.key == pygame.K_DOWN:
                my_robber.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_robber.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_robber.moving_right = False
            if event.key == pygame.K_UP:
                my_robber.moving_up = False
            if event.key == pygame.K_DOWN:
                my_robber.moving_down = False

    # update game objects
    city.update()
    my_robber.update()

    # check for collisions
    pygame.sprite.spritecollide(my_safe_house, city, True)
    pygame.sprite.spritecollide(my_bank, city, True)
    if my_robber.rect.colliderect(my_safe_house):
        if my_robber.rect.right == my_safe_house.rect.right:
            my_robber.rect.left = my_safe_house.rect.right
    for building in city:
        if my_robber.rect.colliderect(building.rect):
            if my_robber.rect.right == building.rect.right:
                my_robber.moving_left = False
                my_robber.rect.left = building.rect.right
            if my_robber.rect.left == building.rect.left:
                my_robber.moving_right = False
                my_robber.rect.right = building.rect.left
            if my_robber.rect.top == building.rect.top:
                my_robber.moving_down = False
                my_robber.rect.bottom = building.rect.top
            if my_robber.rect.bottom == building.rect.bottom:
                my_robber.moving_up = False
                my_robber.rect.top = building.rect.bottom

    # draw game screen
    screen.blit(background, (0, 0))

    city.draw(screen)
    my_safe_house.draw(screen)
    my_bank.draw(screen)
    my_robber.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # locks game to 60fps
