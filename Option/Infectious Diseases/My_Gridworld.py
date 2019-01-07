import pygame
from random import randint
from Gridworld import GridWorld

running = True

world = GridWorld(60, 40, 10)
suspectible = (0, 0, 255)
infected = (255, 0, 0)
recovered = (0, 255, 0)

for i in range(100):
    world.set_cell(randint(0, 60), randint(0, 40), suspectible)
    world.set_cell(randint(0, 60), randint(0, 40), infected)
    world.set_cell(randint(0, 60), randint(0, 40), recovered)

for row in world.get_surroundings(1, 1, 1):
    print(row)


while running:
    if world.process_events() == True:
        break
    world.update()
pygame.quit()
