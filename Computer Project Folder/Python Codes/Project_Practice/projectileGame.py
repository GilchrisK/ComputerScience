# import pygame
# import math
# from sys import exit
# pygame.init()
# # def click(canonBarrel, canonBarrel_rect):
# #     pos = pygame.mouse.get_pos()
# #
# #     x_dist = pos[0] - canonBarrel
# #     y_dist = - (pos[1] - canonBarrel_rect)
# #     angle = math.degrees(math.atan2(y_dist, x_dist))
# #     pass
# def make_window(width, height, caption) -> pygame.Surface:
#     """Create and return a pygame window."""
#     screen: pygame.Surface
#     screen = pygame.display.set_mode((width, height))
#     pygame.display.set_caption(caption)
#     return screen
#
#
#
# def projectileMotion() -> None:
#     SCREEN_HEIGHT = 1200
#     SCREEN_WIDTH = 800
#     screen: pygame.Surface
#     background: pygame.Surface
#     user_quit = False
#     e: pygame.event.Event
#     projectile: pygame.Surface
#     flag: pygame.Surface
#     start_x = 0
#     start_y = -100
#     x = start_x
#     y = start_y
#     time = 0
#     shoot = False
#     angle = 0
#     speed = 100
#
#     screen = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed: 200")  # width and height
#     # pygame.display.set_caption("Projectile Motion")  # Title of the window
#     background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
#
#     projectile = pygame.image.load("cannon ball.png").convert_alpha()
#     projectile = pygame.transform.scale(projectile,(10,10))
#     projectile_rect = projectile.get_rect(midbottom=(100, 600))
#
#     flag = pygame.image.load("flag.png")
#     flag = flag.convert_alpha()
#
#     start_y = 600 - projectile.get_height()
#     y = start_y
#     clock: pygame.time.Clock = pygame.time.Clock()
#
#     canonWheel = pygame.image.load("cannonWheel7.png").convert_alpha()
#     canonWheel = pygame.transform.scale(canonWheel, (40, 40))
#     canonWheel_rect = canonWheel.get_rect(midbottom=(100, 600))
#
#     canonBarrel = pygame.image.load("cannonBarrel.png").convert_alpha()
#     canonBarrel = pygame.transform.scale(canonBarrel,(35,75))
#     canonBarrel_rect = canonBarrel.get_rect(midbottom=(100, 600))
#
#
#     while not user_quit:
#         clock.tick(30)
#
#         screen.fill('#42afc2')
#         pygame.draw.rect(screen, ("Black"), (0, 745, 1200, 60))  # Bottom menu area
#         pygame.draw.rect(screen, ('Dark Green'), (0, 575, 1200, 170))  # Grass
#         pygame.draw.rect(screen, ("#263436"), (0, 585, 1200, 30))  # Road
#         surface = pygame.draw.line(screen, ("White"), (0, 600), (1200, 600))  # Road line/ SURFACE
#
#
#         screen.blit(projectile,projectile_rect)
#         screen.blit(canonBarrel, canonBarrel_rect)
#         screen.blit(canonWheel, canonWheel_rect)
#
#
#
#
#
#
#         for e in pygame.event.get():
#             if e.type == pygame.QUIT:
#                 user_quit = True
#
#             elif e.type == pygame.KEYDOWN and not shoot:
#                 if e.__dict__["key"] == pygame.K_UP and angle < 90:
#                     angle += 10
#                 elif e.__dict__["key"] == pygame.K_DOWN and angle >= 10:
#                     angle -= 10
#                 elif e.__dict__["key"] == pygame.K_RIGHT:
#                     speed += 10
#                 elif e.__dict__["key"] == pygame.K_LEFT and speed >= 10:
#                     speed -= 10
#                 elif e.__dict__["key"] == pygame.K_SPACE:
#                     shoot = True
#
#         if shoot:
#             # Increment time
#             time += 1 / 15
#             # Calculate location
#             x = (start_x
#                  + math.cos(math.radians(angle)) * speed * time)
#             y = (start_y
#                  - (math.sin(math.radians(angle)) * speed * time)
#                  + .5 * 72 * time ** 2)
#             # Check if it's hit the "ground"
#             if y + projectile.get_height() >= screen.get_height():
#                 time = 0
#                 shoot = False
#                 # Put a flag where it landed
#                 background.blit(flag, (x, screen.get_height() - flag.get_height()))
#                 # Reset projectile to start
#                 x = start_x
#                 y = start_y
#
#             # Draw to the screen and show.
#         pygame.display.set_caption("Angle: " + str(angle) + " Speed: " + str(speed))
#         screen.blit(background, (0, 0))
#         screen.blit(projectile, (x, y))
#         pygame.display.flip()
#
#
#
#     pygame.quit()
#
# projectileMotion()
#
#
#
#
#
#
#
#         #     if event.type == pygame.MOUSEBUTTONDOWN:
#         #         if canonBarrel_rect.collidepoint(event.pos):
#         #             print("True")
#         #     if event.type == pygame.KEYDOWN:
#         #         if event.key == pygame.K_UP:
#         #             changeBarrelPos = 5
#         #         elif event.key == pygame.K_DOWN:
#         #             changeBarrelPos = -5
#         #     elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#         #         changeBarrelPos = 0
#
#
#
#
#         # update everything
#         # runs the screen permanently
#
