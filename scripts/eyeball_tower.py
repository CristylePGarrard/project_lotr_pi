#!/usr/bin/env python3

import pygame
import time

# config
BMP_PATH = "/home/samwise/lotr/shire/tower_eyeball.bmp"
FRAME_WIDTH = 20
FRAME_HEIGHT = 32
FRAME_COUNT = 15
FPS = 6
SCALE = 4

# init
pygame.init()
screen = pygame.display.set_mode(
        (FRAME_WIDTH * SCALE*1.5, FRAME_HEIGHT * SCALE*1.5) # 7
        )
clock = pygame.time.Clock()


sheet = pygame.image.load(BMP_PATH).convert()
print("Sheet size:", sheet.get_width(), sheet.get_height())
frames = []
for i in range(FRAME_COUNT):
    frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT))
    frame.blit(sheet, (0,0), (0, i * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT))
    frames.append(
            pygame.transform.scale(
                frame,
                (FRAME_WIDTH * SCALE, FRAME_HEIGHT * SCALE)
                )
            )

# MAIN LOOP
clock = pygame.time.Clock()
frame_index = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    screen.blit(frames[frame_index], (0,0))
    pygame.display.flip()

    frame_index = (frame_index + 1) % len(frames)

    clock.tick(10)

pygame.quit()

#screen.fill((50,50,50))
#screen.blit(frames[0], (0, 0))
#pygame.display.flip()

#time.sleep(5)
#pygame.quit()

#screen.fill((255,0,0))
#pygame.display.flip()
#time.sleep(2)

#running=True
#frame_index=0

#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False

#    screen.fill((0,0,0))
#    screen.blit(frames[frame_index], (0,0))

#    frame_index = (frame_index + 1) % FRAME_COUNT
#    clock.tick(FPS)
#pygame.quit()


