#4
import pygame
from sys import exit # closes the window when you call it
pygame.init()
screen = pygame.display.set_mode((600,600)) #width and height
pygame.display.set_caption("Projectile Motion") #Title of the window
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50) # change the font


ground_surface = pygame.image.load("pixel_Background_cropped.png").convert_alpha() # converts the image into something that pygame can work with more easily (more smooth)
text_surface = test_font.render("My game", False, "Black").convert_alpha()
sky_surface = pygame.image.load("sky.png").convert_alpha()

snail_surface = pygame.image.load("snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,449))

person_surface = pygame.image.load("person.png").convert_alpha()
player_rect = person_surface.get_rect(midbottom = (50,449)) #takes person_surface and creates a rectangle around it

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,449))
    screen.blit(text_surface,(250,80))

    screen.blit(person_surface,player_rect)
    player_rect.right +=1 # This moves the person to the left

    snail_rect.x -=4
    if snail_rect.right <=0: #if the right side of the rectangle is less than 0 then the left part of the snail appears again at x=800
        snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)


    pygame.display.update()
    clock.tick(60)# Should not run faster than 60 times per second, controls the pace of the game