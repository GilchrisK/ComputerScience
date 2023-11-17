#6
import pygame
from sys import exit # closes the window when you call it
pygame.init()
screen = pygame.display.set_mode((600,600)) #width and height
pygame.display.set_caption("Projectile Motion") #Title of the window
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50) # change the font


ground_surface = pygame.image.load("pixel_Background_cropped.png").convert_alpha() # converts the image into something that pygame can work with more easily (more smooth)

text_surface = test_font.render("My game", False, "Black").convert_alpha()
text_rect = text_surface.get_rect(center = (300,80))

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
        # if event.type == pygame.MOUSEMOTION: # Prints the coords of where the mouse is whilst its moving
        #     print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN: # Prints output when you hold the mouse down
             print("mouse down")

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,449))
    pygame.draw.rect(screen,"Purple",text_rect,30)
    #pygame.draw.line(screen,"Pink",(0,600),(600,0),10) #draws a line from coord to coord
    #pygame.draw.line(screen,"Pink",(0,600),pygame.mouse.get_pos(),10) #draws a line that you can move the end of it
    pygame.draw.ellipse(screen,"pink",pygame.Rect(50,200,100,100))
    screen.blit(text_surface,text_rect)
    screen.blit(person_surface,player_rect)
    player_rect.right +=1 # This moves the person to the left

    snail_rect.x -=4
    if snail_rect.right <=0: #if the right side of the rectangle is less than 0 then the left part of the snail appears again at x=800
        snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("collsion")

    mouse_position = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_position):
        print("collsion")
        # print(pygame.mouse.get_pressed()) #prints which True/False to the button on the mouse that you are clicking



    pygame.display.update()
    clock.tick(60)# Should not run faster than 60 times per second, controls the pace of the game