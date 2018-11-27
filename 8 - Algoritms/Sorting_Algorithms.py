numbers = [43, 5, 3, 1, 6, 8]


def bubble_sort(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
        print(x)

# bubble_sort(numbers)


def selection_sort(x):
    for i in range(len(x)):
        min_index = i
        for j in range(i, len(x)):
            if x[min_index] > x[j]:
                min_index = j
            x[i], x[min_index] = x[min_index], x[i]
        print(x)

# selection_sort(numbers)


def insertion_sort(x):
    for i in range(1, len(x)):
        current_value = x[i]
        j = i - 1
        while j >= 0 and current_value < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = current_value
    return x


insertion_sort(numbers)
