import pygame
from itertools import cycle, islice, chain

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Pygame Task 2')
clock = pygame.time.Clock()

fifty = range(1, 51)
reverse_fifty = reversed(fifty)
radius_list = cycle(chain(fifty, reverse_fifty))
radius = list(islice(radius_list, 100))


count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 255, 0), (100, 100), radius[count], 1)
    pygame.draw.circle(screen, (0, 255, 0), (150, 150), radius[count], 1)
    pygame.draw.circle(screen, (0, 255, 0), (200, 200), radius[count], 1)
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), radius[count], 1)
    pygame.draw.circle(screen, (0, 255, 0), (300, 300), radius[count], 1)
    pygame.draw.circle(screen, (0, 255, 0), (350, 350), radius[count], 1)
    pygame.draw.circle(screen, (0, 255, 0), (400, 400), radius[count], 1)

    count += 1
    if count == 100:
        count = 1

    pygame.display.update()
    clock.tick(24)
pygame.quit()
