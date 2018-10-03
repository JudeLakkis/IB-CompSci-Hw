import math
import codecs
from random import random, randint

# Task 1
# Create a function that takes an age parameter and then returns either True or False if the person is old enough to drive.
years = 22
driving_age = 21


def age(years):
    if years >= driving_age:
        print('You may drive!!')
    else:
        print('How dare you!!')

# Task 2
# Write a function that takes the lengths of three sides of a triangle and
# returns a string indicating whether it’s obtuse, acute, right or not a triangle at all.


a = 12
b = 13
c = 14


def math_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        print('Normal triangle')
    elif a**2 + b**2 > c**2:
        print('Acute Triangle')
    elif a**2 + b**2 < c**2:
        print('Obtuse Triangle')


math_triangle(a, b, c)

# Task 3
# FizzBuzz Test

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print ('Fizz')
    elif n % 5 == 0:
        print ('Buzz')
    else:
        print (str(n))

# Task 4

n = 5
r = 2


def options(n, r):
    return math.factorial(n) / math.factorial(r) * math.factorial(n - r)


if options(n, r) > 1000000:
    print('Yeah, bad luck m8')
elif options(n, r) < 1000000 and options(n, r) > 10000:
    print('Well you can give it a go if you want m8')
elif options(n, r) < 1000:
    print('Give it a go m8, you could pull it off')

# Task 5
yo_mama = []
with codecs.open('Yo Mama.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        yo_mama.append(line.strip())


def Mama(yo_mama):
    print(yo_mama[randint(0, 1040)])


Mama(yo_mama)

# Task 6
die = [1, 3, 5]


def three_dice(die):
    count = 0
    for i in range(3):
        if die[i] == randint(1, 6):
            count += 1
    print(count, 'out of 3 guesses were correct m8')
    if count == 3:
        print('Well done m8')


three_dice(die)
