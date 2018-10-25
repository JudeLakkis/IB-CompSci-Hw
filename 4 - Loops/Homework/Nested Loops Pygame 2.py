import random
import time
import pygame

r, g, b, y = 0, 0, 0, 50
colour = [r, g, b]
drawn = False


def pyra(drawn):
    if drawn == True:
        y = 50
        for i in range(3):
            colour[f] = random.randint(0, 255)
        drawn = False

        while drawn == False:
            for j in range(7):
                x = 0
                for j in range(6 - i):
                    x += 50
                for j in range(1, i):
                    pygame.draw.rect(screen, colour[0:], ((x, y), (50, 50)))
                    x += 50
                for i in range(i, 0, -1):
                    pygame.draw.rect(screen, colour[0:], ((x, y), (50, 50)))
                    x += 50
                y += 50
            drawn = True


screen = pygame.display.set_mode((200, 300))
pygame.display.set_caption('Basic Window')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    pygame.draw.polygon(screen, (0, 0, 0), [[100, 100], [0, 200], [200, 200]], 5)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
