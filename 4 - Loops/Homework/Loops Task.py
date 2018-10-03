# Task 1
def tasku_whan():
    print('For Loop')
    for i in range(-3, 9):
        print(i)

    print('While Loop')
    a = -3
    while a < 9:
        print(a)
        a += 1


# tasku_whan()
# Task 2


num = 1


def is_odd(num):
    if num % 2 == 1:
        print('Odd')
        return True
    else:
        print('Even')
        return False


is_odd(num)
