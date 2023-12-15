import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cannon Game")

# Cannon parameters
cannon_length = 50
cannon_width = 20
cannon_color = RED
cannon_angle = 45

# Projectile parameters
projectile_radius = 10
projectile_color = WHITE
projectile_speed = 10
projectile = None

# Function to calculate angle between two points
def calculate_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

# Main game loop
running = True
dragging = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Update cannon angle based on mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cannon_angle = calculate_angle(WIDTH // 2, HEIGHT, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and projectile is None:
                # Shoot projectile when spacebar is pressed
                projectile_angle = math.radians(cannon_angle)
                projectile_dx = projectile_speed * math.cos(projectile_angle)
                projectile_dy = -projectile_speed * math.sin(projectile_angle)
                projectile = {
                    'x': WIDTH // 2,
                    'y': HEIGHT - cannon_length,
                    'dx': projectile_dx,
                    'dy': projectile_dy
                }

    # Update projectile position
    if projectile is not None:
        projectile['x'] += projectile['dx']
        projectile['y'] += projectile['dy']

        # Check if the projectile is out of bounds
        if not (0 <= projectile['x'] <= WIDTH and 0 <= projectile['y'] <= HEIGHT):
            projectile = None

    # Draw everything
    screen.fill(BLACK)

    # Draw cannon
    pygame.draw.rect(screen, cannon_color, (WIDTH // 2 - cannon_width // 2, HEIGHT - cannon_length, cannon_width, cannon_length))

    # Draw projectile
    if projectile is not None:
        pygame.draw.circle(screen, projectile_color, (int(projectile['x']), int(projectile['y'])), projectile_radius)

    pygame.display.flip()

pygame.quit()
