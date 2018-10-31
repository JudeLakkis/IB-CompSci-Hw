# Task 1
l1 = [1, 2, 6]
l1_1 = [6, 1, 2, 3]
l1_2 = [13, 1, 2, 3]


def find_six(x):
    if 6 in x:
        print('True')
        return True
    else:
        print('False')
        return False


find_six(l1)
find_six(l1_1)
find_six(l1_2)
print('\n')


# Task 2
l2 = [1, 2, 3]
l2_1 = [5, 11, 9]
l2_2 = [7, 0, 0]


def reverse(x):
    print(x[::-1])
    return x[::-1]


reverse(l2)
reverse(l2_1)
reverse(l2_2)
print('\n')


# Task 3
l3 = [1, 2, 3]
l3_1 = [1, 2, 3, 4]
l3_2 = [7, 4, 6, 2]


def first_and_last(x):
    a, b = x[0], x[len(x) - 1]
    x[:] = []
    x.append(a)
    x.append(b)
    print(x)


first_and_last(l3)
first_and_last(l3_1)
first_and_last(l3_2)
print('\n')

# Task 4
l4 = [2, 5]
l4_1 = [4, 3, 10, 5, 6]
l4_2 = [4, 5, 10, 15, 16, 0, 4]


def two_or_three(x):
    if 2 in x or 3 in x:
        print('Yes')
        return True
    else:
        print('No')
        return False


two_or_three(l4)
two_or_three(l4_1)
two_or_three(l4_2)
print('\n')

# Task 5
l5 = [2, 1, 2, 3, 4]
l5_1 = [2, 2, 0]
l5_2 = [1, 3, 5]


def even(x):
    count = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            count += 1
        else:
            continue
    print(count)


even(l5)
even(l5_1)
even(l5_2)
print('\n')
