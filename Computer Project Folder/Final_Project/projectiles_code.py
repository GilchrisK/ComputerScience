import tkinter as tk
import math
from matplotlib import pyplot as plt
import numpy as np
import pygame # Imports and initialize pygame.
pygame.init()


def open_tkinter_page():
    root = tk.Tk()
    root.title("Tkinter Page")

    label = tk.Label(root, text="This is a Tkinter page opened from Pygame!")
    label.pack()

    root.mainloop()

def display_graph(u_speed, before_time):
    time = np.linspace(0, before_time, 100)
    speed = u_speed - 9.8 * time

    distance = u_speed * time - 0.5 * 9.8 * time ** 2
    plt.figure(figsize=(10,6))

    plt.subplot(2,1,1)
    plt.plot(time, speed, color="blue", label="speed")
    plt.ylabel("Speed")
    plt.xlabel("Time")
    plt.title("Speed vs Time")
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time, distance, color="Red", label="Distance")
    plt.ylabel("Distance")
    plt.xlabel("Time")
    plt.title("Distance vs Time")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


def projectile_window(width, height, caption):
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen


def main() -> None:
    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 1200

    screen: pygame.Surface
    background: pygame.Surface
    user_quit = False
    e: pygame.event.Event
    projectile: pygame.Surface
    flag: pygame.Surface
    ground_surface: pygame.Surface
    start_x = 10
    start_y = -100
    x = start_x
    y = start_y
    shoot = False
    angle = 0
    speed = 100
    time = 0
    graph_icon2: pygame.Surface
    trajectory_points = []

    screen = projectile_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed: 200 Time: 0")
    bigHorizontal_ruler_surface = pygame.image.load("x_ruler3.png").convert_alpha()
    ground_x = 0
    ground_y = screen.get_height() - 150
    bigHorizontal_ruler = bigHorizontal_ruler_surface.get_rect(midbottom=(ground_x + 600, ground_y + 21))
    ground_surface = pygame.image.load("grass_surface.png").convert_alpha()
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((222, 237, 244))
    projectile = pygame.image.load("cannon ball.png")
    projectile = projectile.convert_alpha()
    flag = pygame.image.load("flag.png").convert_alpha()
    horizontal_ruler_surface = pygame.image.load("x_ruler.png").convert_alpha()
    horizontal_ruler = horizontal_ruler_surface.get_rect(midbottom = (screen.get_height() + 325,screen.get_height() - 550))
    start_y = screen.get_height() - ground_surface.get_height() - projectile.get_height()
    y = start_y
    clock: pygame.time.Clock = pygame.time.Clock()

    graph_icon2 = pygame.image.load("graph_icon2.png")
    graph_icon2_rect = graph_icon2.get_rect(topleft= (1100,10))

    line_icon = pygame.image.load("line.png")
    line_icon_rect = line_icon.get_rect(topleft=(1000,20))

    exit_icon = pygame.image.load("exit_btn.png")
    exit_icon_rect = exit_icon.get_rect(topleft=(1070,738))





    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if graph_icon2_rect.collidepoint(e.pos):
                    display_graph(speed, time)
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RETURN:
                    display_graph(speed, time)

            # Process keys to adjust angle and shoot.
            elif e.type == pygame.KEYDOWN and not shoot:
                if e.__dict__["key"] == pygame.K_UP and angle < 90:
                    angle += 5
                elif e.__dict__["key"] == pygame.K_DOWN and angle >= 10:
                    angle -= 5
                elif e.__dict__["key"] == pygame.K_RIGHT and speed <=280:
                    speed +=5
                elif e.__dict__["key"] == pygame.K_LEFT and speed >= 10:
                    speed -= 10
                elif e.__dict__["key"] == pygame.K_SPACE:
                    shoot = True
                    trajectory_points.clear()
                    x = start_x
                    y = start_y

        mouse_position = pygame.mouse.get_pos()
        if horizontal_ruler.collidepoint(mouse_position):
            if e.type == pygame.MOUSEBUTTONDOWN:  # Prints output when you hold the mouse down
                background.blit((bigHorizontal_ruler_surface), (bigHorizontal_ruler))

        mouse_position = pygame.mouse.get_pos()
        if exit_icon_rect.collidepoint(mouse_position):
            if e.type == pygame.MOUSEBUTTONDOWN:
                from Projectiles_HomePage import run_homePage
                pygame.quit()
                run_homePage()






#############################################


        # Move the projectile through the air
        if shoot:
            # Increment time
            time += 1/15


            # Calculate the location
            x = (start_x
                 + math.cos(math.radians(angle)) * speed * time)
            y = (start_y
                 - (math.sin(math.radians(angle)) * speed * time)
                 + .5 * 72 * time ** 2)
            # Check if it's hit the "ground"
            if y + projectile.get_height() >= screen.get_height() - ground_surface.get_height() :
                time = 0
                shoot = False
                # Put a flag where it landed
                background.blit(flag, (x, screen.get_height() - ground_surface.get_height() - flag.get_height() + 4 )) # Without the +4 the flag slightly levitates above the ground
                # Reset projectile to start




            if x >= start_x:
                trajectory_points.append((int(x), int(y)))


        # Draw to the screen and show.
        pygame.display.set_caption("Angle: " + str(angle) + " Speed: " + str(speed/5) + " Time: " + str(time))
        screen.blit(background, (0, 0))
        screen.blit(projectile, (x, y))
        screen.blit(ground_surface,(ground_x,ground_y))
        screen.blit(graph_icon2,(1100,20))
        screen.blit(horizontal_ruler_surface,(horizontal_ruler))
        screen.blit(line_icon,(1000,20))
        screen.blit(exit_icon,(1070,738))

        mouse_position = pygame.mouse.get_pos()
        if line_icon_rect.collidepoint(mouse_position):
            if e.type == pygame.MOUSEBUTTONDOWN:
                if shoot and len(trajectory_points) > 1:
                    pygame.draw.lines(screen, (255,0,0), False, trajectory_points,2)

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_1:
                if shoot and len(trajectory_points) > 1:
                    pygame.draw.lines(screen, (255, 0, 0), False, trajectory_points, 2)


        pygame.display.flip()

    pygame.quit()


main()

