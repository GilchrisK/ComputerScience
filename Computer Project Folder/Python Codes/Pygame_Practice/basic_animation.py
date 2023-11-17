
import pygame
from sys import exit # closes the window when you call it
pygame.init()
screen = pygame.display.set_mode((600,600)) #width and height
pygame.display.set_caption("Projectile Motion") #Title of the window
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50) # change the font


ground_surface = pygame.image.load("pixel_Background.png").convert_alpha() # converts the image into something that pygame can work with more easily (more smooth)
text_surface = test_font.render("My game", False, "Black").convert_alpha()

snail_surface = pygame.image.load("snail.png").convert_alpha()
snail_x_pos = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_surface,(0,0))
    screen.blit(text_surface,(250,80))
    snail_x_pos -= 5
    if snail_x_pos < - 100:
        snail_x_pos  = 700
    screen.blit(snail_surface,(snail_x_pos,400))


    pygame.display.update()
    clock.tick(60)# Should not run faster than 60 times per second, controls the pace of the game