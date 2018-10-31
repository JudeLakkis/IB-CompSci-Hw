import pygame
import itertools

# Fundamentals
# Task 1

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Pygame Task 1')
clock = pygame.time.Clock()

colours = itertools.cycle(['green', 'black'])
base_colour = next(colours)
next_colour = next(colours)
current_colour = base_colour

FPS = 60
change_every_x_seconds = 1
number_of_steps = change_every_x_seconds * FPS
step = 1

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    step += 1
    if step < number_of_steps:
        current_colour = [x + (((y - x) / number_of_steps) * step)
                          for x, y in zip(pygame.color.Color(base_colour), pygame.color.Color(next_colour))]
        # (y-x)/number_of_steps figures out the amount of change per step
    else:
        step = 1
        base_colour = next_colour
        next_colour = next(colours)

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, current_colour, (400, 400), 100)
    pygame.display.update()
    clock.tick(FPS)
