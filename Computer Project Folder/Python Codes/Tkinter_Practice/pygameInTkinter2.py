import tkinter as tk
import pygame
import os, random
clock = pygame.time.Clock()
 # change the font

root = tk.Tk()
button_win = tk.Frame(root, width = 500, height = 25)
button_win.pack(side = tk.TOP)
embed_pygame = tk.Frame(root, width = 800, height = 800)
embed_pygame.pack(side = tk.TOP)

os.environ['SDL_WINDOWID'] = str(embed_pygame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.display.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Projectile Motion")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     # update everything
#     # runs the screen permanently
#     pygame.display.update()
#     clock.tick(60)

def random_color():
    global circle_color
    circle_color = pygame.Color(0)
    circle_color.hsla = (random.randrange(360), 100, 50, 100)

random_color()
color_button = tk.Button(button_win, text = 'random color',  command = random_color)
color_button.pack(side=tk.LEFT)

def pygame_loop():
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, circle_color, (250, 250), 125)
    pygame.display.flip()
    root.update()
    root.after(100, pygame_loop)

global test_
def layout():
    test_font = pygame.font.Font(None, 50)
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
        clock.tick(60)


layout()
pygame_loop()
tk.mainloop()

#

