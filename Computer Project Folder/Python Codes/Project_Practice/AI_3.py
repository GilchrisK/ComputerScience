import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Game")
clock = pygame.time.Clock()

# Load the player image
player_image = pygame.image.load("cannonBarrel.png")
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
player_speed = 5
player_angle = 0

# Projectile properties
projectile_image = pygame.image.load("cannon ball.png")
projectile_speed = 10
projectile_active = False
projectile_rect = projectile_image.get_rect()
projectile_angle = 0

# Dragging variables
dragging = False
offset_x, offset_y = 0, 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player_rect.collidepoint(event.pos):
                    dragging = True
                    offset_x = event.pos[0] - player_rect.x
                    offset_y = event.pos[1] - player_rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                player_rect.x = event.pos[0] - offset_x
                player_rect.y = event.pos[1] - offset_y

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not projectile_active:
                projectile_active = True
                projectile_rect.center = player_rect.center
                projectile_angle = player_angle

    # Update player angle based on mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_x, mouse_y)):
        player_angle = math.degrees(math.atan2(player_rect.centery - mouse_y, player_rect.centerx - mouse_x)) + 90
        rotated_player = pygame.transform.rotate(player_image, player_angle)
        player_rect = rotated_player.get_rect(center=player_rect.center)

    # Update projectile position if active
    if projectile_active:
        projectile_rect.x += projectile_speed * math.cos(math.radians(projectile_angle))
        projectile_rect.y += projectile_speed * math.sin(math.radians(projectile_angle))

        # Check if the projectile is out of the screen
        if not (0 < projectile_rect.x < WIDTH and 0 < projectile_rect.y < HEIGHT):
            projectile_active = False

    # Draw everything
    screen.fill(BLACK)
    screen.blit(rotated_player, player_rect.topleft)  # Draw the rotated player
    if projectile_active:
        screen.blit(projectile_image, projectile_rect)

    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
