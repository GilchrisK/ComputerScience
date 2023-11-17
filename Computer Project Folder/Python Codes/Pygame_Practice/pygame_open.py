# 1
import pygame
from sys import exit


def open():  # closes the window when you call it
    pygame.init()
    screen = pygame.display.set_mode((800, 800))  # width and height
    pygame.display.set_caption("Projectile Motion")  # Title of the window
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # update everything
        # runs the screen permanently
        pygame.display.update()
        clock.tick(60)