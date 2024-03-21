import math
import pygame # Imports and initialize pygame.
pygame.init()


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
    time = 0
    shoot = False
    angle = 0
    speed = 100
    graph_icon2: pygame.Surface
    moving = False








    screen = projectile_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed: 200")
    bigHorizontal_ruler_surface = pygame.image.load("x_ruler3.png").convert_alpha()
    ground_x = 0
    ground_y = screen.get_height() - 150
    bigHorizontal_ruler = bigHorizontal_ruler_surface.get_rect(midbottom=(ground_x + 600, ground_y + 21))
    ground_surface = pygame.image.load("grass_surface.png").convert_alpha()
    graph_x = screen.get_height() + 300
    graph_y = screen.get_height() - 780
    # xruler_x = screen.get_height() + 300
    # xruler_y = screen.get_height() - 690
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((222, 237, 244))
    projectile = pygame.image.load("cannon ball.png")
    projectile = projectile.convert_alpha()
    flag = pygame.image.load("flag.png")
    flag = flag.convert_alpha()
    graph_icon2 = pygame.image.load("graph_icon2.png")
    graph_icon2 = graph_icon2.convert_alpha()
    horizontal_ruler_surface = pygame.image.load("x_ruler1.png").convert_alpha()
    horizontal_ruler = horizontal_ruler_surface.get_rect(midbottom = (screen.get_height() + 325,screen.get_height() - 690))
    start_y = screen.get_height() - ground_surface.get_height() - projectile.get_height()
    y = start_y
    clock: pygame.time.Clock = pygame.time.Clock()




    while not user_quit:
        # Loop 30 times per second
        clock.tick(30)

        for e in pygame.event.get():
            # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
            # Process keys to adjust angle and shoot.
            elif e.type == pygame.KEYDOWN and not shoot:
                if e.__dict__["key"] == pygame.K_UP and angle < 90:
                    angle += 5
                elif e.__dict__["key"] == pygame.K_DOWN and angle >= 10:
                    angle -= 5
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    speed += 10
                elif e.__dict__["key"] == pygame.K_LEFT and speed >= 10:
                    speed -= 10
                elif e.__dict__["key"] == pygame.K_SPACE:
                    shoot = True

        mouse_position = pygame.mouse.get_pos()
        if horizontal_ruler.collidepoint(mouse_position):

            if e.type == pygame.MOUSEBUTTONDOWN:  # Prints output when you hold the mouse down
                background.blit((bigHorizontal_ruler_surface), (bigHorizontal_ruler))

                print("yes")
        #         for e in pygame.event.get():
        #             if e.tye == pygame.MOUSEBUTTONUP:
        #                 moving = False
        #             elif e.type == pygame.MOUSEBUTTONDOWN:
        #                 bigHorizontal_ruler.collidepoint(e.pos)
        #                 moving = True
        #             elif e.type == pygame.MOUSEMOTION and moving:
        #                 bigHorizontal_ruler.move_ip(e.rel)
        # pygame.display.update()









        # Move the projectile through the air
        if shoot:
            # Increment time
            time += 1 / 15

            # Calculate location
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
                x = start_x
                y = start_y


        # Draw to the screen and show.
        pygame.display.set_caption("Angle: " + str(angle) + " Speed: " + str(speed))
        screen.blit(background, (0, 0))
        screen.blit(projectile, (x, y))
        screen.blit(ground_surface,(ground_x,ground_y))
        screen.blit(graph_icon2,(graph_x, graph_y))
        screen.blit(horizontal_ruler_surface,(horizontal_ruler))
        # pygame.draw.circle(screen,"#000000", (int(x), int(y)), 5)
        pygame.display.flip()

    pygame.quit()


main()
