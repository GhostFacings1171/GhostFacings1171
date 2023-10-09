import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 900
HEIGHT = 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.jump_height = -10
        self.bird_width = 70
        self.bird_height = 70

    def jump(self):
        self.velocity = self.jump_height

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.bird_width, self.bird_height))

# Pipe class
# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH + 110  # Aumenta a distância entre os canos
        self.pipe_width = 90  # Aumenta a largura do cano
        self.gap_height = 215  # Aumenta a altura da lacuna
        self.top_height = random.randint(50, HEIGHT - self.gap_height - 50)

    def move(self):
        self.x -= 3

    def draw(self):
        pygame.draw.rect(win, GREEN, (self.x, 0, self.pipe_width, self.top_height))
        pygame.draw.rect(win, GREEN, (self.x, self.top_height + self.gap_height, self.pipe_width, HEIGHT - self.top_height - self.gap_height))
 

# Game variables
bird = Bird()
pipes = [Pipe()]
score = 0

# Game loop
running = True
while running:
    clock.tick(30)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update game objects
    bird.update()

    # Check for collision with pipes
    for pipe in pipes:
        if bird.x + bird.bird_width > pipe.x and bird.x < pipe.x + pipe.pipe_width:
            if bird.y < pipe.top_height or bird.y + bird.bird_height > pipe.top_height + pipe.gap_height:
                running = False

        if pipe.x + pipe.pipe_width < bird.x:
            score += 1

        pipe.move()

    # Add new pipe
    if pipes[-1].x < WIDTH - 200:
        pipes.append(Pipe())

    # Remove off-screen pipes
    if pipes[0].x + pipes[0].pipe_width < 0:
        pipes.pop(0)

    # Draw game objects
    win.fill(BLACK)
    bird.draw()
    for pipe in pipes:
        pipe.draw()
    pygame.display.update()

# Clean up
pygame.quit()
