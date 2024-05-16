import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join 
pygame.init()

pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 50
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_bacjground(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()
    

if __name__ == "__main__":
    main(window)