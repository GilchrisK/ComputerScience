import pygame
import sys

pygame. init()

width, height = 400,200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Menu")

white = (255,255,255)
black = (0,0,0)

button_width, button_height = 150, 50
button_x, button_y = (width - button_width) // 2, (height - button_height) // 2

menu_open = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_x < mouse_x <button_x + button_width and button_y < mouse_y < button_y + button_height:
                menu_open = not menu_open

    screen.fill(white)
    pygame.draw.rect(screen, black,(button_x,button_y, button_width, button_height))

    if menu_open:
        pygame.draw.rect(screen, black,(menu_x, menu_y, menu_width, menu_height))

    pygame.display.flip()