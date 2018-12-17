import math
import matplotlib.pyplot as plt
from random import random

population = {'m': 84, 'f': 91, 'c': 0}
step = 24

x_coords = []
y_coords_male = []
y_coords_female = []
y_coords_crab = []


def miracle_of_life():
    # Apparently 7.6% of females are infertile...
    internally_broken = 0.076

    for i in range(int(population['f'] * 0.6 * 0.3)):
        if random() > internally_broken:
            if random() > 0.5:
                population['m'] += 1
            else:
                population['f'] += 1


def end_of_the_road():
    death_rate = 0.05
    for i in range(population['m']):
        if random() <= death_rate:
            if random() > 0.5:
                population['m'] -= 1

    for i in range(population['f']):
        if random() <= death_rate:
            if random() > 0.5:
                population['f'] -= 1


def starvation():
    starvation_baseline = 0.005555

    if population['m'] + population['f'] != 0:
        current_sarvation_rate = starvation_baseline * math.log(population['m'] + population['f'], 10)

    for i in range(int(population['m'] + population['f'])):
        if random() <= current_sarvation_rate:
            if random() > 0.5:
                population['m'] -= 1
            population['f'] -= 1


def crab_uprising():
    if population['m'] + population['f'] > 1000:
        population['c'] += 2

    for i in range(int(population['c'] / 2)):
        if random() > 0.5:
            population['m'] -= 1
        population['f'] -= 1

    # print(population['c'])


def simulation_view():
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 15
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size

# Main


for weeks in range(100):

    miracle_of_life()
    end_of_the_road()
    crab_uprising()
    starvation()

    print(population)
    x_coords.append(weeks * step)
    y_coords_male.append(population['m'])
    y_coords_female.append(population['f'])
    y_coords_crab.append(population['c'])

simulation_view()

plt.figure()
plt.plot(x_coords, y_coords_male, color='b')
plt.plot(x_coords, y_coords_female, color='#FF69b4')
plt.plot(x_coords, y_coords_crab, color='r')

plt.legend(['Males', 'Females', 'Crabs'], loc='upper left')
plt.xlabel('Weeks')
plt.ylabel('Number of Beings')
plt.title('Fear the CRABS!!')

plt.show()
