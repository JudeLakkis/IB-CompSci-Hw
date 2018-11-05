from random import randint

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
            continue
    print(total)


scary_thirteens(l6)
scary_thirteens(l6_1)
scary_thirteens(l6_2)
print('\n')

# Task 7
l7 = [1, 2, 3, 4, 100]
l7_1 = [0, 1, 4, 5, 10, 8, 7]


def middle_mean(x):
    minimum, maximum, total = min(x), max(x), sum(x)
    a = print((total - (maximum + minimum)) / (len(x) - 2))
    return a


middle_mean(l7)
middle_mean(l7_1)
print('\n')

# Task 8
l8 = [7, 4, 5, 5, 4, 7]
l8_1 = [7, 4, 5, 4, 7]
l8_2 = [4, 2, 2, 2, 2, 4, 1]


def palindrome(x):
    if x == x[::-1]:
        print('Palindrome')
        return True
    print('Not Palindrome')
    return False


palindrome(l8)
palindrome(l8_1)
palindrome(l8_2)
print('\n')

# Task 9
l9 = ['unique', 'UnIqUe', 'Same', 'Same', 'Some_Number', 'Mr.Bach', 'yeetus yeetus']


def unique_list(x):
    a = [i.upper() for i in x]
    print(list(sorted(set(a))))


unique_list(l9)
print('\n')

# Task 10
coordinates = []


def three_dimensional_coordinates(x):
    a, b, c = randint(-100, 100), randint(-100, 100), randint(-100, 100)
    point = tuple([a, b, c])
    x.append(point)
    return


def closest(x):
    if len(x) - len(set(x)) >= 1:
        print('Same')

    close_points = []
    for i in range(len(x)):
        for j in range(len(x)):
            distance = (((x[i][0]) - (x[j][0]))**2 + ((x[i][1]) - (x[j][1]))**2 + ((x[i][2]) - (x[j][2]))**2)**0.5
            if distance != 0:
                close_points += [distance]
    print(sorted(close_points)[0])
    return sorted(close_points)[0]


for i in range(10):
    three_dimensional_coordinates(coordinates)

closest(coordinates)

# Task 11
