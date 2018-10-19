import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Basic Window')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    if (y / 50) % 2 == 0:
	    for i in range(12):
	        x = 0
	        for j in range(12):
	            if (x / 50) % 2 == 1:
	                pygame.draw.rect(screen, (255, 255, 255), ((x, y), (50, 50)))
	                x += 50
	            elif (x / 50) % 2 == 0:
	                pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
	                x += 50

	else:
		for i in range(12):
	        x = 0
	        for j in range(12):
	            if (x / 50) % 2 == 1:
	                pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
	                x += 50
	            elif (x / 50) % 2 == 0:
	                pygame.draw.rect(screen, (255, 255, 255), ((x, y), (50, 50)))
	                x += 50
	y += 50

    pygame.display.update()
    clock.tick(60)
pygame.quit()
