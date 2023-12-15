import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GROUND_HEIGHT = 50
CANON_LENGTH = 100
GRAVITY = 0.1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion Game")

# Font for text rendering
font = pygame.font.Font(None, 36)

# Game variables
cannon_angle = 45  # Initial angle
cannon_x, cannon_y = 50, HEIGHT - GROUND_HEIGHT
projectile_speed = 10  # Initial speed
projectile = None
dragging_cannon = False
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cannon_x <= event.pos[0] <= cannon_x + CANON_LENGTH and \
                    cannon_y - CANON_LENGTH <= event.pos[1] <= cannon_y:
                dragging_cannon = True
            elif projectile is None and 650 <= event.pos[0] <= 750 and 500 <= event.pos[1] <= 550:
                # Fire projectile when the "Fire" button is clicked
                projectile = [cannon_x + CANON_LENGTH, cannon_y - CANON_LENGTH]
                projectile_speed = 10  # Reset speed

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_cannon = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging_cannon:
                # Adjust cannon angle based on mouse movement
                cannon_angle = math.degrees(math.atan2(cannon_y - event.pos[1], event.pos[0] - cannon_x))

    # Update game logic
    if projectile:
        projectile[0] += projectile_speed * math.cos(math.radians(cannon_angle))
        projectile[1] -= projectile_speed * math.sin(math.radians(cannon_angle))
        projectile_speed += GRAVITY  # Apply gravity

        # Check if projectile hits the ground
        if projectile[1] >= HEIGHT - GROUND_HEIGHT:
            projectile = None
            projectile_speed = 10  # Reset speed

        # Check if projectile hits the target
        target_rect = pygame.Rect(600, 400, 50, 50)
        projectile_rect = pygame.Rect(projectile[0] - 5, projectile[1] - 5, 10, 10)
        if projectile_rect.colliderect(target_rect):
            score += 10
            projectile = None
            projectile_speed = 10  # Reset speed

    # Draw background
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT - GROUND_HEIGHT))
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    # Draw cannon
    pygame.draw.line(screen, BLACK, (cannon_x, cannon_y), (cannon_x + CANON_LENGTH * math.cos(math.radians(cannon_angle)),
                                                            cannon_y - CANON_LENGTH * math.sin(math.radians(cannon_angle))), 5)

    # Draw target
    pygame.draw.rect(screen, RED, (600, 400, 50, 50))

    # Draw projectile
    if projectile:
        pygame.draw.circle(screen, BLUE, (int(projectile[0]), int(projectile[1])), 5)

    # Draw "Fire" button
    pygame.draw.rect(screen, BLUE, (650, 500, 100, 50))
    text = font.render("Fire", True, WHITE)
    screen.blit(text, (680, 515))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
