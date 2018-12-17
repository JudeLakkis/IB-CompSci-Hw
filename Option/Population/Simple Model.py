from random import random, triangular
import matplotlib.pyplot as plt
from math import log

population = 1
step = 12
time = 0

birth_rate = 0.15
death_rate = 0.005
preditor_rate = 0.001
spanish_flu = 0.15
starvation_rate_baseline = 0.01
current_starvation_rate = starvation_rate_baseline

x_coords = []
y_coords = []

for i in range(0, 12):
    for j in range(0, population):
        if random() < birth_rate:
            population += int(triangular(1, 15, 10))
        if random() < death_rate:
            population -= 1
        if random() < preditor_rate:
            population -= 1
        if random() < spanish_flu and i > 2:
            if population <= 2:
                population -= 1
            else:
                population -= 2
        current_starvation_rate = starvation_rate_baseline * log(population, 10)
        print(current_starvation_rate)

    x_coords.append(i * step)
    y_coords.append(population)
    print(population)


def quick_resize():
    fig_size = plt.rcParams["figure.figsize"]

    fig_size[0] = 15
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size


quick_resize()

plt.figure()
plt.plot(x_coords, y_coords)
plt.xlabel('Hours')
plt.ylabel('Population Size')
plt.title('Tribbles Growing')
plt.show()
