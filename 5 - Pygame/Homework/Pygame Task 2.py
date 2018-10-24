import pygame

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Basic Window')
clock = pygame.time.Clock()

radius = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if radius <= 50:
        radius += 1
    if radius >= 50:
        radius = 1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), radius, 1)
    pygame.display.update()
    clock.tick(24)
pygame.quit()
