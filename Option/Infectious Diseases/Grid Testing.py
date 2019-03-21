import pygame
import time
from random import random, randint
from Gridworld import GridWorld


# Setting up the gridworld
simulation = GridWorld(60, 40, 10)
finish = False

# [Green, Recovered] [Blue, Susectible] [Yellow, Infected] [Red, Dead]
colours = [(0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 0)]

for i in range(300):
    # People Creation
    simulation.set_cell(randint(0, 60), randint(0, 40), colours[randint(0, 3)])

# Infected Grid
inf_grid = [[0] * 40 for i in range(60)]


# Main
while not finish:
    finish = simulation.process_events()
    simulation.update()

    for cell in simulation.cells:
        if simulation.cells[cell] == (0, 0, 255):
            inf_chance = 0

            # Grid Level 1
            surround_one = simulation.get_surroundings(cell[0], cell[1], 1)
            sur_one_peeps = 0
            for peeps_around in surround_one:
                for peep in peeps_around:
                    if peep == (255, 255, 0):
                        sur_one_peeps += 1
            inf_chance += 0.25 * sur_one_peeps

            # Grid Level 2
            surround_two = simulation.get_surroundings(cell[0], cell[1], 2)
            sur_two_peeps = 0
            for peeps_around in surround_two:
                for peep in peeps_around:
                    if peep == (255, 255, 0):
                        sur_two_peeps += 1
            inf_chance += 0.05 * sur_two_peeps

            # Grid Level 3
            surround_three = simulation.get_surroundings(cell[0], cell[1], 3)
            sur_three_peeps = 0
            for peeps_around in surround_three:
                for peep in peeps_around:
                    if peep == (255, 255, 0):
                        sur_three_peeps += 1
            inf_chance += 0.02 * sur_three_peeps

            # Capping so inf_chance is never higher than 97%
            if inf_chance > 0.97:
                inf_chance = 0.97

                # Infecting the peep
            if random() < inf_chance:
                simulation.set_cell(cell[0], cell[1], (255, 255, 0))

        # This adds one day to every infected peep in the inf_grid
        if simulation.cells[cell] == (255, 255, 0):
            inf_grid[cell[0]][cell[1]] += 1

        # On day 3, the infected peep lives or dies
        if inf_grid[cell[0]][cell[1]] == 9:
            inf_grid[cell[0]][cell[1]] = 0
            if random() > 0.005:
                simulation.set_cell(cell[0], cell[1], (0, 255, 0))
            else:
                simulation.set_cell(cell[0], cell[1], (255, 0, 0))

    time.sleep(0.5)

simulation.end()
