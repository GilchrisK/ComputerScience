#8
import pygame
from sys import exit # closes the window when you call it

def display_score():
    current_time= int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f'{current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (300,50))
    screen.blit(score_surface,score_rect)



pygame.init()
screen = pygame.display.set_mode((600,600)) #width and height
pygame.display.set_caption("Projectile Motion") #Title of the window
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50) # change the font
game_active = True
start_time = 0
jump_sound = pygame.mixer.Sound("Mario-jump-sound.mp3")
background_Music = pygame.mixer.Sound("Monkeys-Spinning-Monkeys(chosic.com).mp3")
background_Music.play(loops= -1)

ground_surface = pygame.image.load("pixel_Background_cropped.png").convert_alpha() # converts the image into something that pygame can work with more easily (more smooth)

score_surface = test_font.render("My game", False, "Black").convert_alpha()
score_rect = score_surface.get_rect(center = (300, 80))


sky_surface = pygame.image.load("sky.png").convert_alpha()


snail_surface = pygame.image.load("snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,449))

player_surface = pygame.image.load("person.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50,449)) #takes person_surface and creates a rectangle around it
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION: # Prints the coords of where the mouse is whilst its moving
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN: # Prints output when you hold the mouse down
        #      print("mouse down")
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE and player_rect.bottom >=449:
                    player_gravity = -25
                    jump_sound.play()
                    jump_sound.set_volume(0.5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >=449:
                    player_gravity = -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,449))
        # pygame.draw.rect(screen,"Purple", score_rect, 30)
        # pygame.draw.ellipse(screen,"Brown",pygame.Rect(50,200,100,100))
        # screen.blit(score_surface, score_rect)
        display_score()

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 449: #these two lines of code makes sure the player does not pass the ground when falling
            player_rect.bottom = 449
        screen.blit(player_surface,player_rect)



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

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("Red")

    pygame.display.update()
    clock.tick(60)# Should not run faster than 60 times per second, controls the pace of the game