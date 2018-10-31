import pygame
from random import randint

pygame.font.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Pygame Task 3')
clock = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans MS', 30)

count = 300
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # text = font.render('Circle', False, (255, 255, 255))
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    pygame.draw.circle(screen, (r, g, b), (500, 500), count, 1)
    count -= 1
    if count == 1:
        break

    # screen.blit(text, (450, 475))
    pygame.display.update()
    clock.tick(24)
pygame.quit()
