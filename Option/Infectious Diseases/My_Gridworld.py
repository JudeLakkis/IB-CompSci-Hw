from Gridworld import GridWorld
from random import randint

# 60x40 cells, each cell is 10x10 pixels
simulation = GridWorld(60, 40, 10)

simulation.set_cell(10, 10 (255, 0, 0))

simulation.remove_cell(10, 10)

colour = simulation.get_cell(4, 2)

colours = [(255, 0, 0)(0, 255, 0)(0, 0, 255)(255, 0, 255)]
for i in range(300):
    simulation.get_cell(randint(0, 60), randint(0, 40), colours[randint(0, 3)])

for cell in simulation.cells:
    print(cell[0], cell[1], simulation.cells[cell])

s = simulation.get_surroundings(0, 0, 2)

for r in s:
    print(r)

done = False
while not done:
    done = simulation.process_events()
    simulation.update()

simulation.end()
