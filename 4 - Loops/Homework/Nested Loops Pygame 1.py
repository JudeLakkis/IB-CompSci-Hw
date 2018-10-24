import pygame

screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption('Basic Window')
clock = pygame.time.Clock()

a = 0
square_size = 50
y = 0
height = 5


def grid(y, height):
    for i in range(0, height):
        if i % 2 == 1:
            x = 50
            for j in range(0, 2):
                pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
                x += 100
        elif i % 2 == 0:
            x = 0
            for k in range(0, 3):
                pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
                x += 100
        y += 50


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    grid(y, height)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
