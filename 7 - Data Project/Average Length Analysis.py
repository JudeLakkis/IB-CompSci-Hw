import pickle
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

by_year = pickle.load(open("by_year.p", "rb"))

totals = {}
l = []

# Performing analysis

for year in by_year:
    for movie in by_year[year]:
        if movie[1].isdigit():
            l.append(int(movie[1]))
            average = sum(l) / len(l)
            decimal = float("{0:.3f}".format(average))
            totals[movie[0]] = decimal

a = sorted(list(totals.keys()))
b = []
for i in a:
    b.append(i[-2:])
print(b)


def quick_resize():
    fig_size = plt.rcParams["figure.figsize"]

    fig_size[0] = 15
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size


# Creating matplotlib graph number 1 from the data

quick_resize()

plt.bar(range(len(totals)), list(totals.values()), align='edge', color='r', edgecolor='k', alpha=0.5)
plt.xticks(range(len(totals)), b, size='small')
plt.ylim(100, 107), plt.xlim(0, len(b))
plt.ylabel('Average Runtime'), plt.xlabel('1900\'s Movie Years')
plt.title('Average Runtime per Year')

plt.tight_layout()
plt.show()
