import pickle
import numpy as np
import operator
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

peeps = {}
by_director = pickle.load(open("by_director.p", "rb"))


for director in by_director:
    for movie in by_director[director]:
        # print(director)
        if director not in peeps:
            peeps[director] = 1
        else:
            peeps[director] += 1

names = []
movies = []
for d in peeps:
    if peeps[d] >= 10 and peeps[d] != 253:
        clean = d.replace('\t', '')
        names.append(clean)
        movies.append(peeps[d])


def quick_resize():
    fig_size = plt.rcParams["figure.figsize"]

    fig_size[0] = 15
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size


quick_resize()


objects = names
y_pos = np.arange(len(names))
performance = movies

plt.barh(y_pos, performance, align='center', color='r', edgecolor='k', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Number of Movies')
plt.title('Directors with more than 10 movies')

plt.show()
