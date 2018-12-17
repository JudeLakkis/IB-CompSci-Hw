import matplotlib.pyplot as plt
from random import random, triangular

population = {'m': 2, 'f': 2}
step = 24  # This being a single day, or 24 hours
dead = False

x_coords = []
y_coords_male = []
y_coords_female = []


def simulation_view():
    fig_size = plt.rcParams["figure.figsize"]

    fig_size[0] = 15
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size


def birth():
    birth_rate = 0.2
    if random() < birth_rate:
        if random() > 0.5:
            population['m'] += int(triangular(1, 3, 1.5))

        if random() < 0.5:
            population['f'] += int(triangular(1, 5, 3))


def death():
    death_rate = 0.05
    if random() < death_rate:
        if random() > 0.4:
            population['m'] -= 1
        if random() > 0.6:
            population['f'] -= 1


def extinct(population):
    global dead
    if population['f'] == 0:
        population['m'] = 0
        dead = True

    if population['m'] == 0:
        population['f'] = 0
        dead = True
    print(dead)
    return dead


# __________MAIN__________ #

for weeks in range(0, 20):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # Runs for 10 days
    for j in range(0, int(population['m'] + population['f'])):
        print(int(population['m'] + population['f']))

        birth()
        death()
        extinct(population)

        print(population)

    x_coords.append(weeks * step)
    y_coords_male.append(population['m'])
    y_coords_female.append(population['f'])

simulation_view()

plt.figure()
plt.plot(x_coords, y_coords_male, color='b')
plt.plot(x_coords, y_coords_female, color='#FF69b4')

plt.legend(['Males', 'Females'], loc='upper left')
plt.xlabel('Weeks')
plt.ylabel('Number of Beings')
plt.title('Simple Gender-Based Population')
print(dead)
if dead == True:
    plt.text(max(x_coords) / 2, 1, 'Extinct...', fontsize=50)

plt.show()
