import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bg_img = pygame.image.load("background.png")
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5

    def jump(self):
        self.velocity = -10

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        win.blit(bird_img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.gap = 150
        self.top = self.height - pipe_img.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= 3

    def draw(self):
        win.blit(pipe_img, (self.x, self.top))
        win.blit(pipe_img, (self.x, self.bottom))

# Game variables
bird = Bird()
pipes = [Pipe(WIDTH + i * 200) for i in range(4)]
score = 0
clock = pygame.time.Clock()

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
    for pipe in pipes:
        pipe.move()
        if pipe.x + pipe_img.get_width() < 0:
            pipes.remove(pipe)
            pipes.append(Pipe(WIDTH))
        if pipe.x == bird.x:
            score += 1

    # Check for collision
    for pipe in pipes:
        if bird.y < pipe.top or bird.y + bird_img.get_height() > pipe.bottom:
            if bird.x + bird_img.get_width() > pipe.x and bird.x < pipe.x + pipe_img.get_width():
                running = False

    # Draw game objects
    win.blit(bg_img, (0, 0))
    bird.draw()
    for pipe in pipes:
        pipe.draw()
    pygame.display.update()

# Clean up
pygame.quit()
