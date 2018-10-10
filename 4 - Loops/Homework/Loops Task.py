from random import randint
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


for i in range(10):
    is_odd(i)

# Task 3

all_rolls = []


def roll_dice(num):
    for i in range(num):
        all_rolls.append(randint(1, 6))
    print(all_rolls)


roll_dice(30)

# Task 4

number = '9798277985238764587235697523985372395632952739'


def odds_N_evens(number):
    even = 0
    for i in range(len(number)):
        if int(number[i]) % 2 == 0:
            even += 1
    print('Even:', even, 'Odd:', len(number) - even)


odds_N_evens(number)
