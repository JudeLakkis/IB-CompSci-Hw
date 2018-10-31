# Task 6
l6 = [1, 2, 2, 1]
l6_1 = [1, 1, 13, 4, 5]
l6_2 = [1, 2, 2, 1, 13]


def scary_thirteens(x):
    total = 0
    for i in range(len(x)):
        if x[i] != 13:
            total += x[i]
        if x[i] == 13:
            total - 13
            if i != len(x) - 1:
                total -= x[i + 1]
            else:
                continue
    print(total)


scary_thirteens(l6)
scary_thirteens(l6_1)
scary_thirteens(l6_2)
print('\n')

# Task 7
l7 = [1, 2, 3, 4, 100]
l7_1 = [0, 1, 4, 5, 10, 8, 7]


def mean_kinda(x):
    total = 0
    for i in range(len(x)):
        total += x[i + 1]
    print(total)


mean_kinda(l7)
