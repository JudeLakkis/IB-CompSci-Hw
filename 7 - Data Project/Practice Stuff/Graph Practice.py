from random import randint
import matplotlib.pyplot as plt

lst1 = [randint(0, x) * x for x in range(100)]
lst2 = [randint(0, i)**2 for i in range(100)]


def graph1(lst1, lst2):
    plt.plot(lst1, lst2, 'ro')
    # plt.axis([0, 6, 0, 20])
    plt.ylabel('Some Y Numbers')
    plt.xlabel('Some X Numbers')
    plt.show()


# graph1(lst1, lst2)


def histogram():
    x = [randint(0, 100) for i in range(1000)]
    plt.hist(x, 10)
    plt.show()


histogram()
