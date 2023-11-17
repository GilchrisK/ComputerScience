#2
import pygame
from sys import exit # closes the window when you call it
pygame.init()
screen = pygame.display.set_mode((600,600)) #width and height
pygame.display.set_caption("Projectile Motion") #Title of the window
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50) # change the font


ground_surface = pygame.image.load("pixel_Background.png")
text_surface = test_font.render("My game", False, "Black")
snail_surface = pygame.image.load("snail.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_surface,(0,0))
    screen.blit(text_surface,(250,80))
    screen.blit(snail_surface,(400,400))


    pygame.display.update()
    clock.tick(60)# Should not run faster than 60 times per second, controls the pace of the game