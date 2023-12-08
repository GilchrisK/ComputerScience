import pygame
from tkinter import *
from sys import exit


def projectileQuiz():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))  # width and height
    pygame.display.set_caption("Projectile Motion Quiz")  # Title of the window


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # update everything
        # runs the screen permanently
        pygame.display.update()