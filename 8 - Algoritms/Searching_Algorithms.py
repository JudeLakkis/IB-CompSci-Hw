from random import randint

numbers = sorted([randint(0, 100) for x in range(1000)])


def binary_search(lst, search_for):
    location = len(lst) // 2
    while len(lst) > 1:
        if lst[location] > search_for:
            del lst[location:]
        else:
            del lst[:location]
        location = len(lst) // 2
    if lst[0] == search_for:
        print('True')
    else:
        print('False')


binary_search(numbers, 15)
print(numbers)
