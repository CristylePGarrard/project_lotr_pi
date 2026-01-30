#!/usr/bin/env python3

# ----------------------------------------------------------- #
# This is a sample script from pygame to get the ------------ #
# hang of how pygame works. But i left it cause ------------- #
# it's kind of fun to move the ball around the screen ------- #
# ASDW keys are the movement keys. -------------------------- #
# just x out of the window when down and will stop the script #
# ----------------------------------------------------------- #
import pygame

# setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with color to wipe away last frame
    screen.fill("purple")

    # render game
    # draw circle
    pygame.draw.circle(screen, "red", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60)/1000 # limits FPS to 60

pygame.quit()

