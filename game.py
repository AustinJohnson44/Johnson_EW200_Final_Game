import pygame
import sys
import random
import robber
import bank
import safe_house
from cop import Cop, police
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

level = 1  # initialize level


def spawn_cops(num_cops):
    for i in range(num_cops):
        popo = Cop(random.randint(0, SCREEN_WIDTH - TILE_SIZE), random.randint(0, SCREEN_HEIGHT - TILE_SIZE))
        police.add(popo)


# create city buildings
for a in range(0, SCREEN_HEIGHT // TILE_SIZE, 7):
    for b in range(0, (SCREEN_WIDTH // TILE_SIZE), 7):
        my_building = Building(TILE_SIZE * b, TILE_SIZE * a)
        city.add(my_building)

# create safe house in bottom left corner
my_safe_house = safe_house.SafeHouse(0, SCREEN_HEIGHT - 4 * TILE_SIZE)
# create a bank in the top right corner
my_bank = bank.Bank(SCREEN_WIDTH - 3 * TILE_SIZE, 0)
# create coin object on bank
my_coin = bank.Coin(SCREEN_WIDTH - 2 * TILE_SIZE, (3/2) * TILE_SIZE)
# create a robber on the screen
my_robber = robber.Robber(4 * TILE_SIZE, SCREEN_HEIGHT - 4 * TILE_SIZE)
# create a cop
spawn_cops(1)


background = screen.copy()  # makes a second copy of the screen/canvas
clock = pygame.time.Clock()


def draw_game_background():
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


draw_game_background()


while True:
    # game
    print(f"Level: {level}")
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
        my_robber.update()
        my_coin.update(my_robber)
        police.update()

        # check for collisions
        # get rid of city buildings at same location as safe house and bank
        pygame.sprite.spritecollide(my_safe_house, city, True)
        pygame.sprite.spritecollide(my_bank, city, True)
        # collision with bank
        if my_robber.rect.colliderect(my_coin):
            my_coin.collected = True
            for cop in police:
                cop.chase_player(my_robber)
        # collision between cop and robber
        if pygame.sprite.spritecollide(my_robber, police, False) and my_coin.collected:
            print(f"Thanks for playing! You got caught by the robber :(")
            pygame.quit()
            sys.exit()
        # collision with safe house
        if my_robber.rect.colliderect(my_safe_house) and my_coin.collected:
            print(f"Your score is: {1000 * level**2}")
            level += 1
            break
        # collision between the robber and buildings in city
        for building in city:
            # collisions for player
            if my_robber.rect.colliderect(building.rect):
                # Determine the direction of collision
                if (my_robber.rect.right >= building.rect.left and my_robber.moving_right
                        and building.rect.top <= my_robber.rect.centery <= building.rect.bottom):
                    # collision from left
                    my_robber.rect.right = building.rect.left
                if (my_robber.rect.left <= building.rect.right and my_robber.moving_left
                        and building.rect.top <= my_robber.rect.centery <= building.rect.bottom):
                    # collision from right
                    my_robber.rect.left = building.rect.right
                if (my_robber.rect.bottom >= building.rect.top and my_robber.moving_down
                        and building.rect.left <= my_robber.rect.centerx <= building.rect.right):
                    # collision from top
                    my_robber.rect.bottom = building.rect.top
                if (my_robber.rect.top <= building.rect.bottom and my_robber.moving_up
                        and building.rect.left <= my_robber.rect.centerx <= building.rect.right):
                    # collision from bottom
                    my_robber.rect.top = building.rect.bottom
            # collisions with cops
            for cop in police:
                for b in city:
                    if cop.rect.colliderect(building.rect):
                        # Determine the direction of collision
                        if (cop.rect.right >= building.rect.left and cop.moving_right
                                and building.rect.top <= cop.rect.centery <= building.rect.bottom):
                            # collision from left
                            cop.rect.right = building.rect.left
                        if (cop.rect.left <= building.rect.right and cop.moving_left
                                and building.rect.top <= cop.rect.centery <= building.rect.bottom):
                            # collision from right
                            cop.rect.left = building.rect.right
                        if (cop.rect.bottom >= building.rect.top and cop.moving_down
                                and building.rect.left <= cop.rect.centerx <= building.rect.right):
                            # collision from top
                            cop.rect.bottom = building.rect.top
                        if (cop.rect.top <= building.rect.bottom and cop.moving_up
                                and building.rect.left <= cop.rect.centerx <= building.rect.right):
                            # collision from bottom
                            cop.rect.top = building.rect.bottom

        # draw game screen
        screen.blit(background, (0, 0))

        city.draw(screen)
        my_safe_house.draw(screen)
        my_bank.draw(screen)
        my_robber.draw(screen)
        my_coin.draw(screen)
        if my_coin.collected:
            police.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # locks game to 60fps

    # change game characteristics between levels
    my_coin.collected = False
    my_coin = bank.Coin(SCREEN_WIDTH - 2 * TILE_SIZE, (3 / 2) * TILE_SIZE)
    my_robber = robber.Robber(4 * TILE_SIZE, SCREEN_HEIGHT - 4 * TILE_SIZE)
    spawn_cops(1)
