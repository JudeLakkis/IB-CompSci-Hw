import math

# Task 1
num1 = 27
num2 = 2


def frac(num1, num2):
    print('Task 1')
    a = num1 // num2
    b = num1 % num2
    print(str(a), str(b) + '/' + str(num2))
# frac(num1,num2)


# Task 2
string = 'boom'


def vowel_count1(string):
    print('Task 2')
    # print(*map(string.lower().count, "aeiou"))
    print([string.count(vowel) for vowel in 'aeiou'])
    print(' a  e  i  o  u')
# vowel_count1(string)

# Task 3


def oops():
    print('View Task 2')
# oops()

# Task 4


def vowel_count3(string):
    print('Task 4')
    a = [string.count(vowel) for vowel in 'aeiou']
    return a
# vowel_count3(string)


# Task 5
radius = 2


def volume_sphere(radius):
    print('Task 5')
    a = 4 / 3 * math.pi * radius**3
    a = float("{0:.2f}".format(a))
    print(a)
    return(a)


def surface_sphere(radius):
    a = 4 * math.pi * radius**2
    a = float("{0:.2f}".format(a))
    print(a)
    return(a)


# volume_sphere(radius)
# surface_sphere(radius)

# Task 6
def pretty():
    print('Volume:', volume_sphere(radius), 'Surface Area:', surface_sphere(radius))

# pretty()

# Task 7


def person(name, age, weight=60):
    # Having the var with a given value inside the parameter section allows for
    # a defult vaule to be set
    print(name, age, weight)

# person('jeff', '89')


# Task 8
RGBi = [255, 255, 255]


def convert_to_hex(RGB):
    for i in range(len(RGB)):
        print(hex(RGBi[i]), end=' ')


hexi = '2a84ff'


def convert_from_hex(hexi):
    print(int(hexi, 16))


convert_from_hex(hexi)
convert_to_hex(RGBi)
